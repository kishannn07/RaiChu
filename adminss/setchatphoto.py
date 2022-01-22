from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "setchatphoto"
__HELP__ = """
__**This command helps you set chat photo **__
──「 **Usage** 」──
-> `setchatphoto`
"""

@RaiChUB.on_message(filters.group & filters.command("setchatphoto",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def set_chat_photo(_, message):
    msg_id=message.message_id
    chat_id=message.chat.id
    zuzu=await RaiChUB.get_chat_member(chat_id , "me")
    can_change_admin=zuzu.can_change_info
    can_change_member=message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("You don't have enough permission")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await RaiChUB.set_chat_photo(chat_id , photo=message.reply_to_message.photo.file_id)
            return
    else:
        await message.edit_text("Reply to a photo to set it !")
