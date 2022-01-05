import os
import time

import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from userbot.helpers import *

from . import *

try:

    from youtubesearchpython import *

except:
    os.system("pip install pip install youtube-search-python")

from FIREX.utils import admin_cmd, edit_or_reply, progress, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify
from userbot.utils import edit_or_reply


@bot.on(admin_cmd(pattern="lyrics(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lyrics(?: |$)(.*)", allow_sudo=True))
async def nope(aura):
    eviral = aura.pattern_match.group(1)
    if not eviral:
        if aura.is_reply:
            (await aura.get_reply_message()).message
        else:
            await aura.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(eviral))}")

    await troll[0].click(
        aura.chat_id,
        reply_to=aura.reply_to_msg_id,
        silent=True if aura.is_reply else False,
        hide_via=True,
    )

    await aura.delete()


# >>>>>>>>>>>>>>>>>>✓✓✓✓✓<<<<<<<<<<<<<<<<<<<


@bot.on(admin_cmd(pattern="gaana ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gaana ?(.*)", allow_sudo=True))
async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit(
                "```Please unblock``` @FindmusicpleaseBot``` and try again```"
            )

            return

        await gaana.edit("`Sending Your Music...wait!!! 😉😎`")

        await bot.send_file(gaana.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()


# -------------------------------------------------------------------------------


@bot.on(admin_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    query = event.text[6:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb{Eviral}.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Song**")
        with YoutubeDL(song_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    except Exception as e:
        return await eor(hell, f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    await event.edit(
        f"**🎶 Preparing to upload song 🎶 :** \n\n{hell_data['title']} \n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {eviral_mention}",
        thumb=thumb_name,
        attributes=[
            DocumentAttributeAudio(
                duration=int(hell_data["duration"]),
                title=str(hell_data["title"]),
                performer=perf,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp3")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp3")


@bot.on(admin_cmd(pattern="vsong ?(.*)"))
@bot.on(sudo_cmd(pattern="vsong ?(.*)", allow_sudo=True))
async def _(event):
    query = event.text[7:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb{Eviral}.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Video**")
        with YoutubeDL(video_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    except Exception as e:
        return await eor(hell, f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    await event.edit(
        f"**📺 Preparing to upload video 📺 :** \n\n{hell_data['title']}\n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp4",
        supports_streaming=True,
        caption=f"**✘ Video :** `{title}` \n\n**✘ By :** {eviral_mention}",
        thumb=thumb_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp4")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp4")


# -------------------------------------------------------------------------------
import os

from telethon.tl.functions.channels import JoinChannelRequest

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@bot.on(admin_cmd(pattern="getsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="getsong(?: |$)(.*)", allow_sudo=True))
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/anitimeofficial"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await edit_or_reply(so, "🔹Ok wait... 📡Searching your song🔸")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await edit_or_reply(so, "📥Downloading...Please wait🤙")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(
                so, "Please unblock @SongsForYouBot and try searching again🤐"
            )
            return
        await edit_or_reply(so, "Ohh.. I got something!! Wait sending😋🤙")
        await asyncio.sleep(3)
        await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await so.delete()


# -------------------------------------------------------------------------------

import asyncio
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@bot.on(admin_cmd(pattern="dwlsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="dwlsong(?: |$)(.*)", allow_sudo=True))
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await edit_or_reply(
            Deezlod, "` I need a link to download something pro.`**(._.)**"
        )
    else:
        await edit_or_reply(Deezlod, "**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(
                Deezlod, "**Error:** `unblock` @DeezLoadBot `and retry!`"
            )
            return
        await bot.send_file(Deezlod.chat_id, song, caption=details.text)
        await Deezlod.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )
        await Deezlod.delete()


# -------------------------------------------------------------------------------


from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest


@bot.on(admin_cmd(pattern="sdd ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="sdd?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezLoadBot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            try:
                await borg(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            await borg.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await borg.send_file(
                event.chat_id,
                songh,
                caption="🔆**Here's the requested song!**🔆\n`Check out` [FIREX](https://t.me/eviralSupport)",
            )
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
CmdHelp("songs").add_command(
    "song",
    "<song name>",
    "Searches the song from youtube and upload in current chat in audio(.mp3) format. •Highest Quality",
).add_command(
    "vsong",
    "<song name>",
    "Searches the song from youtube and upload in current chat in video(.mp4) format. •Highest Quality",
).add_command(
    "getsong",
    "<song name>",
    "Searches song from a local tg bot @Songsforyoubot and sends the music in current chat",
).add_command(
    "gaana",
    "<song name>",
    "Searches song from a local tg bot @FindmusicpleaseBot and sends the music in current chat",
).add_command(
    "sdd", "<song link>", "Downloads the song from given link"
).add_command(
    "dwlsong", "<song link>", "Same as .sdd but downloads from spotify and deezer"
).add_command(
    "lyrics", "<song name>", "Sends the lyrics of given song."
).add()
