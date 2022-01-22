from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
from joke_generator import generate

__MODULE__ = "joke"
__HELP__ = """
__**This command helps you get a joke in the chat**__
──「 **Usage** 」──
-> `joke`
"""

@RaiChUB.on_message(filters.command("joke",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def joke(_, message):
    await message.edit_text(generate())
