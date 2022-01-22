from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "unban"
__HELP__ = """
__**This command helps you to instantly unban a user in the chat**__
──「 **Usage** 」──
-> `unban`
"""

@RaiChUB.on_message(filters.group & filters.command("unban",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def member_unban(_ , message):
    msg_id=message.message_id
    chat_msg=message.text
    username=None
     
    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id

    chat_id=message.chat.id
    me_m =await client.get_me()
    me_ = await message.chat.get_member(int(me_m.id))
    user_info=await RaiChUB.get_users(username)
    if me_.can_restrict_members:      
        await RaiChUB.unban_chat_member(chat_id , username)
        if(user_info.username):
            usercontact=user_info.username
            reply_string="@"+usercontact+" has been picked up from hell 😈"
            await RaiChUB.edit_message_text(chat_id , msg_id , reply_string)
        else:
            usercontact=user_info.first_name
            reply_string=usercontact+" has been picked up from 😈"
            await RaiChUB.edit_message_text(chat_id , msg_id , reply_string)
    else:
        reply_string="Noob,you can't unban members 😂 !"
        await RaiChUB.edit_message_text(chat_id , msg_id , reply_string )
