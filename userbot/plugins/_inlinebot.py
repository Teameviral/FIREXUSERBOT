import asyncio
import html
import os
import re
from math import ceil
from re import compile

from telethon import Button, custom, events, functions
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot.Config import Config

from . import *

DEFAULTUSER = ALIVE_NAME or "eviral"
eviral_row = Config.BUTTONS_IN_HELP
eviral_emoji1 = Config.EMOJI_IN_HELP1 or "♦️"
eviral_emoji2 = Config.EMOJI_IN_HELP2 or "♦️"
alive_emoji = Config.ALIVE_EMOJI or "⚜"
eviral_pic = Config.PM_PIC or "https://telegra.ph/file/b76f4a906f05c059e046a.jpg"
cstm_pmp = Config.PM_MSG
ALV_PIC = Config.ALIVE_PIC
help_pic = "https://telegra.ph/file/b76f4a906f05c059e046a.jpg"
VAR_PIC = Config.ALIVE_PIC
PREV_REPLY_MESSAGE = {}
mybot = Config.BOT_USERNAME
COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

LOG_GP = Config.LOGGER_ID
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
)
TOTAL_WARN = Config.MAX_FLOOD_IN_PM
USER_BOT_WARN_ZERO = (
    "Enough Of Your Flooding In My Master's PM!! \n\n**🚫 Blocked and Reported**"
)

eviral_FIRST = "__{}__\nPlease choose why u are here.♥️!!"


var_txt = """
     ♦️ALL VAR♦️
•ALIVE_NAME = `{}`
•ALIVE_MSG = `{}`
•ABUSE = {}
•ASSISTANT = {}
•AWAKE_PIC = `{}`
•BOT_USERNAME = `{}`
•BOT_TOKEN = `{}`
•EXTRA_PLUGIN = `{}`
•OP_PIC = `{}`
•PM_DATA = {}
•PM_PIC = `{}`
•LOGGER_ID = `{}`
"""


alive_txt = """
**Hey,
     {}**
  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
  🏅Bø† ẞ†α†µѕ🏅
**•{}•Oաղ̃ҽ̈r :** {}
**•{}•FIRE-X :** {}
**•{}•†ҽ̀lҽ́ƭhøղ  :** {}
**•{}•Ãbûßê     :** {}
**•{}•ßudø      :** {}
**•{}•Bø†       :** {}
"""


def button(page, modules):
    Row = eviral_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
                    f"{eviral_emoji1} " + pair + f" {eviral_emoji2}",
                    data=f"Information[{page}]({pair})",
                )
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
                f"ẞαƈƙ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(f"🔥 ❌ 🔥", data="close"),
            custom.Button.inline(
                f"ɳ̃êӿ†", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]

    modules = CMD_HELP


if Config.BOT_USERNAME is not None and firebot is not None:

    @firebot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "FIREX_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            help_msg = f"⚜『{eviral_mention}』⚜\n\n⭐ 𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍⭆ `{len(CMD_HELP)}`\n🔥 𝚃𝚘𝚝𝚊𝚕 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜⭆ `{len(apn)}`\n📖 Pαցҽ⭆ 1/{veriler[0]}\n"
            if help_pic and help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="Help Menu",
                    buttons=veriler[1],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    f"Hey! Only use .op please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "alive":
            leg_end = alive_txt.format(
                Config.ALIVE_MSG,
                alive_emoji,
                eviral_mention,
                alive_emoji,
                eviralversion,
                alive_emoji,
                version.__version__,
                alive_emoji,
                abuse_m,
                alive_emoji,
                is_sudo,
                alive_emoji,
                Config.BOY_OR_GIRL,
            )
            alv_btn = [
                [Button.url(f"{eviral_USER}", f"tg://openmessage?user_id={Eviral}")],
                [
                    Button.url("My Channel", f"https://t.me/{my_channel}"),
                    Button.url("My Group", f"https://t.me/{my_group}"),
                ],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=leg_end,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=leg_end,
                    title="FIREX Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=leg_end,
                    title="FIREX Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "fsub":
            fsub_btn = [
                [Button.url(f"{eviral_USER}", f"tg://openmessage?user_id={Eviral}")],
                [
                    Button.url("📍My Channel📍", f"https://t.me/{my_channel}"),
                    Button.url("💝My Group💝", f"https://t.me/{my_group}"),
                ],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.article(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    buttons=alv_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "pm_warn":
            lege_nd = eviral_FIRST.format(mssge)
            result = builder.photo(
                file=eviral_pic,
                text=lege_nd,
                buttons=[
                    [
                        custom.Button.inline("📝 Request 📝", data="req"),
                        custom.Button.inline("💬 Chat 💬", data="chat"),
                    ],
                    [custom.Button.inline("🚫 Spam 🚫", data="heheboi")],
                    [custom.Button.inline("Curious ❓", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "varboy":
            le_gend = var_txt.format(
                Config.ALIVE_NAME,
                Config.ALIVE_MSG,
                Config.ABUSE,
                Config.ASSISTANT,
                Config.AWAKE_PIC,
                Config.BOT_USERNAME,
                Config.BOT_TOKEN,
                Config.EXTRA_PLUGIN,
                Config.HELP_PIC,
                Config.PM_DATA,
                Config.PM_PIC,
                Config.LOGGER_ID,
            )
            var_btn = [
                [Button.url(f"{eviral_USER}", f"tg://openmessage?user_id={Eviral}")],
                [
                    Button.url("🔹️Command🔹️", f"http://telegra.ph/Astronomer-10-07"),
                ],
            ]
            if VAR_PIC and VAR_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    VAR_PIC,
                    text=le_gend,
                    buttons=var_btn,
                    link_preview=False,
                )
            elif VAR_PIC:
                result = builder.document(
                    VAR_PIC,
                    text=le_gend,
                    title="FIREX Alive",
                    buttons=var_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=le_gend,
                    title="FIREX Alive",
                    buttons=var_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**⚜  FIRE_X ⚜**",
                buttons=[
                    [Button.url("♥️ Tutorial ♥", "https://youtu.be/9dQgdUJfk_k")],
                    [Button.url("📍 𝚁𝚎𝚙𝚘 📍", "https://github.com/Teameviral/FIREX")],
                    [
                        Button.url(
                            "💞 Deploy 💞",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeameviral%2FFIREX&template=https%3A%2F%2Fgithub.com%2FTeameviral%2FFIREX",
                        )
                    ],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            result = builder.photo(
                ALV_PIC,
                text="""Hey! This is [FIRE-X](https://t.me/Official_FIREX) \nYou can know more about me from the links given below 👇""",
                buttons=[
                    [
                        custom.Button.url(
                            "⭐ Repo ⭐", "https://Github.com/Teameviral/FIREX"
                        ),
                        custom.Button.url(
                            "⚡ Repl ⚡",
                            "https://replit.com/@KrishnaJaiswal1/FIREX#main.py",
                        ),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🔰 This is FIRE-X PM Security for {eviral_mention} to keep away unwanted retards from spamming PM..."
            )

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(eviral):
        if eviral.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {eviral_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await eviral.answer(fck_bit, cache_time=0, alert=True)
            return
        await eviral.get_chat()
        eviral.query.user_id
        await eviral.edit(
            "Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**"
        )
        await asyncio.sleep(2)
        await eviral.edit(
            "Which Type Of Request U Want?",
            buttons=[
                [Button.inline("Register", data="school")],
                [Button.inline("As Usual", data="tg_okay")],
            ],
        )
        yup_text = "`Warning`-❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"
        await bot.send_message(eviral.query.user_id, yup_text)

    @firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
    async def yeahbaba(eviral):
        if eviral.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master.This Is for other users"
            await eviral.answer(fck_bit, cache_time=0, alert=True)
        else:
            await eviral.edit(
                f"✅ **Request Registered** \n\n{eviral_mention} will now decide to talk with u or not\n😐 Till then wait patiently and don't spam!!"
            )
            target = await eviral.client(GetFullUserRequest(eviral.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = eviral.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
                tosend = f"**👀 Hey {eviral_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
                await bot.send_message(LOG_GP, tosend)

    @firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"school")))
    async def yeahbaba(eviral):
        if eviral.query.user_id == bot.uid:
            fck_bit = f"This Is For Other user"
            await eviral.answer(fck_bit, cache_time=0, alert=True)
        else:
            await eviral.edit(
                f"✅ **Request Registered** \n\n{eviral_mention} will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
            )
            target = await eviral.client(GetFullUserRequest(eviral.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = eviral.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {eviral_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {eviral_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {eviral_mention} !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(eviral):
        if eviral.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master{eviral_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await eviral.answer(fck_bit, cache_time=0, alert=True)
            return
        await eviral.get_chat()
        eviral_id = eviral.query.user_id
        await eviral.edit("Okay let Me Think🤫")
        await asyncio.sleep(2)
        await eviral.edit("Okay Giving You A Chance🤨")
        await asyncio.sleep(2)
        await eviral.edit(
            "Will You Spam?",
            buttons=[
                [Button.inline("Yes", data="lemme_ban")],
                [Button.inline("No", data="hmm")],
            ],
        )

        reqws = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"

        await bot.send_message(eviral.query.user_id, reqws)
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={eviral_id}). Wants To Request Something.",
            buttons=[Button.url("Contact Him", f"tg://user?id=eviral_id")],
        )

    @firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
    async def yes_ucan(eviral):
        if eviral.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await eviral.answer(lmaoo, cache_time=0, alert=True)
            return
        await eviral.get_chat()
        await asyncio.sleep(2)
        eviral.query.user_id
        await eviral.edit("Okay You Can Wait Till Wait")
        hmmmmm = "Okay Kindly wait  i will inform you"
        await bot.send_message(eviral.query.user_id, hmmmmm)

    @firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
    async def yes_ucan(eviral):
        if eviral.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await eviral.answer(lmaoo, cache_time=0, alert=True)
            return
        await eviral.get_chat()
        await asyncio.sleep(2)
        eviral_id = eviral.query.user_id
        await eviral.edit("Get Lost Retard")
        ban = f"Pahli Fursat Me Nikal\nU Are Blocked"
        await bot.send_message(eviral.query.user_id, ban)
        await bot(functions.contacts.BlockRequest(eviral.query.user_id))
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={eviral_id}). Has Been Blocked Due to Choose Spam",
            buttons=[Button.url("Contact Him", f"tg://user?id=eviral_id")],
        )

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(2)).decode("UTF-8")
        eviral = hunter.split("+")
        if not event.sender_id == int(eviral[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(eviral[1]), int(eviral[0])))
        except UserNotParticipantError:
            return await event.answer("You need to join the channel first.", alert=True)
        await bot.edit_permissions(
            event.chat_id, int(eviral[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            current_page_number = 0
            simp = button(current_page_number, CMD_HELP)
            button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                f"",
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "This Is For My Master Only.Dont Try To Touch Again. Deploy Ur Own © FIRE-X™"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(
                f"{eviral_emoji1} Re-Open Menu {eviral_emoji2}", data="reopen"
            )
            await event.edit(
                f"**⚜️ FIRE-X Mêñû Prõvîdêr háš běěn čłøšĕd ⚜️**\n\n**Bot Of :**  {eviral_mention}\n\n            [©️FIRE-X]({chnl_link})",
                buttons=veriler,
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "κγα υиgℓι καя янє нο мєяє ϐοτ ραя αgαя ϲнαнιγє τοн κнυ∂ κα ϐαиα ℓο иα. Aα נατє нο υиgℓι καяиє мєяє ϐοτ ρє.   ©FIRE-X"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @firebot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"⚜『{eviral_mention}』⚜\n\n⭐ 𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍⭆ `{len(CMD_HELP)}`\n🔥 𝚃𝚘𝚝𝚊𝚕 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜⭆ `{len(apn)}`\n📖 Pαցҽ⭆ 1/{veriler[0]}\n",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "This Button Only For My Master.   ©FIRE-X",
                cache_time=0,
                alert=True,
            )

    @firebot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    f"{alive_emoji} " + cmd[0] + f" {alive_emoji}",
                    data=f"commands[{commands}[{page}]]({cmd[0]})",
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append(
            [
                custom.Button.inline(
                    f"{eviral_emoji1} Help Menu {eviral_emoji2}", data=f"page({page})"
                )
            ]
        )
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**📗 𝙵𝚒𝚕𝚎 :**  `{commands}`\n**🔢 Total Commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. ©FIRE-X™",
                cache_time=0,
                alert=True,
            )

    @firebot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 𝙵𝚒𝚕𝚎 :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += (
                    f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                )
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n"
            result += f"**ℹ️ 𝙸𝚗𝚏𝚘 :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += (
                f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
            )
        else:
            result += f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n"
            result += f"**⌨️ 𝙵𝚘𝚛 𝙴𝚡𝚊𝚖𝚙𝚕𝚎 :**  `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(
                        f"{eviral_emoji1} Return {eviral_emoji2}",
                        data=f"Information[{page}]({cmd})",
                    )
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "MY MASTER ONLY CAN ACCESS THIS BUTTON. DEPLOY UR OWN ©FIRE-X™ ",
                cache_time=0,
                alert=True,
            )
