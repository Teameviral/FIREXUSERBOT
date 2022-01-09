import asyncio
import os
import re
import sys

os.system("pip install telethon==1.24.0")

import telethon.utils
from telethon import Button, TelegramClient, custom, events

from userbot import LOGS, bot, eviralversion
from userbot.Config import Config
from var import Var

from .start import abuses, addons, assistants, hekp, install, module, spams

l1 = Config.COMMAND_HAND_LER
l2 = Config.SUDO_COMMAND_HAND_LER
eviral_PIC = "https://telegra.ph/file/b76f4a906f05c059e046a.jpg"

perf = "[ †hê FIRE-X ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"eviral_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.firebot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.firebot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting FIREX ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 FIREX Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")

firebot = bot.firebot


async def killer():
    eviral_USER = bot.me.first_name
    Eviral = bot.uid
    legd_mention = f"[{eviral_USER}](tg://user?id={Eviral})"
    name = f"{legd_mention}'s Assistant"
    description = (
        f"I am Assistant Of {legd_mention}.This Bot Can Help U To Chat With My Master"
    )
    codetechbot = await firebot.get_me()
    bot_id = codetechbot.first_name
    if bot_id.endswith("Assistant"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file(
                "@BotFather", "userbot/resources/pics/-4965507108355287505_121.jpg"
            )
        except Exception as e:
            print(e)
    # else:
    # print("Turn On ASSISTANT to Use This")


async def evirals():
    eviral_USER = bot.me.first_name
    Eviral = bot.uid
    legd_mention = f"[{eviral_USER}](tg://user?id={Eviral})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully FIREX Has Been Deployed \nMy Master ~ 『{legd_mention}』 \nVersion ~ {eviralversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await firebot.send_file(
            bot.me.id, eviral_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    await event.delete()
    codetechbot = await firebot.get_me()
    bot_id = codetechbot.first_name
    if event.query.user_id is not bot.uid:
        await firebot.send_message(
            event.chat_id,
            message=f"Hey Sir It's Me {bot_id}, Your Assistant! How Can I Help U?",
            buttons=[
                [
                    Button.url(" Support ", "https://t.me/FirexSupport"),
                    Button.url(" Updates ", "https://t.me/Official_FIREX"),
                ],
                [
                    custom.Button.inline("Settings", data="osg"),
                    custom.Button.inline("Restart", data="restart"),
                ],
                [custom.Button.inline("Hack", data="hack")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"restart")))
async def restart(event):
    await event.delete()
    await firebot.send_message(event.chat_id, "Restarting")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await firebot.send_message(
            event.chat_id,
            message=f"Var Explaination Without Going To Heroku",
            buttons=[
                [
                    custom.Button.inline("Var Explain", data="var"),
                    custom.Button.inline("All Var", data="allvar"),
                    custom.Button.inline("Extra Setting", "extraset"),
                ],
                [custom.Button.inline("Back", data="start")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"var")))
async def users(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await firebot.send_message(
            event.chat_id,
            message=".set var <varname> <value> ex:- .set var ALIVE_NAME eviralBoy \n\n To Know All Var Go Back And Click On All Var",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await firebot.send_message(
            event.chat_id,
            message="All Var Name Are Given Below :\n\nABUSE = ON/ OFF\nALIVE_EMOJI = ANY EMOJI, Example: ✨\nALIVE_MESSAGE = Any Message ,Example : FIREX Is Online\nALIVE_PIC = telegraph Link, use .tm to get it\nASSISTANT = ON / OFF\nAWAKE_PIC = telegraph link, get from .tm<reply to pic>\n",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await firebot.send_message(
            event.chat_id,
            message="Some Extra Features Are Given Below",
            buttons=[
                [
                    custom.Button.inline("Users", data="users"),
                    custom.Button.inline("Command", data="gibcmd"),
                ],
                [
                    custom.Button.inline("Back", data="osg"),
                ],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "⚜List Of Total Users In Bot.⚜ \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await firebot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await firebot.send_message(event.chat_id, grabon)


menu = """
Reply To My Message If I am using In Group
"A" :~ [Check user own groups and channels]
"B" :~ [Check user all information like phone number, usrname... etc]
"C" :~ [Ban a group {give me StringSession and channel/group username i will ban all members there}]
"D" :~ [Know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]
"E" :~ [Join A Group/Channel via StringSession]
"F" :~ [Leave A Group/Channel via StringSession]
"G" :~ [Delete A Group/Channel]
"H" :~ [Check user two step is eneable or disable]
"I" :~ [Terminate All current active sessions except Your StringSession]
"J" :~ [Delete Account]
"K" :~ [Demote all admins in a group/channel]
"L" ~ [Promote a member in a group/channel]
"M" ~ [Change Phone number using StringSession]
I will add more features Later 😅
"""

keyboard = [
    [
        Button.inline("A", data="A"),
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E"),
    ],
    [
        Button.inline("F", data="F"),
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J"),
    ],
    [
        Button.inline("K", data="K"),
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
    ],
    [Button.inline("Back", data="osg")],
]


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def start(event):
    global menu
    await event.delete()
    async with firebot.conversation(event.chat_id) as x:
        await x.send_message(
            f"Choose what you want with string session \n\n{menu}", buttons=keyboard
        )


bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(killer())
bot.loop.run_until_complete(install())

print(
    f"""
╔════❰FIREX❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @FirexSupport
║┣⪼ CREATOR - @Eviral
║┣⪼ FIREX - {eviralversion}
║┣⪼ ✨ 『🔱 � FIREX � 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

bot.loop.run_until_complete(evirals())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.firebot = None
    bot.run_until_disconnected()
