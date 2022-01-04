""".admin Plugin for @Eviral"""
from telethon.tl.types import ChannelParticipantsAdmins

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@bot.on(admin_cmd(pattern="admins"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


CmdHelp("calladmin").add_command("admins", None, "it Help u to call admin").add_info(
    "This Command Used in Group To Call Admin"
).add_warning("Harmless Module✅").add_type("Official").add()
