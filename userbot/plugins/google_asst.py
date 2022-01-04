import asyncio
import datetime
import os
import subprocess

import emoji
from googletrans import Translator
from gtts import gTTS

from . import *


@bot.on(admin_cmd(pattern="trp ?(.*)"))
@bot.on(sudo_cmd(pattern="trp ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "-" in input_str:
        lan, text = input_str.split("-")
    else:
        await eod(
            event,
            f"`trt LanguageCode - message`  or  `trt LanguageCode as reply to a message.`\n\nTry `trc` to get all language codes",
            7,
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        output_str = """**Translated**\nFrom {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_or_reply(event, str(exc))


@bot.on(admin_cmd(pattern=r"trs", outgoing=True))
@bot.on(sudo_cmd(pattern=r"trs", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        "**All The Language Codes Can Be Found** \n ⚡ [Here](https://telegra.ph/file/d2d666595b61c676169c1.jpg) ⚡",
        link_preview=False,
    )


@bot.on(admin_cmd(pattern="voices (.*)"))
@bot.on(sudo_cmd(pattern="voices (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "-" in input_str:
        lan, text = input_str.split("-")
    else:
        await eod(event, "Invalid Syntax. Module stopping.")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            required_file_name + ".opus",
        ]
        try:
            t_response = subprocess.check_output(
                command_to_execute, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await event.edit(str(exc))
            # continue sending required_file_name
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.datetime.now()
        ms = (end - start).seconds
        await borg.send_file(
            event.chat_id,
            required_file_name,
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True,
        )
        os.remove(required_file_name)
        await eor(event, "Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms))
        await asyncio.sleep(5)
        await event.delete()
    except Exception as e:
        await eod(event, str(e), 10)


CmdHelp("ggℓ αѕѕτ").add_command(
    "voices",
    "<reply to a msg> <lang code>",
    "Sends the replied msg content in audio format.",
).add_command(
    "trs",
    "<lang code> <reply to msg>",
    "Translates the replied message to desired language code. Type '.trc' to get all the language codes",
    f"trt en - hello | .trt en <reply to msg>",
).add_command(
    "trp", None, "Gets all the possible language codes for google translate module"
).add_info(
    "Google Assistant"
).add_warning(
    "✅ Harmless Module."
).add()
