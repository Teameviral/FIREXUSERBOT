from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(eviral):
    eviral = eviral.pattern_match.group(1)
    if not eviral:
        if eviral.is_reply:
            (await eviral.get_reply_message()).message
        else:
            await edit_or_reply(
                eviral,
                "`Sir please give some query to search and download it for you..!`",
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(eviral))}")

    await troll[0].click(
        eviral.chat_id,
        reply_to=eviral.reply_to_msg_id,
        silent=True if eviral.is_reply else False,
        hide_via=True,
    )
    await eviral.delete()


CmdHelp("memevoice").add_command(
    "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
