from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.plugins import *


@borg.on(admin_cmd(pattern="hpic?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Lolis{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @LoliHeavenBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hfutanari?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Futanari{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hshota?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Shota{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hvideo?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Hentai Videos")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hoppai?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Oppai")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="htrap?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Trap")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hbdsm?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "BDSM")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hfurry?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Furry")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hgif?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "GIF Hentai")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


@borg.on(admin_cmd(pattern="hcosplay?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Cosplay")
            response = await response
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)


CmdHelp("hentai").add_command(
    "hpic", None, "Uses of this cmnd you get anime porn image"
).add_command("hfutanari", None, "Use And see").add_command(
    "hshota", None, "Use And see"
).add_command(
    "hoppai", None, "Use And see"
).add_command(
    "htrap", None, "Use And see"
).add_command(
    "hbdsm", None, "Use And see"
).add_command(
    "hfurry", None, "Use And see"
).add_command(
    "hgif", None, "Use And see"
).add_command(
    "hcosplay", None, "Use And see"
).add_command(
    "hvideo", None, "Use And see"
).add_warning(
    "Harm⚠️"
).add_info(
    "+18 contant"
).add_type(
    "Abuse"
).add()
