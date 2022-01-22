import platform
import re
import socket
import sys
import time
import uuid
from datetime import datetime
from os import environ, execle, path, remove

import psutil
from pyrogram import __version__
from pyrogram import filters
from RaiChUB import RaiChUB , vr , Adminsettings
__MODULE__ = "System"
__HELP__ = """**This command helps you to Bot System**
-> `sysinfo` `restart`
"""

@RaiChUB.on_message(filters.command("sysinfo",vr.get("HNDLR")) & filters.user(Adminsettings))
async def pijhaau(_ , message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = round(psutil.virtual_memory().total)
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(RaiChUB.workdir)
    psutil.disk_io_counters()
    disk = f"{du.used} / {du.total} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    res = f"""**System Info**
    
**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatFork - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**Hostname :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
    """
    await message.edit_text(res)
@RaiChUB.on_message(filters.command("restart",vr.get("HNDLR")) & filters.user(Adminsettings))
async def pijgsku(_ , message):
    await message.edit_text("` Restarting... 🤯🤯`")
    args = [sys.executable, "-m", "RaiChUB"]
    execle(sys.executable, *args, environ)
    exit()
    return

