from os import remove

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, eor

from . import *


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@bot.on(
    admin_cmd(
        pattern="stopvc$",
        outgoing=True,
    )
)
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await eor(e, "`Voice Chat Stopped...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@bot.on(
    admin_cmd(
        pattern="playvc$",
    )
)
async def _(e):
    zz = await eor(e, "`VC bot started...`")
    er, out = await bash("python3 ./vcstarter.py & sleep 10 && npm start")
    LOGS.info(er)
    LOGS.info(out)
    if er:
        msg = f"Failed {er}\n\n{out}"
        if len(msg) > 4096:
            with open("vc-error.txt", "w") as f:
                f.write(msg.replace("`", ""))
            await e.reply(file="vc-error.txt")
            await zz.delete()
            remove("vc-error.txt")
            return
        await zz.edit(msg)


@bot.on(
    admin_cmd(
        pattern="vcinvite$",
        outgoing=True,
    )
)
async def _(e):
    ok = await eor(e, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


@bot.on(
    admin_cmd(
        pattern="startvc$",
        outgoing=True,
    )
)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await eor(e, "`Voice Chat Started...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@bot.on(
    admin_cmd(
        pattern="listvcaccess$",
    )
)
async def _(e):
    xx = await eor(e, "`Getting Voice Chat Bot Users List...`")
    mm = get_vcsudos()
    pp = f"**{len(mm)} Voice Chat Bot Approved Users**\n"
    if len(mm) > 0:
        for m in mm:
            try:
                name = (await e.client.get_entity(int(m))).first_name
                pp += f"• [{name}](tg://user?id={int(m)})\n"
            except ValueError:
                pp += f"• `{int(m)} » No Info`\n"
    await xx.edit(pp)


@bot.on(
    admin_cmd(
        pattern="rmvaccess ?(.*)",
    )
)
async def _(e):
    xx = await eor(e, "`Disapproving to access Voice Chat features...`")
    input = e.pattern_match.group(1)
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        name = (await e.client.get_entity(userid)).first_name
    elif input:
        try:
            userid = await get_user_id(input)
            name = (await e.client.get_entity(userid)).first_name
        except ValueError as ex:
            return await eod(xx, f"`{str(ex)}`", time=5)
    else:
        return await eod(xx, "`Reply to user's msg or add it's id/username...`", time=3)
    if not is_vcsudo(userid):
        return await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is not approved to use my Voice Chat Bot.`",
            time=5,
        )
    try:
        del_vcsudo(userid)
        await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is removed from Voice Chat Bot Users.`",
            time=5,
        )
    except Exception as ex:
        return await eod(xx, f"`{str(ex)}`", time=5)


@bot.on(
    admin_cmd(
        pattern="vcaccess ?(.*)",
    )
)
async def _(e):
    xx = await eor(e, "`Approving to access Voice Chat features...`")
    input = e.pattern_match.group(1)
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
        name = (await e.client.get_entity(userid)).first_name
    elif input:
        try:
            userid = await get_user_id(input)
            name = (await e.client.get_entity(userid)).first_name
        except ValueError as ex:
            return await eod(xx, f"`{str(ex)}`", time=5)
    else:
        return await eod(xx, "`Reply to user's msg or add it's id/username...`", time=3)
    if is_vcsudo(userid):
        return await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is already approved to use my Voice Chat Bot.`",
            time=5,
        )
    try:
        add_vcsudo(userid)
        await eod(
            xx,
            f"[{name}](tg://user?id={userid})` is added to Voice Chat Bot Users.`",
            time=5,
        )
    except Exception as ex:
        return await eod(xx, f"`{str(ex)}`", time=5)


CmdHelp("vcplayer").add_command(
    "vcaccess", None, "Reply to user and access vc"
).add_command("rmvaccess", None, "Reply to useer to denied to access vc").add_command(
    "stopvc", None, "To stop Vc"
).add_command(
    "startvc", None, "To start Vc"
).add_command(
    "listvcaccess", None, "List of vc access"
).add_command(
    "vcinvite", None, "Invite in vc"
).add()
