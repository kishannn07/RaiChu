from pyrogram import filters, Client
from RaiChUB import RaiChUB, Adminsettings,vr, starttimer, HNDLR
from datetime import datetime

__MODULE__ = "PING"
__HELP__ = """
__**This command helps you to instantly get the ping of the userbot**__
──「 **Usage** 」──
-> `ping`
"""
@RaiChUB.on_message(filters.command("ping",("HNDLR")) & filters.user(Adminsettings))
async def pinger(_, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.edit_text(
        f"**🏓 Pong!!**\n**🛠️ Server** `{ms}` \n`YEAH, YOUR BOT IS PERFORMING WELL`",
    )
