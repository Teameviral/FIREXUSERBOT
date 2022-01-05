import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from userbot.Config import Config

from . import *

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS")
LOP = Var.HEROKU_APP_NAME
eviral = Var.HEROKU_API_KEY


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target


@bot.on(admin_cmd(pattern="sudo"))
async def sudo(event):
    sudo = "True" if Config.SUDO_USERS else "False"
    users = sudousers
    if sudo == "True":
        await eor(event, f"📍 **Sudo :**  `Enabled`\n\n📝 **Sudo users :**  `{users}`")
    else:
        await eod(event, f"📍 **Sudo :**  `Disabled`")


@bot.on(admin_cmd(pattern="addsudo(?: |$)"))
async def add(event):
    ok = await eor(event, "**⌛ Adding Sudo Users...**")
    bot = "SUDO_USERS"
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        await eod(ok, "**Please Set-Up**  `HEROKU_APP_NAME` **to add sudo users!!**")
        return
    heroku_Config = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await eod(ok, f"Reply to a user to add them in sudo.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await ok.edit(
        f"✅** Added**  `{target}`  **in Sudo User.**\n\n Restarting Heroku. Wait A Minute."
    )
    heroku_Config[bot] = newsudo


@bot.on(admin_cmd(pattern="rmsudo"))
async def remove_sudo(event):
    Heroku = heroku3.from_key(eviral)
    app = Heroku.app(LOP)
    heroku_var = app.config()
    if not event.is_reply:
        return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")
    if event.is_reply:
        id = (await event.get_reply_message()).sender_id
        name = (await bot.get_entity(id)).first_name
        op = re.search(str(id), str(sudousers))
        if op:
            i = ""
            amazing = sudousers.split(" ")
            amazing.remove(str(id))
            i += str(amazing)
            x = i.replace("[", "")
            xx = x.replace("]", "")
            xxx = xx.replace(",", "")
            done = xxx.replace("'", "")
            heroku_var["SUDO_USERS"] = done
            await event.edit(
                f"The **{name}** Has Been Removed Successfully(Please Wait I am Restarting)"
            )
        else:
            await event.edit(f"The {name} Is Not in Sudo 😑😑")
        if heroku_var["SUDO_USERS"] == None:
            await event.edit(f"The Sudo List Is Empty😑😑")


@bot.on(admin_cmd("listsudo"))
async def sudolists(event):
    op = await event.edit("Checking All Sudos")
    Heroku = heroku3.from_key(eviral)
    app = Heroku.app(LOP)
    app.config()
    if not sudousers:
        return await event.edit("Sudo List Is Empty")
    sudos = sudousers.split(" ")
    sudoz = "**»Sudo List«**"
    for sudo in sudos:
        k = await bot.get_entity(int(sudo))
        pro = f"\n[**Name:** {k.first_name} \n**Username:~** @{k.username or None}]\n"
        sudoz += pro
    await op.edit(sudoz)


CmdHelp("sudo").add_command(
    "sudo", None, "Check If Your Bot Has Sudo Enabled!!"
).add_command(
    "addsudo", "<reply to user>", "Adds replied user to sudo list."
).add_command(
    "rmsudo",
    "<reply to user>",
    "Removes the replied user from your sudo list if already added.",
).add_info(
    "Manage Sudo."
).add_warning(
    "⚠️ Grant Sudo Access to someone you trust!"
).add_type(
    "Official"
).add()
