import asyncio
import random

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"indslogan$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Speaking A Slogan")
    await asyncio.sleep(2)
    x = random.randrange(1, 25)
    if x == 1:
        await event.edit("Inqilab Zindabad \n\n **By : Bhagat Singh**")
    if x == 2:
        await event.edit(
            "DON'T TRY TO KNOW ABUOT ME I M eviral✌️ @Eviral\nfrom: @FirexSupport"
        )
    if x == 3:
        await event.edit("Subhash Chandra Bose : Dilli Chalo ")
    if x == 4:
        await event.edit("Mahatma Gamdhi : 'Do or die' (Karo Ya Maro)")
    if x == 5:
        await event.edit(
            "Chandra Shekhar Azad : Dushman ki goliyon ka hum samna karenge, Azad hee rahein hain, Azad hee rahenge "
        )
    if x == 6:
        await event.edit(
            "Bal Gandhar Tilak : Swaraj Mera Janamsiddh adhikar hai, aur main ise lekar rahunga"
        )
    if x == 7:
        await event.edit(
            "A.P.J Abdul Kalam : Don't take rest after your first victory because if you fail in second, more lips are waiting to say that your first victory was just luck "
        )
    if x == 8:
        await event.edit("Atal Bihari Bhajpai : Jai Jawan Jai kisan Jai Vigyan")
    if x == 9:
        await event.edit(
            "Subhash Chandra Bose : Tum Mujhe Khoon Do, main Tumhe Ajadi Doonga”. (Give me blood and I will give you freedom)"
        )
    if x == 10:
        await event.edit("Iqbal : Saare jahan se achchha hindustan hamara")
    if x == 11:
        await event.edit(
            "Ram Prasad Bismil : Sarfaroshi ki tamanna, ab hamare dil me hai"
        )
    if x == 12:
        await event.edit("Bal Gandhar Tilak : Swaraj (Self Rule) is my birthright")
    if x == 13:
        await event.edit("Rabindra Nath Tagore : Jan Gan Man Adhinayak Jaya hey")
    if x == 14:
        await event.edit(
            "Jawahar Lal Nehru : Aaram Haraam Hai (Cast off your laziness) "
        )


CmdHelp("ind slogan").add_command("indslogan", None, "slogan").add()
