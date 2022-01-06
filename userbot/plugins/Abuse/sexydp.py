# Made By @Its_eviralBoy Keep Credits If You Are Goanna Kang This Lol

# And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

# Usage .actressdp Im Not Responsible For Any Ban caused By This
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
    "https://telegra.ph/file/2799c5767357cdaa074b9.jpg",
    "https://telegra.ph/file/06d96ec5711a9f77a73cc.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/109cffe40624fa5001d16.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/f9d79e6ad847203768de5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/2799c5767357cdaa074b9.jpg",
    "https://telegra.ph/file/06d96ec5711a9f77a73cc.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/109cffe40624fa5001d16.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/f9d79e6ad847203768de5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/2799c5767357cdaa074b9.jpg",
    "https://telegra.ph/file/06d96ec5711a9f77a73cc.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/109cffe40624fa5001d16.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/f9d79e6ad847203768de5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/2799c5767357cdaa074b9.jpg",
    "https://telegra.ph/file/06d96ec5711a9f77a73cc.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/c9bc336ce573ddb0be62c.jpg",
    "https://telegra.ph/file/109cffe40624fa5001d16.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/df603a49e4425aaf1632a.jpg",
    "https://telegra.ph/file/f9d79e6ad847203768de5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
    "https://telegra.ph/file/e27b7f46f2a7fde8e8fb5.jpg",
]


@borg.on(admin_cmd(pattern="sexydp ?(.*)"))
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


CmdHelp("sexydp").add_command(
    "sexydp", None, "Starts autodp of sexy pic & wait for 5 min"
).add()
