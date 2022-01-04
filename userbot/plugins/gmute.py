"""import asyncio

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute


@bot.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def blowjob(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:
        await edit_or_reply(
            event, "I guess you need some rest. You are trying to gmute yourself😌"
        )

        return
    elif event.is_private:
        await edit_or_reply(event, "`Globally Mute Raho😂`")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event, "I need a user to gmute. Please reply or get his uid"
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, "This retard cant speak. Ye phle se chuda h 😂"
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully Globally Muted Ab bol ke Dikha 😏.")


@bot.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def cumshot(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Aur bhai kr liya aram Aajao Shuru kare Bakchodi 😎")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "Please reply to a user or add them into the command to ungmute them.",
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user can already speak freely✌️😃")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Now u Can Speak Freely")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CmdHelp("gmute").add_command(
    "gmute", "<Reply To User>", "To Mute User In Which U are Admin"
).add_command("gunmute", "<Reply Ro User", "To Unmute User In Which U are Admin").add()
"""
