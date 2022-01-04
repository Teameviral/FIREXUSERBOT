import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

from . import *


@bot.on(admin_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But Boss! This is Not A Chat`")


@bot.on(admin_cmd(";__;$"))
# @register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@bot.on(admin_cmd("yo$"))
# @register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)


@bot.on(admin_cmd("oof$"))
# @register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@bot.on(admin_cmd("ccry$"))
# @register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@bot.on(admin_cmd("fp$"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@bot.on(admin_cmd("moon$"))
# @register(outgoing=True, pattern="^.mmoon$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd("source$"))
# @register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/Spandey112/SensibleUserbot")


@bot.on(admin_cmd("readme$"))
# @register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/Spandey112/SensibleUserbot/blob/master/README.md")


@bot.on(admin_cmd("heart$"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd("fap$"))
# @register(outgoing=True, pattern="^.fap$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="evil ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😒You Know I'm a good **PERSON**😏")
        await asyncio.sleep(1.9)
        await event.edit("BUT😡")
        await asyncio.sleep(1.2)
        await event.edit("😑Don't give me a reason😠")
        await asyncio.sleep(1.9)
        await event.edit("🤨To show my😎")
        await asyncio.sleep(1.4)
        await event.edit("**😈EVIL SIDE**😈")
        await asyncio.sleep(1.3)
        await event.edit(
            "**😈YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY EVIL SIDE😈**"
        )


CmdHelp("extra").add_command("leave", None, "Leave a Group").add_command(
    "__", None, "You Try It"
).add_command("cry", None, "Cry").add_command(
    "fp", None, "Sends palm face page"
).add_command(
    "evil", None, "Show Evil Side"
).add_command(
    "fap", None, "Faking Orgasm"
).add_command(
    "heart", None, "Try it u will grt emotion back"
).add_command(
    "readme", None, "Readme."
).add_command(
    "oof",
    None,
    "Use and See",
).add_command(
    "moon", None, "Face of Moon"
).add_command(
    "clock", None, "Use amd See"
).add()
