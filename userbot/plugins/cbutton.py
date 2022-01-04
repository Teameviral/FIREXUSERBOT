import os
import re

from telethon import custom

from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.utils import admin_cmd

BOT_USERNAME = Config.BOT_USERNAME
# regex obtained from: https://github.com/PaulSonOfLars/firebot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(r"(\{([^\[]+?)\}\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@borg.on(admin_cmd(pattern="cbutton"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "**What text should I use in button post?**")
    prev = 0
    note_data = ""
    buttons = []
    for match in BTN_URL_REGEX.finditer(markdown_note):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1
        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            # create a thruple with button label, url, and newline status
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)
        # if odd, escaped -> move along
        elif n_escapes % 2 == 1:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
        else:
            break
    else:
        note_data += markdown_note[prev:]
    message_text = note_data.strip() or None
    tl_ib_buttons = build_keyboard(buttons)
    firebot_reply_message = None
    if reply_message and reply_message.media:
        firebot_reply_message = await event.client.download_media(reply_message.media)
    if tl_ib_buttons == []:
        tl_ib_buttons = None
    await firebot.send_message(
        entity=event.chat_id,
        message=message_text,
        parse_mode="html",
        file=firebot_reply_message,
        link_preview=False,
        buttons=tl_ib_buttons,
    )
    await event.delete()
    if firebot_reply_message:
        os.remove(firebot_reply_message)


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(custom.Button.url(btn[0], btn[1]))
        else:
            keyb.append([custom.Button.url(btn[0], btn[1])])
    return keyb


CmdHelp("cbutton").add_command(
    "cbutton",
    None,
    "Use And See",
    "cbutton Test [Google]<buttonurl:https://www.google.com> [Support]<buttonurl:https://t.me/FirexSupport:same> [Channel]<buttonurl:https://t.me/Its_FIREX>",
).add_info("Use to Create Button").add_warning("Harmless Module✅").add_type(
    "Official"
).add()
