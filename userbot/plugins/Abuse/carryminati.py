import asyncio
import random

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"carry$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("speaking a line.......")
    await asyncio.sleep(2)
    x = random.randrange(1, 25)
    if x == 1:
        await event.edit("To Kaise Hai AAp Log??**")
    if x == 2:
        await event.edit("Mithai Ki Dukan Pe Leke Jaunga200 Me Bik Jayega ")
    if x == 3:
        await event.edit("Ab Aayega Maza Hmmmmmmm ")
    if x == 4:
        await event.edit(
            "Agar Ye Banda Cricket Mein Commentary KarnaShuru Kar De.. To Match Ka Kya Hoga"
        )
    if x == 5:
        await event.edit("Tiktokers Ke Kanome Ek Hi Avaj ,To Kiase He Aap Log ")
    if x == 6:
        await event.edit(
            "Pathhar Se Mat Maro Mere Diwano Ko,Bum Ka Jamana Hai Udado Salo Ko "
        )
    if x == 7:
        await event.edit("Duniya madar***d thi, madar***d hai aur madar***d rahegi. ")
    if x == 8:
        await event.edit("Youthube ")
    if x == 9:
        await event.edit("Aao yaar apne kaano mein earphone daalo.")
    if x == 10:
        await event.edit(
            "Ek to aap muje benchoo benchoo bolna band kijiye , kya bigaada hai meine apka , aap honge benchoo."
        )
    if x == 11:
        await event.edit(
            "Ganta bancho, sirf dukandaron ka faiyda hota hai isme , aur benchoo kis chutiye ne valentine’s week bnaya hai, pure saal nukkad mein chai biscuit khake paise bchao aur ek hafte mein aise udaa do jaise baap ki koyle ki factory hoo. Banchoo!! "
        )
    if x == 12:
        await event.edit(
            " Saat din, Sunday se leke agle sunday tak gifts do….Akhand Chuityapa Banchoo !!"
        )
    if x == 13:
        await event.edit(
            " Woh kehti hai grow some balls, ab doo ke teen kaise karu bancho."
        )
    if x == 14:
        await event.edit(
            "“Aaj mei thakne ke mood mei nahi thakane ke mood mei hoon..” ... "
        )
    if x == 15:
        await event.edit("“Joh bistar pe zabaan dete hain woh aksar badal jate hain”")
    if x == 16:
        await event.edit(
            "Pichwade mein itni goli maroonga ... ki uske bachche pittal ke paida honge"
        )
    if x == 17:
        await event.edit(
            "Hamara income high ho na ho ... outcome toh hamara bhi world class hai"
        )
    if x == 18:
        await event.edit("Bhoot bhoot ... inki maa ki ")
    if x == 19:
        await event.edit(
            "Log sunenge to kya kahenge ... chutiya aashiqui ke chakkar mein mar gaya, aur laundiya bhi nahi mili"
        )
    if x == 20:
        await event.edit("Pehli baar mein sabse zyada mazaa aata hai ")
    if x == 21:
        await event.edit(
            "Pachaas pachaas kos door jab gaon mein Holi hoti hai ... toh maa kehti hai sooja beti sooja ... varna apni pichkaari lekar Jabbar aa jayega "
        )
    if x == 22:
        await event.edit(
            "Koi madharchod button dabakar mere liye yeh faisla nahin karega ... ki mujhe kab marna hai"
        )
    if x == 23:
        await event.edit(
            "Aaj kal pyar na naukrani jaisa ho gaya hai ... aata hai, bell bhajata hai, kaam karta hai aur chala jaata hai"
        )
    if x == 24:
        await event.edit(
            "Meri mardangi ke bare mein aap gaon ki kisi bhi ladki se pooch sakte ho ... report achchi milegi "
        )
    if x == 25:
        await event.edit("Written and Created By: @MYSTERIOUS_PLUGINS ! thank you🙏🏻❤")


CmdHelp("carryminati").add_command("carry", None, "CarryMinati").add_type("Abuse").add()
