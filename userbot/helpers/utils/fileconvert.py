import logging
import os
import random

from moviepy.editor import VideoFileClip
from PIL import Image, ImageOps
from telethon import functions, types

from userbot.helpers.logger import logging

LOGS = logging.getLogger(__name__)
from userbot.helpers.runner import runcmd
from userbot.helpers.tools import media_type
from userbot.plugins.sql_helper.global_collectionjson import *
from userbot.utils import edit_or_reply


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        catevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        catevent = event
    catmedia = None
    catfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(catfile):
        os.remove(catfile)
    if mediatype == "Photo":
        catmedia = await reply.download_media(file="./temp")
        im = Image.open(catmedia)
        im.save(catfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, catfile, thumb=-1)
    elif mediatype == "Sticker":
        catmedia = await reply.download_media(file="./temp")
        if catmedia.endswith(".tgs"):
            catcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{catmedia}' '{catfile}'"
            stdout, stderr = (await runcmd(catcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif catmedia.endswith(".webp"):
            im = Image.open(catmedia)
            im.save(catfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, catfile, thumb=-1)
        if not os.path.exists(catfile):
            catmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(catfile, 0.1)
            except Exception:
                clip = clip.save_frame(catfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            catmedia = await reply.download_media(file="./temp")
            im = Image.open(catmedia)
            im.save(catfile)
    if catmedia and os.path.lexists(catmedia):
        os.remove(catmedia)
    if os.path.lexists(catfile):
        return catevent, catfile, mediatype
    return catevent, None


async def vid_to_gif(inputfile, outputfile, speed=None, starttime=None, endtime=None):
    try:
        clip = VideoFileClip(inputfile)
        if starttime is not None and endtime is not None:
            clip = clip.subclip(int(starttime), int(endtime))
        if speed is not None:
            clip = clip.speedx(float(speed))
        clip.write_gif(outputfile, logger=None)
        return outputfile
    except Exception as e:
        LOGS.error(e)
        return None


async def r_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((i, h))
        img2 = img2.resize((w - i, h))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        outframes.append(temp)
    return outframes


async def l_frames(image, w, h, outframes):
    for i in range(1, w, w // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = ImageOps.mirror(img1.resize((i, h)))
        img2 = ImageOps.mirror(img2.resize((w - i, h)))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (i, 0))
        temp = ImageOps.mirror(temp)
        outframes.append(temp)
    return outframes


async def ud_frames(image, w, h, outframes, flip=False):
    for i in range(1, h, h // 30):
        img1 = img2 = image.copy()
        temp = Image.new("RGB", (w, h))
        img1 = img1.resize((w, i))
        img2 = img2.resize((w, h - i))
        temp.paste(img1, (0, 0))
        temp.paste(img2, (0, i))
        if flip:
            temp = ImageOps.flip(temp)
        outframes.append(temp)
    return outframes


async def spin_frames(image, w, h, outframes):
    image.thumbnail((512, 512), Image.ANTIALIAS)
    img = Image.new("RGB", (512, 512), "black")
    img.paste(image, ((512 - w) // 2, (512 - h) // 2))
    image = img
    way = random.choice([1, -1])
    for i in range(1, 60):
        img = image.rotate(i * 6 * way)
        outframes.append(img)
    return outframes


async def invert_frames(image, w, h, outframes):
    image.convert("RGB")
    invert = ImageOps.invert(image)
    outframes.append(image)
    outframes.append(invert)
    return outframes


async def unsavegif(event, sandy):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=sandy.media.document.access_hash,
                    file_reference=sandy.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        LOGS.info(str(e))


def _sudousers_list():
    try:
        sudousers = get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]


async def edit_or_freply(
    event,
    text,
    parse_mode=None,
    link_preview=None,
    file_name=None,
    aslink=False,
    deflink=False,
    noformat=False,
    linktext=None,
    caption=None,
):  # sourcery no-metrics
    sudo_users = _sudousers_list()
    link_preview = link_preview or False
    reply_to = await event.get_reply_message()
    if len(text) < 4096 and not deflink:
        parse_mode = parse_mode or "md"
        if event.sender_id in sudo_users:
            if reply_to:
                return await reply_to.reply(
                    text, parse_mode=parse_mode, link_preview=link_preview
                )
            return await event.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    if not noformat:
        text = md_to_text(text)
    if aslink or deflink:
        linktext = linktext or "Message was to big so pasted to bin"
        response = await paste_message(text, pastetype="s")
        text = linktext + f" [here]({response})"
        if event.sender_id in sudo_users:
            if reply_to:
                return await reply_to.reply(text, link_preview=link_preview)
            return await event.reply(text, link_preview=link_preview)
        await event.edit(text, link_preview=link_preview)
        return event
    file_name = file_name or "output.txt"
    caption = caption or None
    with open(file_name, "w+") as output:
        output.write(text)
    if reply_to:
        await reply_to.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    if event.sender_id in sudo_users:
        await event.reply(caption, file=file_name)
        await event.delete()
        return os.remove(file_name)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)
