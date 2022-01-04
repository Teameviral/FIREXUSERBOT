import asyncio

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import *

CmdHelp("fullpromo").add_command(
    "fullpromote", None, "to give full promote to anyone with all rights"
).add()


@borg.on(admin_cmd(pattern="fullpromote ?(.*)"))
async def prmte(event):
    xx = await eor(event)
    await event.get_chat()
    user, rank = await get_user_info(ult)
    if not rank:
        rank = "ℓεɠεɳ∂"
    if not user:
        return await xx.edit("Reply to a user to promote him with all rights!")
    try:
        await event.client(
            EditAdminRequest(
                event.chat_id,
                user.id,
                ChatAdminRights(
                    add_admins=True,
                    invite_users=True,
                    change_info=True,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True,
                    manage_call=True,
                ),
                rank,
            ),
        )
        await xx.edit(
            f"{inline_mention(user)} is now an admin with full rights in {event.chat.title} with title {rank}.",
        )
    except BadRequestError:
        return await xx.edit("I don't have the right to promote you.")
    await asyncio.sleep(5)
    await xx.delete()
