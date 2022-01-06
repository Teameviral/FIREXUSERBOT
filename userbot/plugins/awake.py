import time

from telethon import version

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import StartTime, eviralversion
from userbot.cmdhelp import CmdHelp

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


eviral_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "eviral Choice eviralϐοτ"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@FirexSupport"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if eviral_IMG:
        eviral_caption = f"**{eviral_mention}**\n"

        eviral_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        eviral_caption += f"     ⚜ 𝓛𝓮𝓰𝓮𝓷𝓭𝓑𝓸𝓽 𝓘𝓼 𝓐𝔀𝓪𝓴𝓮 ⚜\n"
        eviral_caption += f"•🔥• FIRE-X     : ν3.0\n"
        eviral_caption += f"•🔥• 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽      : `{version.__version__}`\n"
        eviral_caption += f"•🔥• 𝚄𝙿𝚃𝙸𝙼𝙴         : `{uptime}`\n"
        eviral_caption += f"•🔥• 𝙲𝙷𝙰𝙽𝙽𝙴𝙻        : [𝕮нαииєℓ](t.me/Official_FIREX)\n"
        eviral_caption += f"•🔥• ᴹʸ 𝙶𝚁𝙾𝚄𝙿 : {CUSTOM_YOUR_GROUP}\n"

        await event.client.send_file(
            event.chat_id, eviral_IMG, caption=eviral_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 eviralϐοτ  : `{eviralversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [eviral](t.me/Eviral)\n",
        )


CmdHelp("awake").add_command("awake", None, "υѕє αи∂ ѕєє").add_info(
    "Same Like Alive"
).add_type("Official").add()
