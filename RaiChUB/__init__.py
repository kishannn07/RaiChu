import pytgcalls
import os
from datetime import datetime
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from logging import warning as wr
from pyrogram import Client
from pyrogram.types import Message
from decouple import config
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from redis import ConnectionError, ResponseError, StrictRedis
from uti.confi import Var
LOGS = getLogger(__name__)

starttimer=datetime.now()
if not Var.API_ID or not Var.API_HASH:
    wr("No API_ID or API_HASH found.    Quiting...")
    exit(1)

Adminsettings= [Var.OWNER_ID]
# Adminsettings= Adminsettings.append(Var.OWNER_ID)


START_TIME = datetime.now()


try:
    redis_info = Var.REDIS_URI.split(":")
    vr = StrictRedis(
        host=redis_info[0],
        port=redis_info[1],
        password=Var.REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
except ConnectionError as ce:
    wr(f"ERROR - {ce}")
    exit(1)
except ResponseError as res:
    wr(f"ERROR - {res}")
    exit(1)

try:
    if vr.get("HNDLR"):
        HNDLR = vr.get("HNDLR")
    else:
        vr.set("HNDLR", ".")
        HNDLR = vr.get("HNDLR")
except BaseException:
    pass

if vr.get("SUDOS") is None:
    vr.set("SUDOS", "1")
if vr.get("VC_SESSION"):
    vc_session=vr.get("VC_SESSION")
    vc_api_id= vr.get("VC_API_ID")
    vc_api_hash=vr.get("VC_API_HASH")
    vcbot = Client(vc_session, api_id=vc_api_id, api_hash=vc_api_hash)
else:
    vcbot = None


# Postgresqlw5mj by
#def mulaisql() -> scoped_session:


async def get_bot_inline(bot):
    global BOTINLINE_AVAIABLE
    if setbot:
        try:
            await naruto.get_inline_bot_results("@{}".format(bot.username), "test")
            BOTINLINE_AVAIABLE = True
        except errors.exceptions.bad_request_400.BotInlineDisabled:
            BOTINLINE_AVAIABLE = False


async def get_self():
    global Owner, OwnerName, OwnerUsername
    getself = await RaiChUB.get_me()
#     Adminsettings={}
    Owner = getself.id
    vr.set("SUDOS" , Owner)
    if getself.last_name:
        OwnerName = getself.first_name + " " + getself.last_name
    else:
        OwnerName = getself.first_name
    OwnerUsername = getself.username
    
       

async def get_bot():
    global BotID, BotName, BotUsername
    getbot = await setbot.get_me()
    BotID = getbot.id
    BotName = getbot.first_name
    BotUsername = getbot.username


BASE = declarative_base()
setbot = Client(":memory:",api_id=Var.API_ID, api_hash=Var.API_HASH, bot_token=Var.BOT_TOKEN )
RaiChUB = Client(Var.SESSION, api_id=Var.API_ID, api_hash=Var.API_HASH)
async def edrep(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})
