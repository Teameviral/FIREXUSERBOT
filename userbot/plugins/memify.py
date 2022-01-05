import asyncio
import os

import cv2
from PIL import Image

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.helpers.convert import deEmojify

from . import *

path = "./eviralmify/"
if not os.path.isdir(path):
    os.makedirs(path)

from userbot.Config import Config
from userbot.helpers.mmf import *

lg_id = os.environ.get("LOGGER_ID", None)


@bot.on(admin_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def _(event):
    _reply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (_reply and (_reply.media)):
        legen_ = await eod(event, "`Can't memify this 🥴`")
        return
    eviral = await _reply.download_media()
    if eviral.endswith((".tgs")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        cmd = ["lottie_convert.py", eviral, "pic.png"]
        file = "pic.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif eviral.endswith((".webp", ".png")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        pic = Image.open(eviral)
        pic.save("pic.png", format="PNG", optimize=True)
        file = "pic.png"
    else:
        await eor(event, "**Memifying 🌚🌝**")
        img = cv2.VideoCapture(eviral)
        tal, semx = img.read()
        cv2.imwrite("pic.png", semx)
        file = "pic.png"
    output = await draw_meme(file, msg)
    await bot.send_file(
        event.chat_id, output, force_document=False, reply_to=event.reply_to_msg_id
    )
    await legen_.delete()
    try:
        os.remove(eviral)
        os.remove(file)
    except BaseException:
        pass
    os.remove(pic)


@bot.on(admin_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(event):
    eviral = event.pattern_match.group(1)
    if not eviral:
        if event.is_reply:
            (await event.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(event, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(event, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(eviral))}")
    if troll:
        await event.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                event.chat_id,
                legen_,
                caption="",
            )
        await legen_.delete()
    else:
        await eod(event, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="gg(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gg(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    eviral = kraken.pattern_match.group(1)
    if not eviral:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Googlax need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(eviral))}")
    if troll:
        await kraken.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                kraken.chat_id,
                legen_,
                caption="",
            )
        await kraken.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="honk(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="honk(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    eviral = kraken.pattern_match.group(1)
    if not eviral:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Honka need some text to make sticker.")

    troll = await bot.inline_query("honka_says_bot", f"{(deEmojify(eviral))}.")
    if troll:
        await kraken.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                kraken.chat_id,
                legen_,
                caption="",
            )
        await legen_.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="gogl(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gogl(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    hell = kraken.pattern_match.group(1)
    if not hell:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Need some text...")

    troll = await bot.inline_query("stickerizerbot", f"#12{(deEmojify(hell))}")
    if troll:
        await kraken.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                kraken.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


client = borg


@bot.on(admin_cmd(pattern="memify ?(.*)"))
@bot.on(sudo_cmd(pattern="memify ?(.*)", allow_sudo=True))
async def _(event):
    _reply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (_reply and (_reply.media)):
        legen_ = await eod(event, "`Can't memify this 🥴`")
        return
    eviral = await _reply.download_media()
    if eviral.endswith((".tgs")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        cmd = ["lottie_convert.py", eviral, "pic.png"]
        file = "pic.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif eviral.endswith((".webp", ".png")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        pics = Image.open(eviral)
        pics.save("pic.png", format="PNG", optimize=True)
        file = "pic.png"
    else:
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        img = cv2.VideoCapture(eviral)
        tal, semx = img.read()
        cv2.imwrite("pic.png", semx)
        file = "pic.png"
    output = await drawText(file, msg)
    await bot.send_file(
        event.chat_id, output, force_document=False, reply_to=event.reply_to_msg_id
    )
    await legen_.delete()
    try:
        os.remove(eviral)
        os.remove(file)
        os.remove(output)
    except BaseException:
        pass


@bot.on(admin_cmd(pattern="mmf ?(.*)"))
@bot.on(sudo_cmd(pattern="mmf ?(.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "You might want to try `.help memify`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "```Reply to a image/sticker.```")
        return
    file = await client.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    await edit_or_reply(event, "```Memifying this image! (」ﾟﾛﾟ)｣ ```")
    text = str(event.pattern_match.group(1)).strip()
    if len(text) < 1:
        return await edit_or_reply(event, "You might want to try `.help memify`")
    meme = await draw_to_Text(file, text)
    await client.send_file(event.chat_id, file=meme, force_document=False)
    os.remove(meme)


CmdHelp("memify").add_command(
    "mmf",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in sticker format.",
    "mmf <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "memify",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in sticker format.",
    "mmf <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "mms",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in image format.",
    "mms <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "doge", "<text>", "Makes A Sticker of Doge with given text.", "doge Hello"
).add_command(
    "gogl", "<text>", "Makes Sticker"
).add_command(
    "gg", "<text>", "Makes google search sticker.", "gg Hello"
).add_command(
    "honk", "<text>", "Makes a sticker with honka revealing given text.", "honk Hello"
).add_info(
    "Make Memes on telegram 😉"
).add_warning(
    "✅ Harmless Module."
).add_type(
    "Addons"
).add()
