"""Get information about an user on GitHub
Syntax: .github USERNAME"""
import requests

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, eor, sudo_cmd


@bot.on(admin_cmd(pattern="gthub (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gthub (.*)", allow_sudo=True))
async def gitsearch(event):
    xx = await eor(event, get_string("com_2"))
    try:
        usrname = event.pattern_match.group(1)
    except BaseException:
        return await xx.edit("`Search for whom? Give me a user name!!`")
    url = f"https://api.github.com/users/{usrname}"
    ult = requests.get(url).json()
    try:
        uname = ult["login"]
        uid = ult["id"]
        upic = ult["avatar_url"]
        ulink = ult["html_url"]
        uacc = ult["name"]
        ucomp = ult["company"]
        ublog = ult["blog"]
        ulocation = ult["location"]
        ubio = ult["bio"]
        urepos = ult["public_repos"]
        ufollowers = ult["followers"]
        ufollowing = ult["following"]
    except BaseException:
        return await xx.edit("`No such user found...`")
    fullusr = f"""
**[GITHUB]({ulink})**
**Name** - {uacc}
**UserName** - {uname}
**ID** - {uid}
**Company** - {ucomp}
**Blog** - {ublog}
**Location** - {ulocation}
**Bio** - {ubio}
**Repos** - {urepos}
**Followers** - {ufollowers}
**Following** - {ufollowing}
"""
    await xx.delete()
    await eviral_bot.send_file(
        event.chat_id,
        upic,
        caption=fullusr,
        link_preview=False,
    )


CmdHelp("gthub").add_command("gthub", "None", "Use and See").add_info(
    "Its help u to find detail of any github a count"
).add()
