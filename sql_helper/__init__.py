import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from uti.confi import Var
import motor.motor_asyncio
mongo_dbb = motor.motor_asyncio.AsyncIOMotorClient(Var.MONGO_DB)
dbb = mongo_dbb["KING"]
def start() -> scoped_session:
    engine = create_engine(Var.DB_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

def start() -> scoped_session:
    dbi_url=Var.DB_URL
    engine = create_engine(dbi_url)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))
