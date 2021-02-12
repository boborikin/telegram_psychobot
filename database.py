from gino import Gino
from aiogram import Dispatcher

from settings import DATABASE_STR
from sqlalchemy import and_

db = Gino()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    telegram_id = db.Column(db.Integer())
    username = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=True)
    state = db.Column(db.JSON(), default={'step': '1'})


class Request(db.Model):
    __tablename__ = "requests"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String)
    successful = db.Column(db.Boolean(), default=False)
    word_p = db.Column(db.String, nullable=True)
    emotion = db.Column(db.String, nullable=True)
    situation = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))


# class Statistic(db.Model):
#     __tablename__ = 'statistic'

#     id = db.Column(db.Integer(), primary_key=True)
#     rec = db.Column(db.String)
#     successful = db.Column(db.Boolean(), default=False)


async def get_reqs(user_id: int) -> tuple:
    reqs = await Request.query.where(and_(
        Request.user_id==user_id
    )).gino.all()
    all_reqs = await Request.query.where(and_(
        Request.word_p != None,
        Request.emotion != None,
        Request.situation != None
    )).gino.all()
    if all_reqs is None:
        count = 0
    else:
        count = len(all_reqs)
    if reqs is None:
        reqs = []
    return reqs, count


async def write_statistic(rec, word_p, emotion, situation, user_id):
    q = await Request.query.where(and_(Request.emotion==emotion, Request.word_p == word_p)).gino.all()
    if q is None:
        q = 0
    else:
        q = len(q)
    await Request.create(
        name=rec,
        successful=True,
        word_p=word_p,
        emotion=emotion,
        situation=situation,
        user_id=user_id
    )
    return q

async def on_startup(dispatcher: Dispatcher) -> None:
    await db.set_bind(DATABASE_STR)
    await db.gino.create_all()


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await db.pop_bind().close()
