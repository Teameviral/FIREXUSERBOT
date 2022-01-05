import os

import requests
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto

from FIREX.utils import admin_cmd, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp

pathdc = "./userbot/"
if not os.path.isdir(pathdc):
    os.makedirs(pathdc)


@bot.on(admin_cmd(pattern=r"trig"))
@bot.on(sudo_cmd(pattern=r"trig", allow_sudo=True))
async def dc(event):
    await event.edit("Making this image 😡triggered😈")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(hmm)
    open("eviral.gif", "wb").write(r.content)
    hehe = "eviral.gif"
    await bot.send_file(event.chat_id, hehe, caption="Got Triggered 😈😂", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"wst"))
@bot.on(sudo_cmd(pattern=r"wst", allow_sudo=True))
async def dc(event):
    await event.edit("What a waste 😒😒")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(hmm)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(event.chat_id, hehe, caption="Totally wasted⚰️ 😒", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"grey"))
@bot.on(sudo_cmd(pattern=r"grey", allow_sudo=True))
async def dc(event):
    await event.edit("Stealing Color from this 😜")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/greyscale?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Ur Black nd White img here 🙃", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


# eviral


@bot.on(admin_cmd(pattern=r"blur"))
@bot.on(sudo_cmd(pattern=r"blur", allow_sudo=True))
async def dc(event):
    await event.edit("Bluring Image🤓🤓")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blur?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(event.chat_id, hehe, caption="Blured 🤓", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"invert"))
@bot.on(sudo_cmd(pattern=r"invert", allow_sudo=True))
async def dc(event):
    await event.edit("Inverting Image🤔🤔")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invert?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Hmm 🤔 try to invert again", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"igrey"))
@bot.on(sudo_cmd(pattern=r"igery", allow_sudo=True))
async def dc(event):
    await event.edit("Don't know what i'm doing 😛😜")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(event.chat_id, hehe, reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()

    # eviral


@bot.on(admin_cmd(pattern=r"bright"))
@bot.on(sudo_cmd(pattern=r"bright", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Brightness 😎")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/brightness?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Brightness increased 😎😎", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()

    # eviral


@bot.on(admin_cmd(pattern=r"ytc"))
@bot.on(sudo_cmd(pattern=r"ytc", allow_sudo=True))
async def hehe(event):
    await event.edit("Lets make a utube comment 😁😁")
    givenvar = event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment = text.split(".")
    except:
        await event.edit("`.ytc username.comment reply  to image`")
    await event.delete()
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathd)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    nikal = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(nikal)
    open("eviral.png", "wb").write(r.content)
    chutiya = "eviral.png"
    await bot.send_file(event.chat_id, chutiya, reply_to=dc)
    for files in (chutiya, img):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()

    # eviral


@bot.on(admin_cmd(pattern=r"glass"))
@bot.on(sudo_cmd(pattern=r"glass", allow_sudo=True))
async def dc(event):
    await event.edit("Framing image under Glass 😁😁")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/glass?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Wow Image Trapped Under the glass 😂", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    # eviral


@bot.on(admin_cmd(pattern=r"blrpl"))
@bot.on(sudo_cmd(pattern=r"blrpl", allow_sudo=True))
async def dc(event):
    await event.edit("Bluring Image🤓🤓")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blurple?avatar={link}"
    r = requests.get(hehe)
    open("eviral.png", "wb").write(r.content)
    hehe = "eviral.png"
    await bot.send_file(event.chat_id, hehe, reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


CmdHelp("imgfun").add_command("trig", None, "🇮🇳🇮🇳🇮🇳").add_command(
    "wst", None, "Reply to image"
).add_command("grey", None, "Reply to image").add_command(
    "blur", None, "Reply To image"
).add_command(
    "glass", None, "Use and see"
).add_command(
    "ytc", None, "Use a d See"
).add_command(
    "invert", None, "Use and see"
).add_command(
    "bright", None, "Use And See"
).add_command(
    "blrpl", None, "Use And See"
).add()
