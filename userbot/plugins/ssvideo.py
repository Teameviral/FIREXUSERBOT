import asyncio
import os
import time

from telethon.tl.types import DocumentAttributeFilename

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

from . import *


@bot.on(admin_cmd(outgoing=True, pattern=r"^\.ssvideo(?: |$)(.*)"))
async def ssvideo(event):

    if not event.reply_to_msg_id:

        return await event.edit("`reply to video!`")

    reply_message = await event.get_reply_message()

    if not reply_message.media:

        return await event.edit("`reply to a video!`")

    try:

        frame = int(event.pattern_match.group(1))

        if frame > 10:

            return await event.edit("`hey..dont put that much`")

    except BaseException:

        return await event.edit("`Please input number of frame!`")

    if (
        reply_message.photo
        or (
            DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
            in reply_message.media.document.attributes
        )
        or (
            DocumentAttributeFilename(file_name="sticker.webp")
            in reply_message.media.document.attributes
        )
    ):

        return await event.edit("`Unsupported files!`")

    c_time = time.time()

    await event.edit("`Downloading media...`")

    ss = await bot.download_media(
        reply_message,
        "anu.mp4",
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[DOWNLOAD]")
        ),
    )

    try:

        await event.edit("`Proccessing...`")

        command = f"vcsi -g {frame}x{frame} {ss} -o ss.png "

        os.system(command)

        await event.client.send_file(
            event.chat_id,
            "ss.png",
            reply_to=event.reply_to_msg_id,
        )

        await event.delete()

    except BaseException as e:

        await event.edit(f"{e}")

    os.system("rm -rf *.png *.mp4")


CmdHelp("ssvideo").add_command("ssvideo", None, "Use and See").add()
