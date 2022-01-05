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

FONT_FILE_TO_USE = "./userbot/helpers/styles/Voice In My Head_080621160753.otf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/5692988b0d53ae24da716.jpg",
    "https://telegra.ph/file/5692988b0d53ae24da716.jpg",
    "https://telegra.ph/file/be0cc8912bece1b1e4783.jpg",
    "https://telegra.ph/file/09d8de43bca126d981dfa.jpg",
    "https://telegra.ph/file/e70f5639c500090f2789a.jpg",
    "https://telegra.ph/file/9e0f911538abd6f5fb54c.jpg",
    "https://telegra.ph/file/9e0f911538abd6f5fb54c.jpg",
]


@borg.on(admin_cmd(pattern="ldp ?(.*)"))
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


CmdHelp("eviraldp").add_command("ldp", None, "Starts autodp of eviralBoy").add()
