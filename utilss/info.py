from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "info"
__HELP__ = """
__**This command helps you to get info of a user in the chat**__
──「 **Usage** 」──
-> `info`
"""

@RaiChUB.on_message(filters.group & filters.command("info",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def info(_, message):
    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention
    if username:
        username = f"@{username}"
        text = f"""
<b>User info</b>:
ID: <code>{id}</code>
First Name: {first_name}
Username: {username}
User link: {user_link}"""
    else:
        text = f"""
<b>User info</b>:
ID: <code>{id}</code>
First Name: {first_name}
User link: {user_link}"""
    await message.reply(text, parse_mode="HTML")
