import asyncio
from datetime import datetime
from pyrogram import filters 
from kingbot import kingbot, setbot , vr, Adminsettings
 
import re
from sql_helper.afk import check_fk, go_fk, no_fk
afk_sanity_check: dict = {}
__MODULE__ = "Afk"
__HELP__ = """
-> `afk`
__**This command helps you to check wether userbot is afk**__
"""
async def is_afk_(f, client, message):
    af_k_c = await check_fk()
    if af_k_c:
        return bool(True)
    else:
        return bool(False)


is_afk = filters.create(func=is_afk_, name="is_afk_")


@kingbot.on_message(filters.user(Adminsettings) & filters.command("afk", vr.get("HNDLR")))
async def set_afk(client, message):
    sult= await message.edit_text("`Processing..`")
    msge = None  
    try:
      res = message.text
      res= res.split(" ",1)[1]
    except Exception:
      pass
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if res:
        msg = f"**The king is unavailable due to work 👀.** \n__He Going Afk Because Of__ `{res}`"
        await go_fk(afk_start, msge)
    else:
        msg = f"**I Am Busy And I Am Going Afk**."
        await go_fk(afk_start)
    await sult.edit(msg)


@kingbot.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & ~filters.edited
    & filters.incoming
)
async def afk_er(client, message):
    if not message:
        return
    if not message.from_user:
        return
    use_r = int(message.from_user.id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 3:
        await message.reply_text(
            "`I Told You 3 Times That The King is busy, Now you are gonna be ignored😑😑`"
        )
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 3:
        return
    lol = await check_fk()
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    message_to_reply = (
        f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`\n**Reason** : `{reason}`"
        if reason
        else f"I Am **[AFK]** Right Now. \n**Last Seen :** `{total_afk_time}`"
    )
    LL = await message.reply(message_to_reply)


@kingbot.on_message(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message):
    lol = await check_fk()
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(
        f"""__The King is Back Alive__\n**No Longer afk.**\n `I Was afk for:``{total_afk_time}`""",
    )
    asyncio.sleep(40)
    await kk.delete()
    await no_fk()
    afk_sanity_check: dict = {}
