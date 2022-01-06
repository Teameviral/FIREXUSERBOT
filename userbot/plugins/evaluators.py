import asyncio
import io
import os
import sys
import time
import traceback

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.utils import admin_cmd, eor, sudo_cmd

EVAL = os.environ.get("EVAL", None)
from . import *


@bot.on(admin_cmd(pattern="exec(?: |$|\n)(.*)", command="exec"))
@bot.on(sudo_cmd(pattern="exec(?: |$|\n)(.*)", command="exec", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "".join(event.text.split(maxsplit=1)[1:])
    if not cmd:
        return await eor(event, "`What should i execute?..`")
    await eor(event, "`Executing.....`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    eviraluser = await event.client.get_me()
    if eviraluser.username:
        curruser = eviraluser.username
    else:
        curruser = "@Official_FIREX"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await eor(
        event,
        f"•Command:\n`{cmd}`\n•Result:\n`{cresult}` ",
    )
    await borg.send_message(
        Config.LOGGER_ID,
        f"#EXEC \n\nTerminal command was executed sucessfully.\n\n**Command :**  `{cmd}`\n**Result :** \n{cresult}",
    )


@bot.on(admin_cmd(pattern="eval(?: |$|\n)(.*)", command="eval"))
@bot.on(sudo_cmd(pattern="eval(?: |$|\n)(.*)", command="eval", allow_sudo=True))
async def _(event):
    if EVAL == "ON":
        if event.fwd_from:
            return
        cmd = "".join(event.text.split(maxsplit=1)[1:])
        if not cmd:
            return await eor(event, "`What should i run ?..`")
        eviralevent = await eor(event, "`Running ...`")
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        try:
            await aexec(cmd, event)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        final_output = f"•  Eval : \n`{cmd}` \n\n•  Result : \n`{evaluation}` \n"
        # await eor(
        # eviralevent,
        # "**Eval Command Executed. Check out LOGGER_ID Group[Private Group Where All Message Forward]for result.**",
        # )
        if "session" in cmd:
            await eor(event, "String is a  Sensetive Data.\nSo, Its Protected By FIREX")
            return
        if "eviral_STRING" in cmd:
            await eor(event, "String is a  Sensetive Data.\nSo, Its Protected By FIREX")
            return
        else:
            await eor(
                eviralevent,
                f"{final_output}",
            )
    else:
        await edit_or_reply(
            event,
            "If U Dont Know More About Then ask With Admin.\nTo Turn On ~  `.set var EVAL ON`",
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


@bot.on(admin_cmd(pattern="bash ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="bash ?(.*)", allow_sudo=True))
async def _(event):
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "bashed.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await eor(event, f"{OUTPUT}")
    await borg.send_message(Config.LOGGER_ID, f"#BASH \n{OUTPUT}")


CmdHelp("evaluators").add_command(
    "eval", "<expr>", "Execute python script"
).add_command(
    "exec",
    "<command>",
    "Execute a Terminal command on FIREX server and shows details",
).add_command(
    "bash", "<query>", "Bash your codes on linux and gives the output in current chat"
).add_type(
    "Official"
).add()
