import os

from telethon import TelegramClient
from telethon.sessions import StringSession

from userbot.Config import Config

try:
    from userbot import bot
except:
    pass

API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("BOT_TOKEN", None)
lnbot = TelegramClient("EVIRAL", API_ID, API_HASH).start(bot_token=token)


class EVIRAL(TelegramClient):
    def __init__(self, string, api_id, api_hash):
        super().__init__(StringSession(string), api_id, api_hash)
        self.id = None
        self.username = None
        self.bot_username = None
        self.bot_token = None
        self.heroku_username = None

    def set(self, **u):
        if u.get("bot_username"):
            self.bot_username = u["bot_username"]
        if u.get("id"):
            self.id = u["id"]
        if u.get("username"):
            self.username = u["username"]
        if u.get("bot_token"):
            self.bot_token = u["bot_token"]
        if u.get("heroku_username"):
            self.heroku_username = u["heroku_username"]

    def __str__(self):
        detail = f"""
Your name is {self.me.first_name}
Your username is @{self.me.username or "no Username"}
Your bot Username is @{self.bot_username}
Your heroku bot username is {self.heroku_username}"""
        return detail


if Config.eviral_STRING:
    session_name = str(Config.eviral_STRING)
    sweetie = EVIRAL(session_name, Config.APP_ID, Config.API_HASH)
else:
    session_name = "startup"
    bbbot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)

if __name__ == "__main__":
    bot.start()
    bot.run_until_disconnected()
    sweetie.run_until_disconnected()
    lnbot.run_until_disconnected()
