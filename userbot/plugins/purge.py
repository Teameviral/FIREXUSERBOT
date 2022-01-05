from asyncio import sleep

import telethon
from telethon.errors import rpcbaseerrors

from FIREX.utils import admin_cmd, errors_handler, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

BOTLOG_CHATID = Config.LOGGER_ID
from userbot import BOTLOG


async def get_target_message(event):
    if event.is_reply and (await event.get_reply_message()).sender_id == borg.uid:
        return await event.get_reply_message()
    async for message in borg.iter_messages(await event.get_input_chat(), limit=20):
        if message.out:
            return message


async def await_read(chat, message):
    chat = telethon.utils.get_peer_id(chat)

    async def read_filter(read_event):
        return read_event.chat_id == chat and read_event.is_read(message)

    fut = borg.await_event(events.MessageRead(inbox=False), read_filter)

    if await is_read(borg, chat, message):
        fut.cancel()
        return

    await fut


@borg.on(admin_cmd(pattern=r"edit"))
@errors_handler
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(
            BOTLOG_CHATID, "Edit query was executed successfully"
        )


@borg.on(admin_cmd(pattern=r"del"))
@errors_handler
async def delete_it(delme):
    """For .del command, delete the replied message."""
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Deletion of message was successful"
                )
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Well, I can't delete a message"
                )


@bot.on(admin_cmd(pattern=r"purge", outgoing=True))
@bot.on(sudo_cmd(pattern=r"purge", allow_sudo=True))
@errors_handler
async def fastpurger(purg):
    """For .purge command, purge all messages starting from the reply."""
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Fast purge complete!\n`Purged " + str(count) + " messages.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    await done.delete()
    await purg.delete()


# @register(outgoing=True, pattern="^.purgeme")
@bot.on(admin_cmd(pattern=r"purgeme", outgoing=True))
@bot.on(sudo_cmd(pattern=r"purgeme", allow_sudo=True))
@errors_handler
async def purgeme(delme):
    """For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    i = 1
    await smsg.delete()
    await delme.delete()


@bot.on(admin_cmd(pattern=r"sd", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sd", allow_sudo=True))
@errors_handler
async def selfdestruct(destroy):
    """For .sd command, make seflf-destructable messages."""
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID, "sd query done successfully")


CmdHelp("purge").add_command(
    "del", "<reply to a msg>", "Deletes the replied msg."
).add_command("edit", "<reply to a msg>", "Edits the replied msg").add_command(
    "purge", "<reply>", "Purges all messages starting from the reply."
).add_command(
    "purgeme", "<count>", "Deletes 'x' amount of your latest messages."
).add_command(
    "sd",
    "<time> <message>",
    "Creates a message that selfdestructs in 'x' seconds. Keep the seconds under 100 since it puts your bot to sleep",
).add()
