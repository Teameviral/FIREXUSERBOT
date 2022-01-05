import asyncio
import random

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *

NUMBER = ["0", "1"]

OS = [
    "IF U NEED ANY HELP U CAN TYPE WHEN HE COME BACK HE WILL REPLY U",
    "PLS DONT DISTURB HIM eviral IS BUSY NOW WHEN HE COME BACK HE REPLY U",
    "DON'T BREAK THE HEART OF THE HACKER BCOZ U DON'T KNOW WHAT WILL HAPPN TN",
    "I AM 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』➙𖤍 𝕄ℝ.ℍ𝔸ℂ𝕂𝔼ℝ࿐",
    "I KNOW U ARE WAITING FOR ME I WILL BE BACK SOON",
]

que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.5)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(OS)),
            reply_to=event.message.id,
        )


@bot.on(admin_cmd(pattern="lstarts(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lstarts(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "eviral")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"『🔱 eviral ™🔱』IS STARTING GAME")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "eviral")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"eviral {ALIVE_NAME}")


@bot.on(admin_cmd(pattern="lstops(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lstops(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "GAME OVER")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"GAME HAS STOPED")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "GAME OVER")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"eviral STOPED RAID {ALIVE_NAME}")


CmdHelp("lpersonal").add_command(
    "lstarts", None, "Reply to him or her to start eviral personal file"
).add_command("lstops", None, "Reply To her Ya him To stop eviral personal file").add()
