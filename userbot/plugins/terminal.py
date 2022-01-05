import asyncio
import os

from FIREX.utils import admin_cmd
from userbot import ALIVE_NAME, bot
from userbot.cmdhelp import CmdHelp

eviral = str(ALIVE_NAME) if ALIVE_NAME else "Du"

running_processes: dict = {}


@bot.on(admin_cmd(pattern="term(?: |$|\n)([\s\S]*)"))
async def dc(event):
    await event.edit(f"{eviral}: Running Terminal.....")
    message = str(event.chat_id) + ":" + str(event.message.id)
    if running_processes.get(message, False):
        await event.edit("A process for this event is already running!")
        return
    cmd = event.pattern_match.group(1).strip()
    if not cmd:
        await event.edit(" Give a command or use .help terminal.")
        return
    if cmd in ("userbot.session", "env", "printenv"):
        return await event.edit(f"{eviral}: Privacy Error, This command not permitted")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]
    text = f"Terminal Command: {cmd}\nReturn code: {process.returncode}\n\n"
    if stdout:
        text += "\n[stdout]\n" + stdout.decode("UTF-8").strip() + "\n"
    if stderr:
        text += "\n[stderr]\n" + stderr.decode("UTF-8").strip() + "\n"
    if stdout or stderr:
        if not len(text) > 4096:
            return await event.edit(text)
    output = open("term.txt", "w+")
    output.write(text)
    output.close()
    await event.client.send_file(
        event.chat_id,
        "term.txt",
        reply_to=event.id,
        caption=f"{eviral}: Output too large, sending as file",
    )
    os.remove("term.txt")
    return


from userbot.cmdhelp import CmdHelp

CmdHelp("terminal").add_command("term", None, "Reply to python file").add()
