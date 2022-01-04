import asyncio
import random

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *

NUMBER = ["0", "1"]

tired_response = [
    "I am little tired, Please give me some rest",
    "Who are you to ask me questions Continuously",
    "Leave me alone for some times",
    "Time to Sleep, I will get back to you soon",
    "I have a job to do, Come back later",
    "I need to rest, leave me alone for some times",
    "I am not feeling well, Please Come back later",
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
            message="""{}""".format(random.choice(tired_response)),
            reply_to=event.message.id,
        )


@bot.on(admin_cmd(pattern="adai(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="adai(?: |$)(.*)", allow_sudo=True))
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
        event = await edit_or_reply(event, "Adding ai to user")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Added Ai To User")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "adding ai to user")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"added ai to user")


@bot.on(admin_cmd(pattern="rmvai(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="rmvai(?: |$)(.*)", allow_sudo=True))
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
        event = await edit_or_reply(event, "Removin Ai From user")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Removed successfully")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Removing Ai From User")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Removed Ai From User")


CmdHelp("chatbot").add_command(
    "adai", "<reply to a user message>", "add ai bot"
).add_command("rmvai", "<reply to same user>", "remove ai").add_info(
    "auto reply chatbot"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Addons"
).add()
