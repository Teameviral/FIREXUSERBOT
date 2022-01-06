import asyncio

from . import *


@bot.on(admin_cmd(pattern="yaadash"))
async def _(event):
    await event.edit("***falled while walking***")
    await asyncio.sleep(3)
    await event.edit("***2 Hours Later***")
    await asyncio.sleep(6)
    await event.edit("who i am here ?")
    await asyncio.sleep(1)
    await event.edit("Where I Am?")
    await asyncio.sleep(1)
    await event.edit("What I Am Using?")
    await asyncio.sleep(1)
    await event.edit("What Is Phone?")
    await asyncio.sleep(1)
    await event.edit("What Is Telegram?")
    await asyncio.sleep(1)
    await event.edit("Why Life Exists?")
    await asyncio.sleep(1)
    await event.edit("What is Language?")
    await asyncio.sleep(1)
    await event.edit("Does Reborn Take Place?")
    await asyncio.sleep(1)
    await event.edit("What Is Thinking?")
    await asyncio.sleep(1)
    await event.edit("Does Superman Exists")
    await asyncio.sleep(3)
    await event.edit("Oof I Guess I Should Die")


CmdHelp("yadash").add_command("yaadash", None, "Use and see").add_info(
    "Its Very funny module u can use it to prank your frieds"
).add_warning("Harmless Module✅").add_type("Addons").add()
