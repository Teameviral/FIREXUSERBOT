from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


@borg.on(admin_cmd(pattern="recognized ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    cat = await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("unblock @Rekognition_Bot and try again")
            await cat.delete()
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            cat = response.message.message
            await event.edit(cat)

        else:
            await event.edit("sorry, I couldnt find it")


@borg.on(admin_cmd(pattern="purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@Filetolinkfirebot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@Filetolinkfirebot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@borg.on(admin_cmd(pattern="limit ?(.*)"))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                danish = await conv.get_response()
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @spambot `and retry!")


@borg.on(admin_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a url message.**")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @chotamreaderbot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@bot.on(admin_cmd(pattern="dm ?(.*)"))
@bot.on(sudo_cmd(pattern="dm ?(.*)", allow_sudo=True))
async def _(event):
    if len(event.text) > 3:
        if not event.text[3] == " ":
            return
    d = event.pattern_match.group(1)
    c = d.split(" ")
    try:
        chat_id = await get_user_id(c[0])
    except Exception as e:
        return await eod(event, f"`{e}`")
    msg = ""
    hunter = await event.get_reply_message()
    if event.reply_to_msg_id:
        await bot.send_message(chat_id, hunter)
        await eod(event, "**[Done]**")
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await bot.send_message(chat_id, msg)
        await eod(event, "**[Done]**")
    except BaseException:
        await eod(f"**Invalid Syntax !!**\n\n`.dm <Username or UserID> <message>`")


CmdHelp("checkbot").add_command(
    "reader", None, "open that url in telegraph"
).add_command("purl", None, "Get a direct Downmpad Link").add_command(
    "history", None, "Reply To any User get Detail Of her/Hime"
).add_command(
    "recognize", None, "Send Detail about it"
).add_command(
    "limit", None, "Chech If u are limited or not"
).add_command(
    "dm",
    "<username or user id> <message>",
    "Sends a DM to given username with required msg",
).add_info(
    "Its Work Like Bot On Telegram Access Through Userbot"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Official"
).add()
