import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

eviral_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

eviralBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@firebot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ FIRE-X ⚜", "https://t.me/FirexSupport")]]
    await firebot.send_file(event.chat_id, eviral_IMG, caption=eviralBoy, buttons=GOOD)
