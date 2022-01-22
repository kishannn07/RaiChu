from pyrogram import client, filters
import asyncio
import time
from RaiChUB import edrep, RaiChUB , Adminsettings

__MODULE__ = "chat link"
__HELP__ = """
__**This command helps you to instantly get the invite link of the chat**__
──「 **Usage** 」──
-> `admins`
"""
HNDLR="."
AdminSettings= [1359459092]


@RaiChUB.on_message(filters.command("invitelink",HNDLR) & filters.user(Adminsettings))
async def invite_link(client, message):
    if message.chat.type in ["group", "supergroup"]:
        chat_name = message.chat.title
        try:
                link = await RaiChUB.export_chat_invite_link(message.chat.id)
                await message.reply_text(f"The invite link for chat is {link}")
        except Exception as e:
                print(e)
                await message.reply_text("denied permission")
