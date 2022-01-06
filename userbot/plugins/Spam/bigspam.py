from userbot import bot

from . import *


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


import asyncio

from telethon import events, functions, types


@firebot.on(
    events.NewMessage(pattern="/bigspam", func=lambda e: e.sender_id == bot.uid)
)
async def spam(e):
    if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
        return await e.reply(usage, parse_mode=None, link_preview=None)
    eviral = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    smex = await e.get_reply_message()
    if len(eviral) == 2:
        message = str(eviral[1])
        counter = int(eviral[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "typing"):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)

    elif e.reply_to_msg_id and smex.media:

        counter = int(eviral[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "document"):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
            await asyncio.sleep(0.1)
    elif e.reply_to_msg_id and smex.text:
        message = smex.text
        counter = int(eviral[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "typing"):
                await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.1)
    else:

        await e.reply(usage, parse_mode=None, link_preview=None)
