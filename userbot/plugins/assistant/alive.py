from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『FIRE-X』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{eviral_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『FIRE-X』~ `{eviralversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/FIREXUB)\n"
pm_caption += f"┣**License** ~ [License v3.0](https://github.com/Teameviral/FIREXUSERBOT/blob/main/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『FIRE-X』 ](https://t.me/Fire_X_Channel)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『FIRE-X』](https://t.me/FirexSupport) «««"


@firebot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await firebot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
