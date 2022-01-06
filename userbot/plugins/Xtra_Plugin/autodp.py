import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from userbot.utils import admin_cmd

COLLECTION_STRING1 = [
    "awesome-batman-wallpapers",
    "batman-arkham-knight-4k-wallpaper",
    "batman-hd-wallpapers-1080p",
    "the-joker-hd-wallpaper",
    "dark-knight-joker-wallpaper",
]
COLLECTION_STRING2 = [
    "thor-wallpapers",
    "thor-wallpaper",
    "thor-iphone-wallpaper",
    "thor-wallpaper-hd",
]
COLLECTION_STRING3 = [
    "indian-actress-wallpapers",
    "latest-bollywood-actress-wallpapers-2018-hd",
    "bollywood-actress-wallpaper",
    "hd-wallpapers-of-bollywood-actress",
    "new-bollywood-actress-wallpaper-2018",
]
COLLECTION_STRING4 = [
    "pokemon-serena-wallpaper",
    "anime-girls-wallpapers",
    "sexy-anime-gilr-wallpaper",
    "cute-anime-girl-3d-wallpaper-2018",
    "ash-serena-love-wallpaper",
    "anime-girls-wallpapers",
]
COLLECTION_STRING5 = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
]
COLLECTION_STRING6 = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]
COLLECTION_STRING7 = ["hacker-background"]
COLLECTION_STRING8 = [
    "1920x1080-space-wallpapers",
    "4k-space-wallpaper",
    "cool-space-wallpapers-hd",
]
COLLECTION_STRING9 = [
    "Epic-Space-Wallpaper",
    "Acoustic-Guitar-Wallpaper-HD",
    "Taylor-Guitar-Wallpaper",
    "Classical-Music-Wallpapers-for-Desktop",
    "Prs-Guitar-Wallpaper",
    "Iron-Man-Wallpaper-1920x1080",
    "Dodge-Challenger-Black-Hellcat-Wallpaper",
    "V-for-Vendetta-Mask-Wallpaper",
    "Toxic-Mask-Wallpapers",
    "Minion-Desktop-Wallpaper",
    "Epic-1080p-Wallpapers",
    "Japanese-Desktop-Wallpaper",
    "Cool-Gold-Cars-Wallpapers",
    "Pretty-Wallpapers-for-iPhone-Quotes",
    "dark-abstract-wallpaper",
    "abstract-dark-wallpaper",
    "abstract-wallpapers-and-screensavers",
    "roaring-lion-wallpaper",
    "wolves-screensavers-and-wallpaper",
    "cool-wallpaper-for-men",
    "Epic-1080p-Wallpapers",
    "hacker-background",
    "Vietnam-War-Wallpapers",
    "War-of-the-Worlds-Wallpaper",
    "War-Plane-Wallpaper",
    "World-War-Ii-Wallpaper",
    "Cool-War-Wallpapers",
    "World-War-2-Wallpaper-HD",
]


async def animeppbat():
    rnd = random.randint(0, len(COLLECTION_STRING1) - 1)
    pack = COLLECTION_STRING1[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppthor():
    rnd = random.randint(0, len(COLLECTION_STRING2) - 1)
    pack = COLLECTION_STRING2[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppactress():
    rnd = random.randint(0, len(COLLECTION_STRING3) - 1)
    pack = COLLECTION_STRING3[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animepppoke():
    rnd = random.randint(0, len(COLLECTION_STRING4) - 1)
    pack = COLLECTION_STRING4[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppaven():
    rnd = random.randint(0, len(COLLECTION_STRING5) - 1)
    pack = COLLECTION_STRING5[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppgame():
    rnd = random.randint(0, len(COLLECTION_STRING6) - 1)
    pack = COLLECTION_STRING6[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animepphack():
    rnd = random.randint(0, len(COLLECTION_STRING7) - 1)
    pack = COLLECTION_STRING7[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppspace():
    rnd = random.randint(0, len(COLLECTION_STRING8) - 1)
    pack = COLLECTION_STRING8[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


async def animeppwall():
    rnd = random.randint(0, len(COLLECTION_STRING9) - 1)
    pack = COLLECTION_STRING9[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="batmandp$"))
async def main(event):
    await event.edit("Actibated Batman Dp\nEnjoy 💜")
    while True:
        await animeppbat()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs


@bot.on(admin_cmd(pattern="thordp$"))
async def main(event):
    await event.edit("Activated Thor Dp\nEnjoy 💜")
    while True:
        await animeppthor()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs


@bot.on(admin_cmd(pattern="actressdp$"))
async def main(event):
    await event.edit("Activated Actress Dp\nEnjoy 💜")
    while True:
        await animeppactress()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="animedp$"))
async def main(event):
    await event.edit("Activated Anime Dp\nEnjoy 💜")
    while True:
        await animepppoke()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="avengersdp$"))
async def main(event):
    await event.edit("Activated Avengers Dp\nEnjoy 💜")
    while True:
        await animeppaven()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="gamerdp$"))
async def main(event):
    await event.edit("Activated Gamers Dp\nEnjoy 💜")
    while True:
        await animeppgame()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="hackerdp$"))
async def main(event):
    await event.edit("Activated Hackers Dp\nEnjoy 💜")
    while True:
        await animepphack()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="spacedp$"))
async def main(event):
    await event.edit("Activated Space Dp\nEnjoy 💜")
    while True:
        await animeppspace()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)


@bot.on(admin_cmd(pattern="wallpapers$"))
async def main(event):
    await event.edit("Activated Wallappers on your DP\nEnjoy 💜")
    while True:
        await animeppwall()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)
