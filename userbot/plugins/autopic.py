import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

COLLECTION_STRING = [
    "indian-actress-wallpapers",
    "latest-bollywood-actress-wallpapers-2018-hd",
    "bollywood-actress-wallpaper",
    "hd-wallpapers-of-bollywood-actress",
    "new-bollywood-actress-wallpaper-2018",
]


async def actresspp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="actressdps ?(.*)"))
async def main(event):

    await event.edit("**Starting Actress Profile Pic...\n\nDone !!! Check Your DP **")

    while True:

        await actresspp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

COLLECTION_STRING = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
]


async def avengersdps():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="avengersdps ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Avengers Profile Pic...\n\nDone !!! Check Your DP By @FirexSupport**"
    )

    while True:

        await avengerspp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRINGZ = ["hacker-background"]


async def hackpp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="hackers ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Hacker Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs

    while True:

        await hackpp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRING = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
    "Marvel-Shield-iPhone-Wallpaper",
    "Shield-Logo-Wallpaper",
    "Marvel-Shield-Logo-Wallpaper",
    "Agents-of-Shield-Wallpaper",
    "Agents-of-Shield-iPhone-Wallpaper",
    "Agents-of-Shield-Wallpapers-HD" "Thor-Wallpaper-1920x1080",
    "Thor-Wallpapers",
    "Avengers-HD-Wallpapers-1080p",
    "Avengers-Wallpaper-for-Desktop",
    "Avengers-4K-Wallpaper",
    "Avengers-Age-of-Ultron-Wallpaper",
    "Avengers-Civil-War-Wallpaper",
    "Avengers-2-Wallpapers",
    "Avengers-Logo-Wallpaper",
    "Marvel-Avengers-Desktop-Wallpaper",
    "4K-Deadpool-Wallpaper",
    "3D-Deadpool-Logo-Wallpaper",
    "Deadpool-HD-Desktop-Wallpaper",
    "Cool-Deadpool-Wallpaper",
    "Thor-Wallpaper-HD",
]


async def marveldps():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="marveldps ?(.*)"))
async def main(event):

    await event.edit("**Starting Marvel Profile Pic's...\n\nDone !!! Check Your DP.**")

    while True:

        await marvelpp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRING = ["Predator-Wallpapers-Backgrounds", "Alien-vs-Predator-Wallpaper"]


async def predatordps():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="predatordps ?(.*)"))
async def main(event):
    await event.edit("**Starting predator Profile Pic.**")  # Owner @NihiNivi
    while True:
        await ppp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

# Space lovers
COLLECTION_STRINGS = [
    "1920x1080-space-wallpapers",
    "4k-space-wallpaper",
    "cool-space-wallpapers-hd",
]


async def spacedps():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGS) - 1)

    pack = COLLECTION_STRINGS[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "friday.jpg")


@bot.on(admin_cmd(pattern="spacedps ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Space Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs

    while True:

        await spacepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from FIREX.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
    "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
    "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
    "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
    "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
    "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
    "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
    "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
    "https://telegra.ph/file/1ec37d367bb59ac56131d.jpg",
    "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
    "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
    "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
    "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg",
]


@bot.on(admin_cmd(pattern="survivorpfps ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "@Sur_vivor \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(400)
        except:
            return


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRINGZ = [
    "Vietnam-War-Wallpapers",
    "War-of-the-Worlds-Wallpaper",
    "War-Plane-Wallpaper",
    "World-War-Ii-Wallpaper",
    "Cool-War-Wallpapers",
    "World-War-2-Wallpaper-HD",
]


async def actiondps():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="actiondps ?(.*)"))
async def main(event):

    await event.edit(
        "**Uplaoding Walpapers \n please wait...\n\nDone !!! Check Your DP"
    )

    while True:

        await actionpp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRING = [
    "pokemon-serena-wallpaper",
    "hd-pokemon-iphone-wallpapers",
    "pokemon-wallpaper-pikachu",
    "doraemon-3d-wallpaper-2018",
    "pokemon-serena-wallpaper",
    "anime-girls-wallpapers",
]


async def animedps():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="animedps ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Anime Profile Pic...\n\nDone !!! Check Your DP..by DARK COBRA😎🤟🏻**"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(400)


import asyncio
import os
import random
import re
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from FIREX.utils import admin_cmd

COLLECTION_STRING = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]


async def gamerpfps():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="gamerpfps ?(.*)"))
async def main(event):
    await event.edit("**Starting Gamer Profile Pic.**")  # Owner @NihiNivi
    while True:
        await gamepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(400)


CmdHelp("autopic").add_command(
    "auto_pics", None, "Change ur profile pic automatically"
).add_command("avengersdps", None, "Change ur profile pic automatically").add_command(
    "actressdps", None, "Change ur profile pic automatically"
).add_command(
    "hackers", None, "Change ur profile pic automatically"
).add_command(
    "marveldps", None, "Change ur profile pic automatically"
).add_command(
    "predatordps", None, "Change ur profile pic automatically"
).add_command(
    "spacedp", None, "Change ur profile pic automatically"
).add_command(
    "psurvivorpfs", None, "Change ur profile pic automatically"
).add_command(
    ".actiondps", None, "Change ur profile pic automatically"
).add_command(
    "animedps", None, "Change ur profile pic automatically"
).add_command(
    "gamerpfps", None, "Change ur profile pic automatically"
).add()
