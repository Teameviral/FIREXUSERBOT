"""Available Commands:
.mf"""


from telethon import functions

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"dc"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"dc", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await edit_or_reply(event, result.stringify())


@bot.on(admin_cmd(pattern=r"owner"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"owner", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit(
        """This is my master @Eviral. Support group~@FirexSupport.  Channel~@Eviral"""
    )


CmdHelp("owner").add_command("dc", None, "Gets the DataCenter Number").add_command(
    "owner", None, "😒"
).add()
