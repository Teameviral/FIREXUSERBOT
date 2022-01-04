# (c) @userbot
# Original written by @userbot edit by @I_m_Rock

import asyncio
from collections import deque

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

CmdHelp("earth").add_command("earth", None, "animation").add()


@borg.on(admin_cmd(pattern="earth"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
