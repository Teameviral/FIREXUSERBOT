from . import *


@bot.on(admin_cmd(pattern="gdmrng1(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good Morning")
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                await bot.send_message(
                    chat,
                    f"╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯.\n\n╱╱╱╱╱╱╱╱╱╱╭╮\n╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯",
                )
                done += 1
            except:
                lol += 1
    await event.reply(
        f"I hope your morning is as bright and gorgeous as your smile.[FIRE-X](https://t.me/Official_FIREX)"
    )


@bot.on(admin_cmd(pattern="gdmrng(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good Morning")
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                await bot.send_message(
                    chat,
                    f"G🌷o🍃o🌷D\nM🍃o🌷r🍃N🌷i🍃N🌷g\n\nNo matter how good or \nbad your life is,\nwake up each morning\nand be thankful.\nYou still have a new day.\n\n        🌞  \n \n         ╱◥████◣\n│田│▓ ∩│◥███◣\n╱◥◣ ◥████◣田∩田│\n│╱◥█◣║∩∩∩ 田∩田│\n║◥███◣∩田∩ 田∩田│\n│∩│ ▓ ║∩田│║▓田▓\n🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n",
                )
                done += 1
            except:
                lol += 1
    await event.reply(
        f"I hope your morning is as bright and gorgeous as your smile.[FIRE-X](https://t.me/Official_FIREX)"
    )


CmdHelp("gm").add_command(
    "gdmrng", None, "Wishs Good moning in all groups just one command"
).add_command("gdmrng1", None, "Wish Good Morning To All").add_info(
    "Good Morning Wish Command"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Addons"
).add()
