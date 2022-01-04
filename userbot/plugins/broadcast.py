from . import *


@bot.on(admin_cmd(pattern="gcast ?(.*)"))
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    event = await edit_or_reply(event, "__Globally Broadcasting Msg...__")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"Done in {done} chats, error in {er} chat(s)")


@bot.on(admin_cmd(pattern="gucast ?(.*)"))
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "`This Command Is Sudo Restricted.`")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"Done in {done} chats, error in {er} chat(s)")


CmdHelp("broadcast").add_command(
    "gcast", None, "Publish message to all channel and group"
).add_command(
    "gucast", None, "Same as Gcast But Its Send All The Member With In All Group"
).add_info(
    "Its Used To Send Messages To all Group"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Official"
).add()
