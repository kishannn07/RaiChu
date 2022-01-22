from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from RaiChUB import RaiChUB, vr ,Adminsettings
__MODULE__ = "speedtest"
__HELP__ = """
__**This command helps you to get speed of your connection**__
──「 **Usage** 」──
-> `speedtest`
"""

@RaiChUB.on_message(filters.command("speedtest",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def speedtest(_ , message):
    await message.reply("Processing ...")
    import speedtest
    download = speedtest.Speedtest().download()
    upload = speedtest.Speedtest().upload()
    download=round(download/(1024*1024) , 2)
    upload=round(upload/(1024*1024) , 2)
    await message.reply(f"Downloading speed : {download}Mbps \n Uploading speed : {upload}Mbps")
