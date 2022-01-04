import json
import re

import requests

from . import *


async def callAPI(search_str):
    query = """
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        title {
          romaji
          english
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    """
    variables = {"search": search_str}
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.text


async def formatJSON(outData):
    msg = ""
    jsonData = json.loads(outData)
    res = list(jsonData.keys())
    if "errors" in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
    else:
        jsonData = jsonData["data"]["Media"]
        if "bannerImage" in jsonData.keys():
            msg += f"[〽️]({jsonData['bannerImage']})"
        else:
            msg += "〽️"
        title = jsonData["title"]["romaji"]
        link = f"https://anilist.co/anime/{jsonData['id']}"
        msg += f"[{title}]({link})"
        msg += f"\n\n**Type** : {jsonData['format']}"
        msg += f"\n**Genres** : "
        for g in jsonData["genres"]:
            msg += g + " "
        msg += f"\n**Status** : {jsonData['status']}"
        msg += f"\n**Episode** : {jsonData['episodes']}"
        msg += f"\n**Year** : {jsonData['startDate']['year']}"
        msg += f"\n**Score** : {jsonData['averageScore']}"
        msg += f"\n**Duration** : {jsonData['duration']} min\n\n"
        # https://t.me/FirexSupport/19496
        cat = f"{jsonData['description']}"
        msg += " __" + re.sub("<br>", "\n", cat) + "__"
        return msg


@bot.on(admin_cmd(pattern="anilist (.*)"))
@bot.on(sudo_cmd(pattern="anilist (.*)", allow_sudo=True))
async def anilist(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Searching...")
    result = await callAPI(input_str)
    msg = await formatJSON(result)
    await event.edit(msg, link_preview=True)


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(lege):
    eviral = lege.pattern_match.group(1)
    if not eviral:
        if lege.is_reply:
            (await lege_.get_reply_message()).message
        else:
            await eor(
                lege, "Sir please give some query to search and download it for you..!"
            )
            return

    troll = await bot.inline_query("AniFluidbot", f".anime {(deEmojify(eviral))}")

    await troll[0].click(
        lege_.chat_id,
        reply_to=lege_.reply_to_msg_id,
        silent=True if lege_.is_reply else False,
        hide_via=True,
    )
    await lege.delete()


@bot.on(admin_cmd(pattern="manga(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="manga(?: |$)(.*)", allow_sudo=True))
async def nope(lege_):
    eviral = lege_.pattern_match.group(1)
    if not eviral:
        if lege_.is_reply:
            (await lege_.get_reply_message()).message
        else:
            await eod(
                lege_, "Sir please give some query to search and download it for you..!"
            )
            return

    troll = await bot.inline_query("AniFluidbot", f".manga {(deEmojify(eviral))}")

    await troll[0].click(
        lege_.chat_id,
        reply_to=lege_.reply_to_msg_id,
        silent=True if lege_.is_reply else False,
        hide_via=True,
    )
    await lege_.delete()


@bot.on(admin_cmd(pattern="character(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="character(?: |$)(.*)", allow_sudo=True))
async def nope(lege_):
    eviral = lege_.pattern_match.group(1)
    if not eviral:
        if lege_.is_reply:
            (await lege_.get_reply_message()).message
        else:
            await eod(
                lege_, "Sir please give some query to search and download it for you..!"
            )
            return

    troll = await bot.inline_query("AniFluidbot", f".character {(deEmojify(eviral))}")

    await troll[0].click(
        lege_.chat_id,
        reply_to=lege_.reply_to_msg_id,
        silent=True if lege_.is_reply else False,
        hide_via=True,
    )
    await lege_.delete()


# eviral

CmdHelp("anime").add_command(
    "anime",
    "<anime name>",
    "Searches for the given anime and sends the details.",
    "anime violet evergarden",
).add_command(
    "manga",
    "<manga name>",
    "Searches for the given manga and sends the details.",
    "manga Jujutsu kaisen",
).add_command(
    "character",
    "<character name>",
    "Searches for the given anime character and sends the details.",
    "character Mai Sakurajima",
).add_command(
    "anilist",
    "<anime name>",
    "Searches Details of the anime directly from anilist",
    "anilist attack on titan",
).add_info(
    "Anime Search"
).add_warning(
    "✅ Harmless Module."
).add()
