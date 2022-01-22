from pyrogram import filters
from pyrogram.types import Message
from RaiChUB import RaiChUB, setbot , vr , Adminsettings
import asyncio
__MODULE__ = "invite"
__HELP__ = """
->`invite`
__**This command helps you to invite members in a chat**__
──「 **Usage** 」──
"""
@RaiChUB.on_message(filters.user(Adminsettings) & filters.command("invite", vr.get("HNDLR")))
async def inviteee(client, message):
    mg = await message.edit_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ",1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")
