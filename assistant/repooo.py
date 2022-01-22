from pyrogram import filters 
from RaiChUB import RaiChUB, setbot , vr, Adminsettings
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultArticle,InputTextMessageContent
__MODULE__ = "Repo"
__HELP__ = """**This command helps you to Repo**
-> `repo`
"""

HNDLR="."

@RaiChUB.on_message(filters.user(Adminsettings) & filters.command("repo",HNDLR))
async def hikjbhgakd(_, message):
  booet= await setbot.get_me()
  res=await RaiChUB.get_inline_bot_results(booet.username, "repo")
  mg= await RaiChUB.send_inline_bot_result(message.chat.id, res.query_id, res.results[0].id)
  message.delete()
@setbot.on_inline_query(filters.regex("repo"))
async def ibnrp(_ , inline_query):
  stosen= InputTextMessageContent(message_text=f"𝙂𝙚𝙩 𝙮𝙤𝙪𝙧𝙨𝙚𝙡𝙛 𝙖 𝙍𝙖𝙞𝘾𝙝𝙐𝘽\n 𝐿𝑖𝑔ℎ𝑡 𝑦𝑒𝑎𝑟𝑠 𝑎ℎ𝑒𝑎𝑑")
  keboard= InlineKeyboardMarkup(
                  [  [
                        InlineKeyboardButton(
                            "🔥Repo",
                            url= "https://github.com/ProXSammY/RaiChu"
                        )
                      ]])
  await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Feel like a RaiChu",
                input_message_content=stosen,
                thumb_url="https://telegra.ph/file/d19f785fb32bf4eaa62fd.jpg",
                reply_markup=keboard,
            ),
        ]
    )
