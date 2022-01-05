import asyncio
import io

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME
from userbot import bot as FIREX

from . import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "eviral"
eviral_logo = "eviral_logo1"


@FIREX.on(admin_cmd(pattern=r"listcmnd"))
@FIREX.on(sudo_cmd(pattern=r"listcmnd", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls userbot/plugins"
    thumb = eviral_logo
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"List of Plugins in FIREX :- \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nHELP:- If you want to know the commands for a plugin, do :- \n.plinfo <plugin name> without the < > brackets. \nJoin https://t.me/eviralSupport for help."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmd_list.text"
            eviral_file = await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(
                eviral_file,
                f"Output Too Large. This is the file for the list of plugins in FIREX.\n\n**BY :-** {DEFAULTUSER}",
            )
            await event.delete()


from userbot.cmdhelp import CmdHelp

CmdHelp("listcmnd").add_command("listcmnd", None, "to see all cmnd list").add()
