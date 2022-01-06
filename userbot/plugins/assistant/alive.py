from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『FIRE-X』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{eviral_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『FIRE-X』~ `{eviralversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Its_FIREX)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/The-FIREX/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『FIRE-X』 ](https://t.me/FirexSupport)\n"
pm_caption += f"┣Assistant ~ By [『Lêɠêɳ̃dẞøy』 ](https://t.me/Its_eviralBoy)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『FIRE-X』](https://t.me/FirexSupport) «««"


@firebot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await firebot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
