import asyncio
import random

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"rfilmy$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("producing a filmy dialougue.......")
    await asyncio.sleep(2)
    x = random.randrange(1, 25)
    if x == 1:
        await event.edit(
            "Aaj mere paas gaadi hai, bungla hai, paisa hai... tumhare paas kya hai?\n\nMere paas, mere paas... Maa hai... \n\n **From : Deewar**"
        )
    if x == 2:
        await event.edit(
            "DON'T TRY TO KNOW ABUOT ME I M eviral✌️ @Eviral\nfrom: @FirexSupport"
        )
    if x == 3:
        await event.edit(
            "Amitabh Bachchan: 'Rishte mein to hum tumhare baap lagte hain,\n naam hai Shahenshah\nfrom: Shahenshah "
        )
    if x == 4:
        await event.edit(
            "Kaun kambakth hai jo bardasht karne ke liye peeta hai. Main toh peeta hoon ke bas saans le sakoon\nfrom:devdas"
        )
    if x == 5:
        await event.edit("Main aaj bhi pheke hue paise nahin uthata\nfrom: deewar")
    if x == 6:
        await event.edit("Pushpa, I hate tears...\nfrom: Amar Prem")
    if x == 7:
        await event.edit(
            "Bade bade shehron mein aisi chhoti chhoti baatein hoti rehti hain, Senorita.\nfrom: Dilwale Dulhaniya le jayenge  "
        )
    if x == 8:
        await event.edit("Mogambo khush hua!\nFrom: Mr. India")
    if x == 9:
        await event.edit(
            "Taareekh pe taareekh, taareekh pe taareekh, taarekh pe taareekh\nFrom: Damini"
        )
    if x == 10:
        await event.edit(
            "Dosti ka ek usool hai, madam: no sorry, no thank you\nFrom:Maine Pyaar Kiya"
        )
    if x == 11:
        await event.edit(
            "Filmein sirf teen cheezon ki wajah se chalti hain- entertainment, entertainment, entertainment. Aur main entertainment hoon!\nFrom: The Dirty Picture"
        )
    if x == 12:
        await event.edit(
            "Zindagi mein bhi end mein sab theek ho jaata hai. Happys Endings. Aur agar, aur agar theek na ho to woh the end nahin hai dosto, picture abhi baaki hai.\nFrom: Om Shanti Om"
        )
    if x == 13:
        await event.edit(
            "Kabhi Kabhi Kuch Jeetne Ke Liya Kuch Haar Na Padta Hai. Aur Haar Ke Jeetne Wale Ko Baazigar Kehte Hain.\nFrom:Baazigar"
        )
    if x == 14:
        await event.edit(
            "Salim tujhe marne nahi dega ... aur hum Anarkali tujhe jeene nahi denge.\nFrom:Mughal-e-Azam"
        )
    if x == 15:
        await event.edit(
            "Don ka intezaar toh baarah mulko ki police kar rahi hai, but Don ko pakadna mushkil hi nahi, namumkin hai\nFrom: Don"
        )
    if x == 16:
        await event.edit(
            "Aapke paon dekhe, bahut haseen hai. Inhe zameen par mat utariyega, maile ho jayenge\nFrom:Pakeezah"
        )
    if x == 17:
        await event.edit(
            "Hum tum mein itne ched karenge ... ki confuse ho jaoge ki saans kahan se le ... aur paadein kahan se\nFrom: Dabangg"
        )
    if x == 18:
        await event.edit(
            "Crime Master Gogo naam hai mera, aankhen nikal ke gotiyan khelta hun main.\nFrom: Andaaz apna apna"
        )
    if x == 19:
        await event.edit(
            "Hum jahan khade ho jaate hain, line wahi se shuru hoti hain.\nFrom: Kaalia"
        )
    if x == 20:
        await event.edit("Thapad se darr nahi lagta, pyaar se lagta hai\nFrom:Dabangg")
    if x == 21:
        await event.edit(
            "Our Business Is\nOur Business/nNone of Your Business\nFrom: Race 3"
        )
    if x == 22:
        await event.edit("Jo Ye Tera\nTorture Hai Wo\nMera Warm-up Hai\nFrom: Baaghi 2")
    if x == 23:
        await event.edit(
            "School Ke Bahar\nJab Zindagi Imtehaan\nLeti Hai To Subject Wise\nNahi Leti\nFrom: Hichki"
        )
    if x == 24:
        await event.edit(
            "America Ke Pas Superman Hai,\nBatman Hai, Spiderman Hai…\n Lekin India Ke Pas Padman Hai\nFrom: Padman"
        )
    if x == 25:
        await event.edit("Written and Created By: @Eviral ! thank you🙏🏻❤")


CmdHelp("randomdialogue").add_command("rfilmy", None, "Use and See").add()
