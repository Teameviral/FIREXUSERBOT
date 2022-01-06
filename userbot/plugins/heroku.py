import asyncio
import math
import os

import heroku3
import requests
import urllib3

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *

USERID = bot.uid
DEFAULTUSER = ALIVE_NAME or "eviralϐοy"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =====================================

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"


@borg.on(
    admin_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True)
)
async def variable(var):
    if var.fwd_from:
        return
    app = Heroku.app(HEROKU_APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await eod(
                var,
                f"Go To @FirexSupport\n Type #reveal Then click on Img \n Then Check HEROKU_APP_NAME OR HEROKU_API_KEY Are Filled Correctly",
                link_preview=False,
            )
        await var.edit("`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            variable = var.pattern_match.group(2).split()[0]
            eviral = "**ConfigVars**:" f"\n\n {variable} = `{heroku_var[variable]}`\n"
            if "eviral_STRING" in variable:
                await eor(var, "eviral String is a Sensetive Data.\nProtected By FIREX")
                return
            elif variable in heroku_var:
                await eor(var, eviral)
            else:
                return await var.edit(
                    "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await var.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await eod(
                var,
                f"Go To @FirexSupport\n Type #reveal Then click on Img \n Then Check HEROKU_APP_NAME OR HEROKU_API_KEY Are Filled Correctly.",
                link_preview=False,
            )
        await var.edit("`Setting information...weit ser`")
        variable = var.pattern_match.group(2)
        if not variable:
            return await var.edit(f"`.set var <VARS NAME> <value>`")
        value = var.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split()[1]
            except IndexError:
                return await var.edit(f"`.set var <VARS NAME> <value>`")
        await asyncio.sleep(1.5)
        if "eviral_STRING" in variable:
            await eor(var, "Successfully Changed To {value}")
            return
        elif variable in heroku_var:
            await var.edit(
                f"**{variable}**  `successfully changed to`  ->  **{value}**\nWait A Minute Changes In Heroku.."
            )
        else:
            await var.edit(
                f"**{variable}**  `successfully added with value`  ->  **{value}**\nWait A Min Changes In Heroku.."
            )
        heroku_var[variable] = value
    elif exe == "del":
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await eod(
                var,
                f"Go To @FirexSupport\n Type #reveal Then click on Img \n Then Check HEROKU_APP_NAME OR HEROKU_API_KEY Are Filled Correctly.",
                link_preview=False,
            )
        await var.edit("`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await var.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await var.edit(f"**{variable}**  `successfully deleted`")
            del heroku_var[variable]
        else:
            return await var.edit(f"**{variable}**  `is not exists`")


@bot.on(admin_cmd(pattern="var(?: |$)", outgoing=True))
@bot.on(sudo_cmd(pattern="var(?: |$)", allow_sudo=True))
async def view_config(config):
    if config.fwd_from:
        return
    app = Heroku.app(HEROKU_APP_NAME)
    app.config()
    await edit_or_reply(config, f"{app}")


@bot.on(admin_cmd(pattern="usage(?: |$)", outgoing=True))
@bot.on(sudo_cmd(pattern="usage(?: |$)", allow_sudo=True))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    """
    Get your account Dyno Usage
    """
    await edit_or_reply(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Var.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit(
        " **Dyno Usage** :\n\n"
        f" 🥇`Dyno usage for`  **{Var.HEROKU_APP_NAME}** 🥇:\n"
        f"     🔰  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " ➠ `Dyno hours quota remaining this month`:\n"
        f"     🔰 `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
        f"** ➠ Total Space: __GB**"
    )


@bot.on(admin_cmd(pattern="logs$"))
@bot.on(sudo_cmd(pattern="logs$", allow_sudo=True))
async def _(event):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await eod(
            dyno,
            f"Go To @FirexSupport\n Type #reveal Then click on Img \n Then Check HEROKU_APP_NAME OR HEROKU_API_KEY Are Filled Correctly",
            link_preview=False,
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await event.reply(
            f"Go To @FirexSupport\n Type #reveal Then click on Img \n Then Check HEROKU_APP_NAME OR HEROKU_API_KEY Are Filled Correctly.",
            link_preview=False,
        )
    # event = await eor(dyno, "Downloading Logs...")
    eviral_data = app.get_log()
    await eor(event, eviral_data)


CmdHelp("heroku").add_command(
    "usage", None, "Check your heroku dyno hours status."
).add_command(
    "set var",
    "<NEW VAR> <value>",
    "Add new variable or update existing value/variable\nAfter setting a variable the bot will restart. So be calm for a minute😃",
).add_command(
    "get var", "<VAR NAME", "Gets the variable and its value (if any) from heroku."
).add_command(
    "del var",
    "<VAR NAME",
    "Deletes the variable from heroku. Bot will restart after deleting the variable. so be calm for a minute 😃",
).add_command(
    "logs", None, "Gets the app log of 100 lines of your bot directly from heroku."
).add()
