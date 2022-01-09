import asyncio
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from userbot import bot
from userbot.plugins.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from userbot.plugins.sql_helper.botusers import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)


@firebot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    codetechbot = await firebot.get_me()
    bot_id = codetechbot.first_name
    codetechbot.username
    codetechbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Assistant Bot. \n\nMy [➤ Master](tg://user?id={bot.uid}) \nI Can Deliver Message To My Master Using This Bot. \n\nIf You Want Your Own Assistant You Can Deploy From Button Below. \n\nPowered By [『FIRE-X』](https://t.me/Official_FIREX)"
    if event.sender_id == bot.uid:
        await firebot.send_message(
            vent,
            message=f"Hi Sir/Miss, It's Me {bot_id}, Your Assistant ! \nHow Can I help U?",
            buttons=[
                [
                    Button.url(
                        "Add Me to Group 👥", "t.me/{bot_username}?startgroup=true"
                    )
                ],
                [
                    Button.url(" Support ", "https://t.me/FirexSupport"),
                    Button.url(" Updates ", "https://t.me/FIREXUB"),
                ],
                [custom.Button.inline("Settings", data="osg")],
                [custom.Button.inline("Hack", data="hack")],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await firebot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [
                    custom.Button.inline(" Rules ", data="rules"),
                    custom.Button.inline(" Close ", data="close"),
                ],
                [custom.Button.inline("Contact", data="contact_")],
                [custom.Button.inline("Deploy Your Fire-X", data="deploy")],
            ],
        )


# Data's


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await firebot.send_message(
            event.chat_id,
            message="You Can Deploy Fire-X In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
            link_preview=False,
            buttons=[
                [custom.Button.inline("Deploy your Fire-X", data="fire")],
                [Button.url("Help Me ❓", "https://t.me/firexSupport")],
                [Button.url("Github Repo ❓", "github.com/TeamEviral/FIREXUSERBOT")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fire")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await firebot.send_message(
            event.chat_id,
            message="🔰 https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeameviral%2FFIREXUSERBOT&template=https%3A%2F%2Fgithub.com%2FTeamEviral%2FFIREX",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await firebot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )


@firebot.on(events.callbackquery.CallbackQuery(data=re.compile(b"contact_")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await event.answer("This Is Not For U My Master", cache_time=0, alert=True)
    else:
        await firebot.send_message(
            event.chat_id,
            message="🔰 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ �",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )


# Bot Permit.
@firebot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        add_me_in_db(sed.id, event.sender_id, event.id)


@firebot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == bot.uid:
        if event.raw_text.startswith("/"):
            pass
        else:
            await firebot.send_message(user_id, msg_s)


# broadcast
@firebot.on(
    events.NewMessage(
        pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    )
)
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await firebot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await firebot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@firebot.on(
    events.NewMessage(pattern="^/stats ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(starkisnoob)}"
    )


@firebot.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /hack- hack anyone through string session \n➤ \eval - run an assync code \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@firebot.on(
    events.NewMessage(pattern="^/block ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await firebot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@firebot.on(
    events.NewMessage(pattern="^/unblock ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await firebot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
