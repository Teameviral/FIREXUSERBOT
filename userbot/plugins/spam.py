# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.plugins.sql_helper.gvar_sql import *
from userbot.utils import admin_cmd, sudo_cmd

from . import eviral_mention

SUDO_WALA = Config.SUDO_USERS
lg_id = Config.LOGGER_ID


@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        await e.client.send_message(
            lg_id, f"#SPAM \n\nSpammed  `{counter}`  messages!!"
        )


@bot.on(admin_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(eviral):
    if not eviral.text[0].isalpha() and eviral.text[0] not in ("/", "#", "@", "!"):
        eviral_msg = eviral.text
        FIREX_count = int(eviral_msg[9:13])
        eviral_spam = str(eviral.text[13:])
        for i in range(1, FIREX_count):
            await eviral.respond(eviral_spam)
        await eviral.delete()
        if LOGGER:
            await eviral.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@bot.on(admin_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)


# @register(outgoing=True, pattern="^.mspam (.*)")
@bot.on(admin_cmd(pattern="mspam (.*)"))
@bot.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    if not sender.id == me.id and not SUDO_WALA:
        return await e.reply("`Sorry sudo users cant access this command..`")
    try:
        await e.delete()
    except:
        pass
    try:
        counter = int(e.pattern_match.group(1).split(" ", 1)[0])
        reply_message = await e.get_reply_message()
        if (
            not reply_message
            or not e.reply_to_msg_id
            or not reply_message.media
            or not reply_message.media
        ):
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        message = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, message)
    except:
        return await e.reply(
            f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )


@bot.on(admin_cmd("wspam (.*)"))
@bot.on(sudo_cmd(pattern="wspam (.*)", allow_sudo=True))
async def spam(event):
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    for word in message:
        await event.respond(word)
    if lg_id:
        if event.is_private:
            await event.client.send_message(
                lg_id,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                lg_id,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in {eviral_mention} chat with : `{message}`",
            )


@bot.on(admin_cmd("cspam (.*)"))
@bot.on(sudo_cmd(pattern="cspam (.*)", allow_sudo=True))
async def tmeme(event):
    "Spam the text letter by letter."
    cspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await event.delete()
    for letter in message:
        await event.respond(letter)
    if Config.LOGGER:
        if event.is_private:
            await event.client.send_message(
                lg_id,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with : `{message}`",
            )
        else:
            await event.client.send_message(
                lg_id,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in {get_display_name(await event.get_chat())}(`{event.chat_id}`) chat with : `{message}`",
            )


CmdHelp("spam").add_command(
    "spam", "<number> <text>", "Sends the text 'X' number of times.", ".spam 99 hello"
).add_command(
    "mspam",
    "<reply to media> <number>",
    "Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times",
    ".mspam 100 <reply to media>",
).add_command(
    "dspam",
    "<delay> <spam count> <text>",
    "Sends the text 'X' number of times in 'Y' seconds of delay",
    ".dspam 5 100 hello",
).add_command(
    "bigspam",
    "<count> <text>",
    "Sends the text 'X' number of times. This what FIREX iz known for. The Best BigSpam Ever",
    ".bigspam 5000 hello",
).add_command(
    "cspam",
    "<sentence>",
    "Spam the chat with every letter in given sentence as new message",
    ".cspam FIREX IS OP",
).add_command(
    "wspam",
    "<sentence>",
    "Spams the chat with every word in given sentence as new message",
    ".wspam FIREX IS OP",
).add()
