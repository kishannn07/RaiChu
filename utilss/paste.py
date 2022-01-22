from pyrogram import client, filters
import asyncio
import time
import os
import requests
from pyrogram.types import ChatPermissions , Message
from kingbot import kingbot, vr ,Adminsettings
__MODULE__ = "paste"
__HELP__ = """
__**This command helps you to paste a text to nekobin.com and return a shareable url**__
──「 **Usage** 」──
-> `paste`
"""
def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
@kingbot.on_message(filters.command("paste",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def paste(client,message):
    rep = await message.edit_text("`Please Wait.....`")
    tex_t = get_text(message)
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await rep.edit("`Reply To File / Give Me Text To Paste!`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": message_s})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    raw = f"https://nekobin.com/raw/{key}"
    reply_text = f"Pasted Text To [NekoBin]({url}) And For Raw [Click Here]({raw})"
    await rep.edit(reply_text)
