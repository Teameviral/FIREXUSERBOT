# FIREX Assistant
from telethon import Button, custom

from userbot import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


eviral_USER = bot.me.first_name
Its_eviralBoy = bot.uid

eviral_mention = f"[{eviral_USER}](tg://user?id={Its_eviralBoy})"
eviral_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
eviral_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
eviral_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
eviral_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
eviral_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
eviralversion = "𝚅2.1"

perf = "[ †hê FIRE-X ]"


DEVLIST = ["2082798662"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
