from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

M = (
    "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈▏ν2.ο\n"
)


@borg.on(admin_cmd(pattern=r"spong"))
async def kek(kek):
    await kek.edit(M)


D = (
    "╭━┳━╭━╭━╮╮\n"
    "┃┈┈┈┣▅╋▅┫┃\n"
    "┃┈┃┈╰━╰━━━━━━╮\n"
    "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
    "╲┃┈┈┈┈╭━┳━━━━╯\n"
    "╲┣━━━━━━┫\n"
)


@borg.on(admin_cmd(pattern=r"dogs"))
async def dog(dog):
    await dog.edit(D)


P = (
    "┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┗┻┛┗┻┛┈┈┈┈ν2.ο\n"
)


F = (
    " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈ν2.ο\n"
)

E = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈ν2.ο\n"
)

H = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈HOMER\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈ν2.ο\n"
)


@borg.on(admin_cmd(pattern=r"fox"))
async def fox(fox):
    await fox.edit(F)


@borg.on(admin_cmd(pattern=r"elephant"))
async def elephant(elephant):
    await elephant.edit(E)


@borg.on(admin_cmd(pattern=r"homer"))
async def homer(homer):
    await homer.edit(H)


@borg.on(admin_cmd(pattern=r"pig"))
async def pig(pig):
    await pig.edit(P)


CmdHelp("animal").add_command("pig", None, "pig face").add_command(
    "homer", None, "Homer Face"
).add_command("elephant", None, "Elephant Face").add_command(
    "fox", None, "Fox Face•"
).add_command(
    "dogs", None, "Dog Face"
).add_command(
    "spong", None, "Spong Face"
).add_info(
    "Its Very Useful Module Its used for showing some animal characters"
).add_warning(
    "Harmless Module✅"
).add_type(
    "Addons"
).add()
