from kingbot import kingbot , vr , Adminsettings, setbot
from utilss.vitoo import run_cmd
from utilss.paste import get_text
import asyncio
from pyrogram import filters

@kingbot.on_message(filters.command("qt", vr.get("HNDLR")) & filters.user(Adminsettings))
async def nice_qbot(client, message):
    m = await message.edit_text("`Making A Quote.`")
    query = get_text(message)
    msg_ids = []
    if not query:
        if not message.reply_to_message:
            return await m.edit("`Reply To Message To Make A Quote.`")
        msg_ids.append(message.reply_to_message.message_id)   
    else:
        if not query.isdigit():
            return await m.edit("`Uh? Only Digits My Friend.`")
        if int(query) == 0:
            return await m.edit("`Uh?, You Are Zero.`")
        async for msg in client.iter_history(chat_id=message.chat.id, reverse=True, limit=int(query)):
            if message.message_id != msg.message_id:
                msg_ids.append(msg.message_id)
    if not msg_ids:
        return await m.edit("`Uh?, You Are Zero.`")
    await client.forward_messages("@QuotLyBot", message.chat.id, msg_ids) 
    await asyncio.sleep(7)
    histor_ = await check_history("@QuotLyBot", client)
    if not histor_:
        return await m.edit("`Invalid or No Response Recieved.`")
    if message.reply_to_message:
        await histor_.copy(message.chat.id, reply_to_message_id=message.reply_to_message.message_id)
    else:
        await histor_.copy(message.chat.id)
    await m.delete()
    
         
       
async def check_history(bot, client):
    its_history = (await client.get_history(bot, 1))[0]
    meeee=await client.get_me()
    if its_history.from_user.id == meeee.id:
        return None
    if not its_history.sticker:
        return None
    return its_history
