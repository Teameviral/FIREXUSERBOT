from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from FIREX.utils import admin_cmd, sudo_cmd
from userbot import CMD_LIST, bot
from userbot.Config import Config

from . import *

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

msg = f"""
**⚜  FIRE_X ⚜**

  •        [♥️ 𝚁𝚎𝚙𝚘 ♥️](https://github.com/Teameviral/FIREX)
  •        [♦️ Deploy ♦️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeameviral%2FFIREX&template=https%3A%2F%2Fgithub.com%2FTeameviral%2FFIREX)

  •  ©️ {eviral_channel} ™
"""


@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        eviral = await bot.inline_query(botname, "repo")
        await eviral[0].click(event.chat_id)
        if event.sender_id == Eviral:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    firebotusername = botname
    chat = "@Botfather"
    if firebotusername is not None:
        try:
            results = await event.client.inline_query(firebotusername, "FIREX_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            eviral = await eor(
                event,
                "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(firebotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await eviral.edit("Unblock @Botfather first.")
                await eviral.edit(
                    f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}op` again to get the help menu."
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await eor(
            event,
            "**⚠️ 𝙴𝚁𝚁𝙾𝚁 !!** \n𝙿𝚕𝚎𝚊𝚜𝚎 𝚁𝚎-𝙲𝚑𝚎𝚌𝚔 BOT_TOKEN & BOT_USERNAME on Heroku.",
        )


@bot.on(admin_cmd(pattern="op ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    firebotusername = botname
    input_str = event.pattern_match.group(1)
    if firebotusername is not None or eviral_input == "text":
        results = await event.client.inline_query(firebotusername, "FIREX_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**Check Bot Token And Bot Username In Reveal Var*")

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")


@bot.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def FIREXt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**⚠️ 𝙴𝚛𝚛𝚘𝚛 !** \n𝙽𝚎𝚎𝚍 𝚊 Plugin 𝚗𝚊𝚖𝚎 𝚝𝚘 𝚜𝚑𝚘𝚠 𝚙𝚕𝚞𝚐𝚒𝚗 𝚒𝚗𝚏𝚘")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`♦️`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(
            event,
            "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string,
        )


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("тєℓєтнση  вαѕє∂ υѕєявσт ρσωєяє∂ ву **FIRE-X** вσт")
