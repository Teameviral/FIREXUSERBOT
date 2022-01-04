from userbot import CmdHelp
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"hi ?(.*)"))  # initially made by @NOOB_GUY_OP
async def hhi(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🌺"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\n☁☁☁☁☁☁☁☁"
    )


# later made by me
@borg.on(admin_cmd(pattern=r"gws ?(.*)"))
async def gws(event):
    giveVar = event.text
    """m = giveVar[5:-1]
    if not m:"""
    m = " Get Well Soon ! "
    a = giveVar[-1:]
    if a == "s":
        a = "🌹"
    elif not a:
        a = "🌹"
    await event.edit(f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m} {a}\n{a}{a}{a}{a}{a}{a}{a}")


@borg.on(admin_cmd(pattern=r"his ?(.*)"))
async def hii(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🌺"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{b}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}"
    )


@borg.on(admin_cmd(pattern=r"hola ?(.*)"))
async def hlo(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "🌺"
    b = giveVar[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}"
    )


@borg.on(admin_cmd(pattern=r"byes ?(.*)"))
async def bye(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "✨"
    b = giveVar[7:8]
    if not b:
        b = "🌺"
    await event.edit(
        f"╭━━┳╮╱╱╭┳━━━╮\n┃╭╮┃╰╮╭╯┃╭━━╯\n┃╰╯╰╮ {a}╭┫╰━━╮\n┃╭{b}╮┣╮╭╯┃╭━━╯\n┃╰{b}╯┃┃┃╱┃╰━━╮\n╰━━━╯╰╯╱╰━━━╯\n                              FIRE-X"
    )


CmdHelp("emotes").add_command("hi <emoji>", None, "Try it yourself").add_command(
    "gws <emoji>", None, "Try it yourself"
).add_command("hlo1 <emoji>", None, "Try it yourself").add_command(
    "his <emoji>", None, "Try it yourself"
).add_command(
    "bye <emoji>", None, "Try it yourself"
).add()
