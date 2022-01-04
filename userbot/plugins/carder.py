from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from FIREX import CmdHelp
from FIREX import bot as FIREX
from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd


@FIREX.on(admin_cmd("gencc$"))
@FIREX.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(eviralevent):
    if eviralevent.fwd_from:
        return
    eviralcc = Faker()
    eviralname = eviralcc.name()
    eviraladre = eviralcc.address()
    eviralcard = eviralcc.credit_card_full()

    await edit_or_reply(
        eviralevent,
        f"__**👤 NAME :- **__\n`{eviralname}`\n\n__**🏡 ADDRESS :- **__\n`{eviraladre}`\n\n__**💸 CARD :- **__\n`{eviralcard}`",
    )


@FIREX.on(admin_cmd(pattern="bin ?(.*)"))
@FIREX.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    eviral_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {eviral_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@FIREX.on(admin_cmd(pattern="register ?(.*)"))
@FIREX.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    eviral_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {eviral_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@FIREX.on(admin_cmd(pattern="password ?(.*)"))
@FIREX.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    eviral_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {eviral_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
