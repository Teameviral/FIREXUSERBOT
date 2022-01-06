# credits to userge
# ported to FIREX by @Its_eviralBoy

import asyncio
import os
import random
import urllib

import nekos
import requests

from userbot import *
from userbot.Config import Config
from userbot.utils import *

neko_category = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "smug",
    "goose",
    "baka",
    "woof",
]


@bot.on(admin_cmd(pattern="nekos(?:\s|$)([\s\S]*)"))
async def _(event):
    x = await event.get_chat()
    y = x.id

    if y == 1496036895:
        return await eor(event, "Can't use this command here.")
    if Config.ABUSE != "ON":
        return await eor(
            event,
            "**This command is only for users with heroku variable** `ABUSE` **as** `ON`",
        )
    owo = event.text[7:]
    if owo in neko_category:
        king = await eor(event, f"`Searching {owo} ...`")
        link = nekos.img(owo)
        x = await event.client.send_file(event.chat_id, link, force_document=False)
        await king.delete()
        if link.endswith((".gif")):
            await unsave_gif(event, x)
    elif owo == "":
        king = await eor(event, "`Searching randoms...`")
        uwu = random.choice(neko_category)
        link = nekos.img(uwu)
        x = await event.client.send_file(event.chat_id, link, force_document=False)
        await king.delete()
        if link.endswith((".gif")):
            await unsave_gif(event, x)
    else:
        await eor(
            event,
            f"**Unmatched argument.** \n\n__Get all the required queries for nekos here__ -> **[Nekos Queries](http://telegra.ph/Nekos-Queries-08-20)**",
        )


@bot.on(admin_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Finding some big boobs for u 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending Some Bigs Boobs")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("butts$"))
@bot.on(sudo_cmd(pattern="butts$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Finding some beautiful butts for u🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some beautiful butts🤪")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


CmdHelp("adultzone").add_command("boobs", None, "Sends a random boobs pic").add_command(
    "butts", None, "Sends a random Butt pic"
).add_command("nekos", None, "18+ pic").add_info(
    "Use at Night Its Send U bad pic"
).add_warning(
    "18+"
).add_type(
    "Abuse"
).add()
