from re import compile

from telethon import events
from telethon.events import callbackquery

from FIREX.utils import *
from userbot import *
from userbot import ALIVE_NAME
from userbot.cmdhelp import *
from userbot.Config import Config

eviral_row = Config.BUTTONS_IN_HELP
eviral_emoji = Config.EMOJI_IN_HELP1

from . import *

# main menu for api setting


@firebot.on(callbackquery.CallbackQuery(data=compile(b"apiset")))
async def apiset(event):
    await event.edit(
        get_string("ast_1"),
        buttons=[
            [Button.inline("Remove.bg API", data="rmbg")],
            [Button.inline("DEEP API", data="dapi")],
            [Button.inline("OCR API", data="oapi")],
            [Button.inline("« Back", data="setter")],
        ],
    )


@firebot.on(callbackquery.CallbackQuery(data=compile(b"rmbgapi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "RMBG_API"
    name = "Remove.bg API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(get_string("ast_2"))
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@firebot.on(callbackquery.CallbackQuery(data=compile(b"dapi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "DEEP_API"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your Deep Api from deepai.org and send here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{ALIVE_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@firebot.on(callbackquery.CallbackQuery(data=compile(b"oaspi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "OCR_API"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your OCR api from ocr.space Send Send Here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{ALIVE_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )
