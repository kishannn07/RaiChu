from pyrogram import client, filters
import asyncio
import time
from googlesearch import search
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "ytlink"
__HELP__ = """
__**This command helps you to get youtube link**__
──「 **Usage** 」──
-> `ytlink`
"""

@RaiChUB.on_message(filters.command("ytlink",vr.get("HNDLR")) & filters.user(Adminsettings))  
def youtube_link(_,message):
    msg_txt=message.text
    if " " in msg_txt:
        query=msg_txt[msg_txt.index(" ")+1:len(msg_txt)]
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            if "youtube" in j: 
                message.reply(j)
                break
        else:
            message.reply("Can't search the whole internet !")
    else:
        message.reply("Shall I search How to be stupid ?")
