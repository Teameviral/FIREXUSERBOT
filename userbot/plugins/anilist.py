import json
import re

import requests

from FIREX.utils import *
from userbot import *
from userbot.cmdhelp import CmdHelp


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
        msg += f"\n\n**𝚃𝚢𝚙𝚎** : {jsonData['format']}"
        msg += f"\n**𝙶𝚎𝚗𝚛𝚎𝚜** : "
        for g in jsonData["genres"]:
            msg += g + " "
        msg += f"\n**𝚂𝚝𝚊𝚝𝚞𝚜** : {jsonData['status']}"
        msg += f"\n**𝙴𝚙𝚒𝚜𝚘𝚍𝚎** : {jsonData['episodes']}"
        msg += f"\n**𝚈𝚎𝚊𝚛** : {jsonData['startDate']['year']}"
        msg += f"\n**𝚂𝚌𝚘𝚛𝚎** : {jsonData['averageScore']}"
        msg += f"\n**𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗** : {jsonData['duration']} min\n\n"
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
    event = await edit_or_reply(event, "ѕєαяϲнιиg ϐяο")
    result = await callAPI(input_str)
    msg = await formatJSON(result)
    await event.edit(msg, link_preview=True)


CmdHelp("anilist").add_command(
    "anilist", "<anime name>", "Shows you the details of the anime"
).add_info(
    "Its Very Useful Module Its shows the profile and all the details of the characters of the animation"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Addons"
).add()
