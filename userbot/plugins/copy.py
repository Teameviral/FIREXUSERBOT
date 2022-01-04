from userbot import CmdHelp
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="copy"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(the_real_message)
    else:
        await event.edit(".copy Reply to a  message to copy and paste")


CmdHelp("copy").add_command("copy", "<Reply To User>", " To Copy Message").add_info(
    "Its Help U to Copy Message and auto send"
).add_warning("Harmless Module✅").add_type("Official").add()
