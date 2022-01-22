from pyrogram import client , filters
from pyrogram.types import Message
from RaiChUB import RaiChUB , setbot,Adminsettings
__MODULE__ = "start"
__HELP__ = """**Just a start message**
"""
HNDLR="/"
@setbot.on_message(filters.command("start",HNDLR) & filters.user(Adminsettings))
async def start(_, message: Message):
    await message.reply_text(
        "Shit u are allowed dear!! \n Only RaiChu wield this power" )
@setbot.on_message(filters.command("start",HNDLR) & ~filters.user(Adminsettings))
async def starti(_, message: Message):
    await message.reply_text(
        "Shit u are not allowed dear!! \n Only RaiChu wield this power" )
