# --------------------------------------------------------------------------------------------------------------------------------

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from FIREX.utils import admin_cmd, edit_or_reply, eor, sudo_cmd
from userbot.cmdhelp import CmdHelp


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@bot.on(admin_cmd(pattern="inviteall ?(.*)"))
@bot.on(sudo_cmd(pattern="inviteall ?(.*)", allow_sudo=True))
async def get_users(event):
    legen_ = event.text[11:]
    eviral_chat = legen_.lower
    restricted = ["@FirexSupport", "@Official_FIREX"]
    eviral = await eor(event, f"**Inviting members from** {legen_}")
    if eviral_chat in restricted:
        await event.edit("You can't Invite Members from there.")
        await bot.send_message(-1001344140905, "Sorry for inviting members from here.")
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        eviral = await edit_or_reply(event, "`processing...`")
    else:
        eviral = await edit_or_reply(event, "`processing...`")
    eviral = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await eviral.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await eviral.edit(
        "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/FirexSupport)**\n\n`🔸Inviting Users.......`"
    )
    async for user in event.client.iter_participants(eviral.full_chat.id):
        try:
            await bot(InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await eviral.edit(
                f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await eviral.edit(
        f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/FirexSupport) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
    )


@bot.on(admin_cmd(pattern="invitesall ?(.*)"))
@bot.on(sudo_cmd(pattern="invitesall ?(.*)", allow_sudo=True))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        eviral = await edit_or_reply(event, "`processing...`")
    else:
        eviral = await edit_or_reply(event, "`processing...`")
    aura = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await eviral.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await eviral.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(aura.full_chat.id):
        try:
            if error.startswith("Too"):
                return await eviral.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await eviral.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await eviral.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )


@bot.on(admin_cmd(pattern="add ?(.*)"))
@bot.on(sudo_cmd(pattern="add ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "addsudo" in event.raw_text.lower() or "addblacklist" in event.raw_text.lower():
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(event, "`.add` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Added user to the chat....")


CmdHelp("invite").add_command(
    "add", "<username/id>", "Adds the given user to the group"
).add_command(
    "inviteall",
    "<group username>",
    "Scraps user from the targeted group to your group. Basically Kidnapps user from one chat to another",
).add_command(
    "invitesall", "<group username>", "Kidnap Members. From Group"
).add()
