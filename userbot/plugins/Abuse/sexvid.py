from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="xxshort?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1649926429)
            )
            await event.client.send_message(chat, "🤪{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @OpGufaBot")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(admin_cmd(pattern="xxlong?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1649926429)
            )
            await event.client.send_message(chat, "😏{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @OpGufaBot")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


CmdHelp("sexvideo").add_command(
    "xxshort", None, "For Short Se* Videos (Warning 18+ Only) NSFW"
).add_command("xxlong", None, "For Long Se* Video").add_info("18+ Video").add_warning(
    "Dont watch below 18+"
).add_type(
    "Abuse"
).add()
