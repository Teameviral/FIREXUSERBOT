import asyncio
import io
import os
from pathlib import Path

from FIREX.utils import *
from userbot import *

from . import *

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "『FIRE-X』"
eviral = bot.uid
eviral = f"[{DEFAULTUSER}](tg://user?id={eviral})"
EVAL = os.environ.get("EVAL", None)


@bot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = eviral_logo1
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ 𝙿𝚕𝚞𝚐𝚒𝚗 𝚗𝚊𝚖𝚎 ≈** `{input_str}`\n**⍟ 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 ≈** {eviral_mention}\n\n⚜ **[FIRE-X](https://t.me/FirexSupport)** ⚜"
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    the_1plugin_file = "./userbot/plugins/Abuse/{}.py".format(input_str)
    the_2plugin_file = "./userbot/plugins/Spam/{}.py".format(input_str)
    the_3plugin_file = "./userbot/plugins/Xtra_Plugin/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda1 = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
        return
    elif os.path.exists(the_1plugin_file):
        lauda2 = await event.client.send_file(
            event.chat_id,
            the_1plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
        return
    elif os.path.exists(the_2plugin_file):
        lauda3 = await event.client.send_file(
            event.chat_id,
            the_2plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
        return
    elif os.path.exists(the_3plugin_file):
        lauda4 = await event.client.send_file(
            event.chat_id,
            the_3plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")


@bot.on(admin_cmd(pattern="install ?(.*)"))
@bot.on(sudo_cmd(pattern="install ?(.*)", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    b = 1
    owo = event.text[9:]
    eviral = await eor(event, "__Installing.__")
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "./userbot/plugins/",  # pylint:disable=E0602
                )
            )
            op = open(downloaded_file_name, "r")
            rd = op.read()
            op.close()
            try:
                if EVAL == "ON":
                    if "session" in rd:
                        os.remove(downloaded_file_name)
                        await eviral.edit(
                            f"**⚠️ WARNING !!** \n\n__Replied plugin file contains some harmful codes__."
                        )
                        return
                    elif "(" not in downloaded_file_name:
                        path1 = Path(downloaded_file_name)
                        shortname = path1.stem
                        load_module(shortname.replace(".py", ""))
                        if shortname in CMD_LIST:
                            string = "**Commands found in** `{}`\n".format(
                                (os.path.basename(downloaded_file_name))
                            )
                            for i in CMD_LIST[shortname]:
                                string += "  •  `" + i
                                string += "`\n"
                                if b == 1:
                                    a = "__Installing..__"
                                    b = 2
                                else:
                                    a = "__Installing...__"
                                    b = 1
                                await eviral.edit(a)
                            return await eviral.edit(
                                f"✅ **Installed module** :- `{shortname}` \n✨ BY :- {eviral_mention}\n\n{string}\n\n        ⚡ **[FIRE-X]({chnl_link})** ⚡",
                                link_preview=False,
                            )

                        return await eviral.edit(
                            f"Installed module `{os.path.basename(downloaded_file_name)}`"
                        )
                    else:
                        os.remove(downloaded_file_name)
                        return await eod(
                            eviral,
                            f"**Failed to Install** \n`Error`\nModule already installed or unknown format",
                        )
                else:
                    return await eod(
                        eviral, "First Turn ON Eval CMD = `.set var EVAL ON`"
                    )
            except Exception as e:
                await eod(eviral, f"{e}")
                return os.remove(download_file_name)
        except Exception as e:
            await eod(eviral, f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)


@bot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**Uninstalled** `{shortname}` Successfully")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))


@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"upload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(shortname, str(e))
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )


@bot.on(admin_cmd(pattern=r"cmds"))
@bot.on(sudo_cmd(pattern=r"cmds", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls userbot/plugins"
    thumb = eviral_logo1
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"♥️List Of Plugins In 𝖑𝖊ɠêɳ̃dẞø✞︎ 🇮🇳 :- \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nHELP:- If you want to know the commands for a plugin, do :- \n.plinfo <plugin name> without the < > brackets. \nJoin https://t.me/FirexSupport for help."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmnds_list.text"
            eviral_file = await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(
                eviral_file,
                f"**Output Too Large. This is the file for the list of plugins in L𝖊ɠêɳ̃dẞø✞︎**.\n\nBY :- **{DEFAULTUSER}**",
            )
            await event.delete()


CmdHelp("core").add_command(
    "install",
    "<reply to a .py file>",
    "Installs the replied python file if suitable to userbot codes. (TEMPORARILY DISABLED AS HACKERS MAKE YOU INSTALL SOME PLUGINS AND GET YOUR DATA)",
).add_command(
    "uninstall",
    "<plugin name>",
    "Uninstalls the given plugin from userbot. To get that again do .restart",
    "uninstall alive",
).add_command(
    "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
    "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
    "send",
    "<file name>",
    "Sends the given file from your userbot server, if any.",
    "send alive",
).add_command(
    "cmds", None, "Gives out the list of modules in FIREX."
).add_warning(
    "Before Install Any Plugin.Open That File file by command .open"
).add_info(
    "Xtra Plugin"
).add_type(
    "Official"
).add()
