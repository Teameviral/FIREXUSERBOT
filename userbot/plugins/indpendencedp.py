import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/2f2035b4e8ab1dc6efc3d.jpg",
    "https://telegra.ph/file/a2b6e3781680a6d85f842.jpg",
    "https://telegra.ph/file/18e4d7c45e49ad9340e3c.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/3072bb5fd2c8dd8e9da60.jpg",
    "https://telegra.ph/file/24f84ab213b177ef43d6e.jpg",
    "https://telegra.ph/file/6e372beae3cda13117ec7.jpg",
    "https://telegra.ph/file/70e671947a35f8b8a5d0e.jpg",
    "https://telegra.ph/file/628fafe3fea4371e30e3c.jpg",
    "https://telegra.ph/file/f94c8aa7c8425e4b4346c.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
    "https://telegra.ph/file/c7b64ed41f6113f00415e.jpg",
    "https://telegra.ph/file/c7b64ed41f6113f00415e.jpg",
    "https://telegra.ph/file/c7b64ed41f6113f00415e.jpg",
]


@borg.on(admin_cmd(pattern="inddp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return


CmdHelp("independp").add_command(
    "inddp", None, "Starts autopic of Independence & now wait for 5 min"
).add()
