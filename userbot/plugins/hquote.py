import random

import requests
from bs4 import BeautifulSoup as bs

from userbot.cmdhelp import CmdHelp

from . import *


@bot.on(admin_cmd(pattern="hquote"))
async def hurray(e):
    a = requests.get("https://www.brainyquote.com/topics/hackers-quotes")
    bt = bs(a.content, "html.parser", from_encoding="utf-8")
    out = random.choice(bt.find_all("div", "clearfix"))
    mt = ""
    mt += out.findNext().text
    mt += "\n\n**" + out.findNext().findNext().text + "**"
    await eor(e, mt)


CmdHelp("hquote").add_command("hquote", None, "Use and See").add()
