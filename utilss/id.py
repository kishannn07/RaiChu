from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "id"
__HELP__ = """
__**This command helps you to get id of a user in the chat**__
──「 **Usage** 」──
-> `id`
"""

@RaiChUB.on_message(filters.command("id",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def id(_, message):
    if message.reply_to_message is None:
        await message.reply(f"This chat's ID is: {message.chat.id}")
    else:
        test = f"This scumbag's ID is: {message.reply_to_message.from_user.id}\n\nThis chat's ID is: {message.chat.id}"
        await message.edit_text(test)
