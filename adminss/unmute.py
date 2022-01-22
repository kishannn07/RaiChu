from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "unmute"
__HELP__ = """
__**This command helps you to unmute a user in the chat**__
──「 **Usage** 」──
-> `unmute`
"""
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@RaiChUB.on_message(filters.group & filters.command("unmute",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def unmute(client, message):
    if message.chat.type in ["group", "supergroup"]:
        me_m =await client.get_me()
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Permission! To mute`")
         return
        can_mute= True
        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("some ooga booga")
                return
            try:
                await client.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=unmute_permissions,
                )
                await message.delete()
            except Exception as e:
                await message.edit_text("`Error!`\n" f"**Log:** `{e}`")
                return
        else:
            await message.edit_text("denied_permission")
    else:
        await message.delete()
