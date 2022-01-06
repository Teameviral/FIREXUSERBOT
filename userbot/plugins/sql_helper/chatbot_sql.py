from sqlalchemy import Column, String

from . import BASE, SESSION

"""class ChatBot(BASE):
    __tablename__ = "chatbot"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(String(14), primary_key=True, nullable=False)
    chat_name = Column(UnicodeText)
    user_name = Column(UnicodeText)
    user_username = Column(UnicodeText)
    chat_type = Column(UnicodeText)

    def __init__(
        self, chat_id, user_id, chat_name, user_name, user_username, chat_type
    ):
        self.chat_id = str(chat_id)
        self.user_id = str(user_id)
        self.chat_name = chat_name
        self.user_name = user_name
        self.user_username = user_username
        self.chat_type = chat_type

    def __eq__(self, other):
        return bool(
            isinstance(other, ChatBot)
            and self.chat_id == other.chat_id
            and self.user_id == other.user_id
        )


ChatBot.__table__.create(checkfirst=True)


def is_added(chat_id, user_id):
    try:
        return SESSION.query(ChatBot).get((str(chat_id), str(user_id)))
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_users(chat_id):
    try:
        return SESSION.query(ChatBot).filter(ChatBot.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def get_all_users():
    try:
        return SESSION.query(ChatBot).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def addai(chat_id, user_id, chat_name, user_name, user_username, chat_type):
    to_check = is_added(chat_id, user_id)
    if not to_check:
        adder = ChatBot(
            str(chat_id), str(user_id), chat_name, user_name, user_username, chat_type
        )
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(ChatBot).get((str(chat_id), str(user_id)))
    SESSION.delete(rem)
    SESSION.commit()
    adder = ChatBot(
        str(chat_id), str(user_id), chat_name, user_name, user_username, chat_type
    )
    SESSION.add(adder)
    SESSION.commit()
    return False


def remove_ai(chat_id, user_id):
    to_check = is_added(chat_id, user_id)
    if not to_check:
        return False
    rem = SESSION.query(ChatBot).get((str(chat_id), str(user_id)))
    SESSION.delete(rem)
    SESSION.commit()
    return True


def remove_users(chat_id):
    saved_filter = SESSION.query(ChatBot).filter(ChatBot.chat_id == str(chat_id))
    if saved_filter:
        saved_filter.delete()
        SESSION.commit()


def remove_all_users():
    saved_filter = SESSION.query(ChatBot)
    if saved_filter:
        saved_filter.delete()
        SESSION.commit()
"""


import threading

from sqlalchemy import Column, String


class ChatbotChats(BASE):
    __tablename__ = "chatbot_chats"
    chat_id = Column(String(14), primary_key=True)
    ses_id = Column(String(70))
    expires = Column(String(15))

    def __init__(self, chat_id, ses_id, expires):
        self.chat_id = chat_id
        self.ses_id = ses_id
        self.expires = expires


ChatbotChats.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def is_chat(chat_id):
    try:
        chat = SESSION.query(ChatbotChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()


def set_ses(chat_id, ses_id, expires):
    with INSERTION_LOCK:
        autochat = SESSION.query(ChatbotChats).get(str(chat_id))
        if not autochat:
            autochat = ChatbotChats(str(chat_id), str(ses_id), str(expires))
        else:
            autochat.ses_id = str(ses_id)
            autochat.expires = str(expires)

        SESSION.add(autochat)
        SESSION.commit()


def get_ses(chat_id):
    autochat = SESSION.query(ChatbotChats).get(str(chat_id))
    sesh = ""
    exp = ""
    if autochat:
        sesh = str(autochat.ses_id)
        exp = str(autochat.expires)

    SESSION.close()
    return sesh, exp


def rem_chat(chat_id):
    with INSERTION_LOCK:
        autochat = SESSION.query(ChatbotChats).get(str(chat_id))
        if autochat:
            SESSION.delete(autochat)

        SESSION.commit()


def get_all_chats():
    try:
        return SESSION.query(ChatbotChats.chat_id).all()
    finally:
        SESSION.close()
