# This useless plugin is made By @eviralboi_atul..
# Downloads songs from Spotify
# Keep credits if gonna kang...do not remove/edit this line..

import glob
import subprocess

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

CmdHelp("getsongs").add_command("getsong <songname>", None, "Geting ur music").add()


@borg.on(admin_cmd(pattern="getsong ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "**Getting Your Music it may take a few seconds to fetch the song from you tube and download it..**"
    )
    cmd = event.pattern_match.group(1)
    cmnd = f"{cmd}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    subprocess.run(["spotdl", "-s", cmnd, "-q", "best"])
    subprocess.run(
        'for f in *.opus; do      mv -- "$f" "${f%.opus}.mp3"; done', seviral=True
    )
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Yeah, I found the song..🎶`")
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        allow_cache=False,
        supports_streaming=True,
        caption="Uploaded successfully by Black Lightning   userbot..!",
        reply_to=reply_to_id,
    )
    subprocess.run("rm -rf *.mp3", seviral=True)
