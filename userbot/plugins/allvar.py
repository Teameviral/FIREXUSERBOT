from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *

msg = f"""
TMP_DOWNLOAD_DIRECTORY = {Config.TMP_DOWNLOAD_DIRECTORY}
ALIVE_NAME = {Config.ALIVE_NAME}
ALIVE_MSG = {Config.ALIVE_MSG}
ABUSE = {Config.ABUSE}
YOUR_GROUP = {Config.YOUR_GROUP}
YOUR_CHANNEL = {Config.YOUR_CHANNEL}
BOY_OR_GIRL = {Config.BOY_OR_GIRL}
AWAKE_PIC = {Config.AWAKE_PIC}
OP_PIC = {Config.HELP_PIC}
ALIVE_PIC = {Config.ALIVE_PIC}
BIO_MSG = {Config.BIO_MSG}
PM_PIC = {Config.PM_PIC}
PM_MSG = {Config.PM_MSG}
MAX_FLOOD_IN_PM = {Config.MAX_FLOOD_IN_PM}
LOGGER_ID = {Config.LOGGER_ID}
APP_ID = {Config.APP_ID}
SUDO_USERS = {Config.SUDO_USERS}
SUDO_COMMAND_HAND_LER = {Config.SUDO_COMMAND_HAND_LER}
COMMAND_HAND_LER = {Config.COMMAND_HAND_LER}
API_HASH = {Config.API_HASH}
PLUGIN_CHANNEL = {Config.PLUGIN_CHANNEL}
PRIVATE_GROUP_BOT_API_ID = {Config.PRIVATE_GROUP_BOT_API_ID}
PRIVATE_GROUP_ID = {Config.PRIVATE_GROUP_ID}
PM_LOGGR_BOT_API_ID = {Config.PM_LOGGR_BOT_API_ID}
HEROKU_API_KEY = {Config.HEROKU_API_KEY}
HEROKU_APP_NAME = {Config.HEROKU_APP_NAME}
BOT_USERNAME = {Config.BOT_USERNAME}
NO_OF_BUTTONS = {Config.NO_OF_BUTTONS}
NO_OF_COLUMNS = {Config.NO_OF_COLUMNS}
EMOJI_IN_HELP1 = {Config.EMOJI_IN_HELP1}
EMOJI_IN_HELP2 = {Config.EMOJI_IN_HELP2}
ALIVE_EMOJI = {Config.ALIVE_EMOJI}
PM_DATA = {Config.PM_DATA}
"""

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


@bot.on(admin_cmd(pattern="allvar$"))
@bot.on(admin_cmd(pattern="allvar$", allow_sudo=True))
async def eviral_a(event):
    try:
        eviral = await bot.inline_query(botname, "varboy")
        await eviral[0].click(event.chat_id)
        if event.sender_id == Eviral:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("allvar").add_command("allvar", None, "υѕє αи∂ ѕєє").add_info(
    "U can See All Var Except eviral_STRING"
).add_warning("Harm Module").add_type("Official").add()
