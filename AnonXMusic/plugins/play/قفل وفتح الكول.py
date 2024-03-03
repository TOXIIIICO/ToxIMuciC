import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import get_assistant

@app.on_message(filters.video_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "تم فتح الكول"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "تم قفل الكول"
      await message.reply_text(Enddd)

@app.on_message(filters.video_chat_members_invited)
async def mevegaa(client: Client, message: Message): 
           text = f" قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass