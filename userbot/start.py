import os
from pathlib import Path

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputMessagesFilterDocument

from userbot import bot, eviralversion
from userbot.Config import Config
from userbot.utils import (
    load_abuse,
    load_addons,
    load_module,
    start_assistant,
    start_spam,
)

os.system("pip install telethon==1.24.0")
l2 = Config.SUDO_COMMAND_HAND_LER
eviral_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"
l1 = Config.COMMAND_HAND_LER

perf = "[ †hê FIRE-X ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

plc = os.environ.get("PLUGIN", None)


async def hekp():
    try:
        os.environ[
            "eviral_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By FIREX"
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                eviral_PIC,
                caption=f"Deployed FIRE-X Successfully\n\nFIRE-X ~ {eviralversion}\n\nType `{l1}help` or `{l1}ping` to check!\nFor Assistant Type `.on` \n\nJoin [FIREX Channel](t.me/Official_FIREX) for Updates & [FIREX Chat](t.me/FirexSupport) for any query regarding FIREX",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Official_FIREX"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@FirexSupport"))
    except BaseException:
        pass


async def module():
    import glob

    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


assistant = os.environ.get("ASSISTANT", None)


async def assistants():
    if assistant == "ON":
        import glob

        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))
    else:
        print("⚠️Assistant Not Loaded⚠️")


addon = os.environ.get("EXTRA_PLUGIN", None)


async def addons():
    if addon == "ON":
        import glob

        path = "userbot/plugins/Xtra_Plugin/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")


abuse = os.environ.get("ABUSE", None)


async def abuses():
    if abuse == "ON":
        import glob

        path = "userbot/plugins/Abuse/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_abuse(shortname.replace(".py", ""))
    else:
        print("⚠️Abuse Not Loading⚠️")


spam = os.environ.get("SPAM", None)


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


# Assistant


async def install():
    if plc == "ON":
        try:
            await bot(JoinChannelRequest("@FirexSupportPlugin"))
        except BaseException:
            pass
        i = 0
        chat = -1001518412326
        documentss = await bot.get_messages(
            chat, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        total_doxx = range(0, total)
        for ixo in total_doxx:
            mxo = documentss[ixo].id
            downloaded_file_name = await bot.download_media(
                await bot.get_messages(chat, ids=mxo), "userbot/plugins/"
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                print(f"{i} plugin install")
            else:
                print("Failed")
