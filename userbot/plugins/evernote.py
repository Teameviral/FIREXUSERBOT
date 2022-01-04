from telethon import events


@bot.on(events.NewMessage(pattern=r"^.note (.*)", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await event.edit("Added note to Evernote".format(uwu))
    await bot.send_message("@ifttt", "#note {}".format(uwu))


from userbot.cmdhelp import CmdHelp

CmdHelp("note").add_command("note", None, "Here u can save note").add()
