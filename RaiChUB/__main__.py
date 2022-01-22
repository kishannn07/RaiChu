
import asyncio
import importlib
import sys
import time
import traceback
from pyrogram import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto
from pyrogram import filters 
# import RaiChUB
from RaiChUB import RaiChUB ,setbot , get_bot , get_self, vr ,Adminsettings, vcbot
from assistant import ALL_AST
from adminss import ALL_ADMINN
from utilss import ALL_UTILS
from ownerr import ALL_OWN
from RaiChUB.plugins import ALL_INB
from uti.serra import ser
from uti.confi import Var
loop = asyncio.get_event_loop()
HNDLR="."
BOT_RUNTIME = 0
HELP_COMMANDU = {}
HELP_COMMANDA = {}
HELP_COMMANDO = {}
HELP_COMMANDAST = {}
HELP_COMMANDS = {}
async def get_runtime():
    return BOT_RUNTIME

async def reload_userbot():
    await RaiChUB.start()
    for modul in ALL_MODULES:
        imported_module = importlib.import_module("utilss." + modul)
        imported_module = importlib.import_module("ownerr." + modul)
        imported_module = importlib.import_module("adminss." + modul)
        importlib.reload(imported_module)


async def reinitial_restart():
    await get_bot()
    await get_self()


async def reboot():
    importlib.reload(importlib.import_module("adminss"))
    importlib.reload(importlib.import_module("ownerr"))
    importlib.reload(importlib.import_module("utilss"))
    importlib.reload(importlib.import_module("assistant"))
    # await setbot.send_message(Owner, "Bot is restarting...")
    await setbot.restart()
    await RaiChUB.restart()
    await reinitial_restart()
    # Reset global var
    BOT_RUNTIME = 0
    HELP_COMMANDU = {}
    HELP_COMMANDA = {}
    HELP_COMMANDO = {}
    HELP_COMMANDAST = {}
    # Assistant bot
    
    for modul in ALL_UTILS:
        imported_module = importlib.import_module("utilss." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDU:
                HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modula in ALL_ADMINN:
        imported_module = importlib.import_module("adminss." + modula)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDA:
                HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modulst in ALL_OWN:
        imported_module = importlib.import_module("ownerr." + modulst)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDO:
                HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modula in ALL_AST:
            imported_module = importlib.import_module("assistant." + modul)
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                if not imported_module.__MODULE__.lower() in HELP_COMMANDAST:
                    HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
                else:
                    raise Exception("Can't have two modules with the same name! Please change one")
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
            importlib.reload(imported_module)
    HELP_COMMANDS = {**HELP_COMMANDA,**HELP_COMMANDU,**HELP_COMMANDO, **HELP_COMMANDAST}
# await setbot.send_message(Owner, "Restart successfully!")

async def restart_all():
    # Restarting and load all plugins
    asyncio.get_event_loop().create_task(reboot())


RANDOM_STICKERS = ["CAADAgAD6EoAAuCjggf4LTFlHEcvNAI", "CAADAgADf1AAAuCjggfqE-GQnopqyAI",
                   "CAADAgADaV0AAuCjggfi51NV8GUiRwI"]


async def except_hook(errtype, value, tback):
    sys.__excepthook__(errtype, value, tback)
    errors = traceback.format_exception(etype=errtype, value=value, tb=tback)
    button = InlineKeyboardMarkup([[InlineKeyboardButton("🐞 Report bugs", callback_data="report_errors")]])
    text = "An error has accured!\n\n```{}```\n".format("".join(errors))
    if errtype == ModuleNotFoundError:
        text += "\nHint: Try this in your terminal `pip install -r requirements.txt`"
    await setbot.send_message(Owner, text, reply_markup=button)


async def reinitial():
    await RaiChUB.start()
    await setbot.start()
    await get_self()
    await get_bot()
    await RaiChUB.stop()
    await setbot.stop()


async def start_bot():
    global BOT_RUNTIME, HELP_COMMANDS, HELP_COMMANDU, HELP_COMMANDA, HELP_COMMANDO, HELP_COMMANDAST
    # sys.excepthook = except_hook
    vr.set("Owne", Var.OWNER_ID)
    print("----- Checking user and bot... -----")
    await reinitial()
    print("----------- Check done! ------------")
    # Assistant bot
    if vcbot:
        vcbot.start()
    await setbot.start()
    await RaiChUB.start()
    HELP_COMMANDU = {}
    HELP_COMMANDA = {}
    HELP_COMMANDO = {}
    HELP_COMMANDAST = {}
    for modul in ALL_UTILS:
        imported_module = importlib.import_module("utilss." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDU:
                HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module.__HELP__
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module.__HELP__
    for modula in ALL_ADMINN:
        imported_module = importlib.import_module("adminss." + modula)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDA:
                HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module.__HELP__
    for modulst in ALL_OWN:
        imported_module = importlib.import_module("ownerr." + modulst)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDO:
                HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module.__HELP__
    for moduli in ALL_AST:
            imported_module = importlib.import_module("assistant." + moduli)
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                if not imported_module.__MODULE__.lower() in HELP_COMMANDAST:
                    HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
                else:
                    raise Exception("Can't have two modules with the same name! Please change one")
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module.__HELP__
    for moduloo in ALL_INB:
        imported_module = importlib.import_module("RaiChUB.plugins." + moduloo)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDO:
                HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module.__HELP__
    if vcbot is not None:
         rni= vcbot.run
    ser.HU=HELP_COMMANDU
    ser.HA=HELP_COMMANDA
    ser.HO=HELP_COMMANDO
    ser.HAT=HELP_COMMANDAST
    HELP_COMMANDS = {**HELP_COMMANDA,**HELP_COMMANDU,**HELP_COMMANDO, **HELP_COMMANDAST}
    ser.HC=HELP_COMMANDS
    await idle()
if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    loop.run_until_complete(start_bot())

