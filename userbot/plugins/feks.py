import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from FIREX.utils import admin_cmd
from userbot.cmdhelp import CmdHelp


@borg.on(admin_cmd(pattern="ftyping ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd(pattern="fcontact ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "contact"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd(pattern="fgame ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "game"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd(pattern="flocation ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "location"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd(pattern="fvoice ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "recording"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd(pattern="fvideo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "uploading"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(600)  # type for 10 seconds


@borg.on(admin_cmd("fgben"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "__Reason: Madarchod Saala"
    await event.edit("** Nikal Lawde❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 2082798662:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 99$ to my master__ [Eviral](https://t.me/Eviral) __to release your account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                "**Person's Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Not Given `"
        await event.reply(mention)
    await event.delete()


@bot.on(admin_cmd(pattern="fgban ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Preparing to gban this nub nibba....")
        await asyncio.sleep(2)
        await event.edit("Gbanning user.....")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 1 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 5 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 10 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 15 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 20 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 25 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 30 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 35 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 40 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 45 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 50 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 55 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 60 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 65 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 70 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 75 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 80 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 85 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 90 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 95 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 100 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 105 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 110 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 115 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 120 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 125 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 130 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 135 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 140 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 145 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 150 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 155 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 160 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 165 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 170 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 175 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 180 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 185 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 190 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 200 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 204 chats")
        await asyncio.sleep(1.5)
        await event.edit(
            "Gbanned this nub nibba successfully in😏: 204 chats.\nBlocked and added to gban watch!"
        )


@bot.on(admin_cmd(pattern="fungban ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "Preparing to Ungban this nub nibba please weit for a while....."
        )
        await asyncio.sleep(2)
        await event.edit("UnGbanning user.....")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 1 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 5 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 10 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 15 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 20 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 25 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 30 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 35 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 40 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 45 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 50 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 55 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 60 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 65 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 70 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 75 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 80 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 85 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 90 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 95 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 100 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 105 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 110 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 115 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 120 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 125 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 130 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 135 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 140 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 145 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 150 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 155 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 160 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 165 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 170 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 175 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 180 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 185 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 190 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 200 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 204 chats")
        await asyncio.sleep(1.5)
        await event.edit(
            "UnGbanned this nub nibba successfully in 204 chats.\nUnBlocked and removed from gban watch"
        )


@borg.on(admin_cmd("fmute"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "**Warning!! User Gmuted By Admin...\n**"
    no_reason = "__Reason: ab sale Globally mute hi rah"
    await event.edit("** Gmutting...**")
    asyncio.sleep(2)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 2082798662:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to Mute my master nigger!**\n\n__Your account has been hacked! Pay 99$ to my master__ [Eviral](https://t.me/Eviral) __to release your account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` Gmutted By Admin...\n\n`"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't have a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "**Warning!! User Gmutted By Admin...\nReason: Not Given **"
        await event.reply(mention)
    await event.delete()


@borg.on(admin_cmd("funmute"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "**Warning!! User Unmuted By Admin...\n**"
    no_reason = "__Reason: Purani bat Bhool ja wo pakar ke jhool jha"
    await event.edit("**Ungmutting...**")
    asyncio.sleep(2)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 2082798662:
            await reply_message.reply(
                "Wait a second. Maine Gmute kab kiya Owner ko toh main unmute karu!!!"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` Ungmutted By Admin...\n\n`"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't have a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "**Warning!! User Gmutted By Admin...\nReason: Not Given **"
        await event.reply(mention)
    await event.delete()


from userbot.cmdhelp import CmdHelp

CmdHelp("feks").add_command(
    "gbun", None, "A kind of fake gban try it yourself"
).add_command("fgben", None, "A kind of fake fedgban try it yourself").add_command(
    "funben", None, "A kind of fake ungban try it yourself"
).add_command(
    "fgmute", None, "A kind of fake gmute try it yourself"
).add_command(
    "fungmute", None, "A kind of fake ungmute try it yourself"
).add_command(
    "ftyping",
    None,
    "A kind of fake typing try it yourself Like this u can Use f-typing,contact,game,location,voice,round,video,photo,document,cancel",
).add_command(
    "fcontact", None, "A kind of fake contact try it yourself"
).add()
