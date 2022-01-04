# Plugin by @Rishisuperyo
# Animation by kiddo
# kang =gey ,keep credits = cool coder 😶
# usage .gim
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"gim", outgoing=True))
async def hapy(event):

    a = "🎱➖✊➖➖✊➖🎱\n🌟        \         /          🌟\n⭐          \😁/            ⭐\n✨           🎽             ✨\n              /    \ \n            👟    👟"
    await event.edit(a)


from userbot.cmdhelp import CmdHelp

CmdHelp("gim").add_command("gim", None, "Get info about a File Extension").add()
