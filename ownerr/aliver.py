from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from kingbot import setbot, Adminsettings, kingbot, START_TIME , vr, vcbot
from datetime import datetime
import time
__MODULE__ = "alive"
__HELP__ = """
__**This command helps you to check wether userbot is alive**__
──「 **Usage** 」──
-> `alive`
"""
Alive_pic = "https://telegra.ph/file/664686c15a83ccf26239b.mp4"
@kingbot.on_message(filters.user(Adminsettings) & filters.command("alive",vr.get("HNDLR")))
async def gooe_search(client, message):
    start_time = time.time()
    uptime = (datetime.now() - START_TIME)
    reply_msg = f"**MADE IN 🇮🇳 , MADE WITH 😻**"
    reply_msg += "------------------\n\n"
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    reply_msg += f"🔸Pɪɴɢ Tɪᴍᴇ: **{ping_time}ms\n**"
    reply_msg += f"🔹Kɪɴɢ Uᴘᴛɪᴍᴇ: **{uptime}\n**"
    reply_msg += f"🔸Sᴜᴘᴘᴏʀᴛ: **@KingUserBots\n**"
    reply_msg += f"🔹Rᴇᴘᴏ: **[HERE](https://github.com/ToxicCybers/kinguserbot)\n**"
    reply_msg += f"🔸Pʏᴛʜᴏɴ: **3.8\n\n**"
    reply_msg += f"🍹Sᴇʀᴠᴇʀꜱ Fᴜɴᴄᴛɪᴏɴɪɴɢ Nᴏʀᴍᴀʟ🍹"
    await client.send_photo(message.chat.id , Alive_pic , reply_msg)
    await message.delete()
    if vcbot is not None:
        vcbot.send_message(message.chat.id, "Voice player alive")
