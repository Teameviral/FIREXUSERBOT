from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from FIREX.utils import admin_cmd


@bot.on(admin_cmd("grab ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to text message```")
        return
    chat = ""
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=864838521)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Hi"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await bot.send_file(event.chat_id, response.message)


from userbot.cmdhelp import CmdHelp

CmdHelp("grab").add_command("grab", None, "Reply To any message").add()
