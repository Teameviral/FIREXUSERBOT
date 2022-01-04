import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

from . import *


@bot.on(admin_cmd(pattern="byeall"))
async def _(event):
    await event.edit("Guys I Gotta Go!")
    await asyncio.sleep(3)
    await event.edit(
        """
╭━━┳╮╱╱╭┳━━━┳━━━┳╮╱╱╭╮
┃╭╮┃╰╮╭╯┃╭━━┫╭━╮┃┃╱╱┃┃
┃╰╯╰╮╰╯╭┫╰━━┫┃╱┃┃┃╱╱┃┃
┃╭━╮┣╮╭╯┃╭━━┫╰━╯┃┃╱╭┫┃╱╭╮
┃╰━╯┃┃┃╱┃╰━━┫╭━╮┃╰━╯┃╰━╯┃
╰━━━╯╰╯╱╰━━━┻╯╱╰┻━━━┻━━━╯
       [⚡️»»»『†hê~FIRE-X』«««⚡️](https://t.me/FirexSupport)
"""
    )


CmdHelp("byeall").add_command("byeall", None, "Say Bye to U all in anmation").add()
