from pyrogram import filters
from kingbot import kingbot, setbot , vr, Adminsettings
from pyrogram import filters 
from sql_helper.autopostingdb import (
    add_new_autopost,
    check_if_autopost_in_db,
    del_autopost,
    get_autopost,
)
__MODULE__ = "Auto Post"
__HELP__ = """**This command helps you to Auto post**
-> `autopost` `rmapst`
"""

@kingbot.on_message(filters.command("autopost", vr.get("HNDLR")) & filters.user(Adminsettings))
async def autopost(client, message):
    senr = await message.edit_text("`Processing..`")
    chnnl = get_text(message)
    if not chnnl:
        await senr.edit("`Provide Channel ID!`")
        return
    if str(chnnl).startswith("-100"):
        kk = str(chnnl).replace("-100", "")
    else:
        kk = chnnl
    if not kk.isnumeric():
        try:
            u_ = await client.get_chat(kk)
        except:
            await senr.edit("`Invalid Chat ID / Username!`")
            return
        kk = str(u_.id).replace("-100", "")
    if await check_if_autopost_in_db(message.chat.id, kk):
        await senr.edit("Channel Already In DB")
        return
    await add_new_autopost(message.chat.id, kk)
    await senr.edit(f"`Added AutoPosting To This Channel From {chnnl}`")


@kingbot.on_message(filters.command("rmapst", vr.get("HNDLR")) & filters.user(Adminsettings))
async def rmautopost(client, message):
    cenr = await message.edit_text("`Processing..`")
    chnnl = get_text(message)
    if not chnnl:
        await cenr.edit("`Provide Channel ID!`")
        return
    if str(chnnl).startswith("-100"):
        kk = str(chnnl).replace("-100", "")
    else:
        kk = chnnl
    if not kk.isnumeric():
        try:
            u_ = await client.get_chat(kk)
        except:
            await cenr.edit("`Invalid Chat ID / Username!`")
            return
        kk = str(u_.id).replace("-100", "")
    if not await check_if_autopost_in_db(message.chat.id, kk):
        await cenr.edit("Channel Not In DB")
        return
    await del_autopost(message.chat.id, kk)
    await cenr.edit(f"`Removed AutoPosting To This Channel From {chnnl}`")


@kingbot.on_message(
    (filters.incoming | filters.outgoing)
    & filters.channel
    & ~filters.edited
    & ~filters.service
)
async def autoposterz(client, message):
    chat_id = str(message.chat.id).replace("-100", "")
    if not await get_autopost(int(chat_id)):
        
        return
    channels_set = await get_autopost(int(chat_id))
    if not channels_set:
        
        return
    for chat in channels_set:
        try:
            await message.copy(int(chat["to_channel"]))
        except Exception as err:
            print(err)
            pass
    
