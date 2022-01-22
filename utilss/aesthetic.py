from kingbot import kingbot, vr, Adminsettings
from pyrogram import filters

PRINTABLE_ASCII = range(0x21, 0x7f)
__MODULE__ = "Ae"
__HELP__ = """**This command helps you to AE**
-> `ae`
"""


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@kingbot.on_message(filters.command("ae",vr.get("HNDLR")) & filters.user(Adminsettings))
async def porari(_, message):
    text = message.text
    text = text.split(" ",1)[1]
    text = "".join(aesthetify(text))
    await message.edit(text)
   
