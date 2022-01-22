from pyrogram import filters 
from RaiChUB import RaiChUB, setbot , vr, Adminsettings
from pyrogram.errors import UserPrivacyRestricted


@RaiChUB.on_message(filters.user(Adminsettings) & filters.command("inviteall", vr.get("HNDLR")))
async def hikjgakd(_, message):
    mg=await message.edit_text("Roaring up")
    idoun= message.text
    idoun= idoun.split(None,1)[1]
    try:
       trgt= int(idoun)
    except Exception:
       trgt = idoun.strip()
       if trgt.startswith("@"):
          trgt= trgt[1:]
       else:
          trgt= idoun.strip()
    i=0
    async for memb in RaiChUB.iter_chat_members(trgt):
      membe= memb.user
      membid= membe.id
      await mg.edit(f"trying to add{membe.mention}")
      try:
        await RaiChUB.add_chat_members(message.chat.id, membid)
        i= i+1
      except UserPrivacyRestricted:
        continue
      except Exception as e:
           await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
           return
    await mg.edit(f"The hunt was successful. Got total {i} users")
