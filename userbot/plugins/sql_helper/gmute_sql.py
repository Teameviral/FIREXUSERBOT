"""try:
    from userbot.plugins.sql_helper import BASE, SESSION
except ImportError:
    raise Exception("hello!")

from sqlalchemy import Column, String


class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GMute.__table__.create(checkfirst=True)


def is_gmuted(sender_id):
    try:
        return SESSION.query(GMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmute(sender):
    adder = GMute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender):
    rem = SESSION.query(GMute).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def all_gmuted():
    rem = SESSION.query(GMute).all()
    SESSION.close()
    return rem
"""

from sqlalchemy import Column, String

from . import BASE, SESSION


class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, sender, chat_id):
        self.sender = str(sender)
        self.chat_id = str(chat_id)


GMute.__table__.create(checkfirst=True)


def is_gmuted(sender, chat_id):
    user = SESSION.query(GMute).get((str(sender), str(chat_id)))
    if user:
        return True
    else:
        return False


def gmute(sender, chat_id):
    adder = GMute(str(sender), str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender, chat_id):
    rem = SESSION.query(GMute).get((str(sender), str(chat_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
