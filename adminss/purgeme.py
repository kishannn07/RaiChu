from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "purgeme"
__HELP__ = """
__**This command helps you to delete your last 'n' messages in the chat**__
──「 **Usage** 」──
-> `purgeme`
"""

@RaiChUB.on_message(filters.command("purgeme",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def purgeme(client , message):
    msg_text=message.text
    chat_id=message.chat.id
    if " " in msg_text:
        number=msg_text[msg_text.index(" ")+1 : len(msg_text)]
        if(not number.isnumeric()):
            await message.edit_text("Need a number to delete !")
        else:
            number=int(number)
            msg_id=message.message_id - 1
            while number > 0:
                try:
                    print(msg_id)
                    if RaiChUB.get_messages(chat_id , msg_id).from_user.id == RaiChUB.get_users("me").id:
                        await RaiChUB.delete_messages(chat_id , msg_id)
                        print("Heyyy")
                        number=number-1
                    msg_id=msg_id-1
                except Exception as e:
                    msg_id=msg_id-1
    else:
        await message.edit_text("Give me a number to delete !!")
