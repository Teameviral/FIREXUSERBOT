import asyncio
import random
from collections import deque

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import *
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

from . import *

# --Constants--#
sed1 = "https://telegra.ph/file/9102e0041cf2bacffc4a8.mp4"
sed2 = "https://telegra.ph/file/2034b44685abbc5d8db4d.mp4"
sed3 = "https://telegra.ph/file/c7f8f00729fc4147ad8d6.mp4"
sed4 = "https://telegra.ph/file/f5c968e0dd5bf01748678.mp4"
sed5 = "https://telegra.ph/file/026f3b4776af1f3277614.mp4"
sed6 = "https://telegra.ph/file/3593c809b7dcc17090b6c.mp4"
sed = "https://telegra.ph/file/f29468b5fba0ad146bae2.mp4"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "set ur alive name"
remd = bot.me.id
cap = f"Yeah My Friend This Suprise is for you\nThanks for Being my Friend, I am Blessed With a friend like you✨\n                           ~[{DEFAULTUSER}](tg://user?id={remd})"
# --over--#


@borg.on(admin_cmd(pattern=r"friend$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "Hii..!\nI found My Friend In that Account And this is for him\nAnd i feel like wishing him on this awesome day."
    )
    await asyncio.sleep(10)
    s = random.randrange(1, 20)
    if s == 1:
        await event.edit(
            "With your presence in my life, my life has illuminated with new hope. You are a wonderful soul who has taught me the real meaning of friendship. \nWishing you a warm Happy Best Friend Day."
        )
    if s == 2:
        await event.edit(
            "When we met first you were sweet, gradually you became sweeter and now you are the sweetest person I know. You are my best friend for life. \nHappy Best Friend Day."
        )
    if s == 3:
        await event.edit(
            "Time and distance are important in every relationship. But with a friend like you, who lives in my heart, we will never be separated by distance because we are connected at heart. \nHappy Best Friend Day."
        )
    if s == 4:
        await event.edit(
            "When you have someone whom you can call any day, any time…. you know you are blessed. \nHappy Best Friend Day."
        )
    if s == 5:
        await event.edit(
            "You are someone I can count on in every step of my life. May our beautiful friendship lasts forever! \nHappy Best Friend Day."
        )
    if s == 6:
        await event.edit(
            "Thank you for never letting me do the stupid things alone. This just proves what a great friend you are to me. \nHappy Best Friend Day."
        )
    if s == 7:
        await event.edit(
            "Not many things in life make me happy. But you are an exception. \nHappy Best Friend Day."
        )
    if s == 8:
        await event.edit(
            "I am one of those lucky individuals who have gotten to experience the meaning of true friendship. \nHappy Best Friend Day."
        )
    if s == 9:
        await event.edit(
            "Some people are so special in our lives that it’s hard to imagine existing in a universe without them.\nHappy Best Friend Day."
        )
    if s == 10:
        await event.edit(
            "Thank you for being my bundle of joy. Thank you for being supportive and kind and for believing in me when no one else did.\nHappy Best Friend Day."
        )
    if s == 11:
        await event.edit(
            "Don’t make friends who are comfortable to be with. Make friends who will force you to lever yourself up.\nHappy FriendShip Day. "
        )
    if s == 12:
        await event.edit(
            "The most beautiful discovery true friends make is that they can grow separately without growing apart.\nHappy FriendShip Day. "
        )
    if s == 13:
        await event.edit(
            "Life is partly what we make it, and partly what it is made by the friends we choose.\nHappy FriendShip Day. "
        )
    if s == 14:
        await event.edit(
            "A real friend is one who walks in when the rest of the world walks out.\nHappy FriendShip Day. "
        )
    if s == 15:
        await event.edit(
            "A friend is someone who understands your past, believes in your future, and accepts you just the way you are.\nHappy FriendShip Day. "
        )
    if s == 16:
        await event.edit(
            "Lots of people want to ride with you in the limo, but what you want is someone who will take the bus with you when the limo breaks down.\nHappy FriendShip Day. "
        )
    if s == 17:
        await event.edit(
            "To the world, you may be just one person, but to one person you may be the world.\nHappy FriendShip Day. "
        )
    if s == 18:
        await event.edit(
            "A friend is one who overlooks your broken fence and admires the flowers in your garden.\nHappy FriendShip Day. "
        )
    if s == 19:
        await event.edit(
            "There’s not a word yet for old friends who’ve just met.\nHappy FriendShip Day. "
        )
    if s == 20:
        await event.edit(
            "A friend who understands your tears is much more valuable than a lot of friends who only know your smile.\nHappy FriendShip Day. "
        )
        await asyncio.sleep(5)
    await bot.send_message(
        event.chat_id, "Please Stay Awake For a While one more Parcel Coming"
    )
    await asyncio.sleep(10)
    f = random.randrange(1, 7)

    if f == 1:
        await bot.send_file(event.chat_id, file=sed1, caption=cap, link_preview=False)
    if f == 2:
        await bot.send_file(event.chat_id, file=sed2, caption=cap, link_preview=False)
    if f == 3:
        await bot.send_file(event.chat_id, file=sed3, caption=cap, link_preview=False)
    if f == 4:
        await bot.send_file(event.chat_id, file=sed4, caption=cap, link_preview=False)
    if f == 5:
        await bot.send_file(event.chat_id, file=sed5, caption=cap, link_preview=False)
    if f == 6:
        await bot.send_file(event.chat_id, file=sed6, caption=cap, link_preview=False)
    if f == 7:
        await bot.send_file(event.chat_id, file=sed, caption=cap, link_preview=False)


@bot.on(admin_cmd(pattern=f"bigoof$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


@bot.on(admin_cmd(pattern="birthday$", outgoing=True))
@bot.on(sudo_cmd(pattern="birthday$", allow_sudo=True))
async def gn(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "╔╗╔╦══╦═╦═╦╗╔╗\n║╚╝║══║═║═║╚╝║\n║╔╗║╔╗║╔╣╔╩╗╔╝\n╚╝╚╩╝╚╩╝╚╝• B-day •"
    )


@bot.on(admin_cmd(pattern=f"^Uff$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "U",
        "Uf",
        "Uff",
        "Ufffff",
        "Uffffff",
        "Ufffffff",
        "Uffffffff",
        "Ufffffffff",
        "Uffffffffff",
        "Ufffffffffff",
        "Uffffffffffff",
        "Ufffffffffffff",
        "Uffffffffffffff",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=f"kf$", outgoing=True))
async def _(event):
    r = random.randint(0, 3)
    logger.debug(r)
    if r == 0:
        await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    else:
        r == 1
        await event.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")


@bot.on(admin_cmd(pattern=f"animate$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"animate$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(11)
    await edit_or_reply(event, "animate")
    animation_chars = [
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 192])


@borg.on(admin_cmd(pattern=r"^Tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤨🤔🧐🤨"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=r"^Lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"chutiye$"))
@bot.on(sudo_cmd(pattern=f"chutiye$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 4
    animation_ttl = range(0, 82)
    event = await edit_or_reply(event, "ThInKiNg...")
    animation_chars = [
        "Maderchod- MOTHERFUCKER",
        "Bhosadike-BORN FROM A ROTTEN PUSSY",
        "Bhen chod-Sister fucker",
        "Bhadhava- Pimp",
        "Bhadhava- Pimp",
        "Chodu- Fucker",
        "Chutiya- Fucker, bastard",
        "Gaand- ASS",
        "Gaandu-Asshole",
        "Gadha Bakland- Idiot",
        "Lauda Lund- Penis, dick, cock",
        "Hijra- Gay, Transsexual",
        "Kuttiya- Bitch",
        "Paad- FART",
        "Randi- HOOKER",
        "Saala kutta- Bloody dog",
        "Saali kutti- Bloody bitch",
        "Tatti- Shit",
        "Kamina- bastard",
        "Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
        "Chut ke dhakkan- Pussy lid",
        "Chut ke gulam- Pussy whipped",
        "Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
        "Choot marani ka- Pussy whipped",
        "Choot ka baal- Hair of vagina",
        "Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
        "Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
        "Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
        "Chipkali ke chut ke pasine- Sweat of reptiles cunt",
        "Chipkali ki bhigi chut- Wet pussy of a wall lizard",
        "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
        "Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
        "Cuntmama- Vaginal uncle",
        "Chhed- Vagina,Hole",
        "Apni gaand mein muthi daal- Put your fist up your ass",
        "Apni lund choos- Go and suck your own dick",
        "Apni ma ko ja choos- Go suck your mom",
        "Bhen ke laude- Sister’s dick",
        "Bhen ke takke: Go and suck your sister’s balls",
        "Abla naari tera buble bhaari-  woman, your tits are huge",
        "Bhonsri-Waalaa- You fucker",
        "Bhadwe ka awlat- Son of a pimp",
        "Bhains ki aulad- Son of a buffalo",
        "Buddha Khoosat- Old fart",
        "Bol teri gand kaise maru- let me know how to fuck you in the ass",
        "Bur ki chatani- Ketchup of cunt",
        "Chunni- Clit",
        "Chinaal- Whore",
        "Chudai khana- Whore house",
        "Chudan chuda- Fucking games",
        "Chut ka pujari- pussy worshipper",
        "Chut ka bhoot- Vaginal Ghost",
        "Gaand ka makhan- Butter from the ass",
        "Gaand main lassan- Garlic in ass",
        "Gaand main danda- Stick in ass",
        "Gaand main keera- Bug up your ass",
        "Gaand mein bambu- A bambooup your ass",
        "Gaandfat- Busted ass",
        "Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
        "Hazaar lund teri gaand main-Thousand dicks in your ass",
        "Jhat ke baal- Pubic hair",
        "Jhaant ke pissu- Bug of pubic hair",
        "Kadak Mall- Sexy Girl",
        "Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
        "Khotey ki aulda- Son of donkey",
        "Kutte ka awlat- Son of a dog",
        "Kutte ki jat- Breed of dog",
        "Kutte ke tatte- Dog’s balls",
        "Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
        "Lavde ke bal- Hair on your penis",
        "muh mei lele: Suck my dick",
        "Lund Chus: Suck dick",
        "Lund Ke Pasine- Sweat of dick",
        "Meri Gand Ka Khatmal: Bug of my Ass",
        "Moot, Mootna- Piss off",
        "Najayaz paidaish- Illegitimately born",
        "Randi khana- whore house",
        "Sadi hui gaand- Stinking ass",
        "Teri gaand main kute ka lund- A dog’s dick in your ass",
        "Teri maa ka bhosda- Your mother’s breasts",
        "Teri maa ki chut- Your mother’s pussy",
        "Tere gaand mein keede paday- May worms infest your ass-hole",
        "Ullu ke pathe- Idiot",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 82])


@borg.on(admin_cmd(pattern=f"sadmin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 13)
    await event.edit("sadmin")
    animation_chars = [
        "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",
        "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",
        "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",
        "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",
        "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",
        "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",
        "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",
        "@aaaaaaddddddmmmmmmiiiiiinnnnnn",
        "@aaaaadddddmmmmmiiiiinnnnn",
        "@aaaaddddmmmmiiiinnnn",
        "@aaadddmmmiiinnn",
        "@aaddmmiinn",
        "@admin",
    ]

    for i in animation_ttl:
        await asyncio.sleep(1)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=r"happy?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"happy?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`I am so Happy.....`")
    deq = deque(list("😇✨🍫✨😇✨🍫✨🦋✨😊"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"smile$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"smile$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "smile")
    animation_chars = [
        "🙂",
        "🙃",
        "☺️",
        "😊",
        "😏",
        "😌",
        "🙃",
        "🙂",
        "☺️",
        "🍫",
        "😄",
        "😇",
        "You are special for me..",
        "You are so cute 😍",
        "You are special for me.." "You are so cute 😍",
        "🙂",
        "🙃",
        "☺️",
        "😊",
        "😏",
        "😌",
        "🙃",
        "🙂",
        "☺️",
        "🍫",
        "😄",
        "😇",
        "Now Smile!!😇😇 ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


CmdHelp("animations6").add_command("bigoof", None, "🇮🇳🇮🇳🇮🇳").add_command(
    "happy", None, "Use and see"
).add_command("smile", None, "Use and see").add_command(
    "animate", None, "Use a d See"
).add_command(
    "muth", None, "Use And See"
).add_command(
    "birthday", None, "Use And See"
).add_command(
    "Lol", None, "Use and See Without Dot"
).add_command(
    "Tlol", None, "Use and See But this command Without Dot"
).add_command(
    "chutiye", None, "Animation Abuse"
).add_command(
    "sadmin", None, "Its Shout Admin"
).add_command(
    "friend", None, "Use and See"
).add_info(
    "Its all Animation Use As Anywhere"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Addons"
).add()

# FIREX
