import requests as r
from bs4 import BeautifulSoup as bs

from . import *

link = "https://fungenerators.com/random/truth-or-dare?option="


@bot.on(admin_cmd(pattern="truth$"))
async def gtruth(ult):
    m = await eor(ult, "`Generating a Truth Statement.. `")
    nl = link + "truth"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#TruthTask**\n\n`{cm}`")


@bot.on(admin_cmd(pattern="dare$"))
async def gtruth(ult):
    m = await eor(ult, "`Generating a Dare Task.. `")
    nl = link + "dare"
    ct = r.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"**#DareTask**\n\n`{cm}`")


CmdHelp("truthdare").add_command("truth", None, "Use and See").add_command(
    "dare", None, "Use and See"
).add_info("Game").add_type("Addons").add()
