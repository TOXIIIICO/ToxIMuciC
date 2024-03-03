import asyncio
import requests
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.errors import PeerIdInvalid
from os import getenv
from AnonXMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from AnonXMusic.utils.database import (set_cmode,get_assistant) 
from AnonXMusic.utils.decorators.admins import AdminActual
from AnonXMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)


muttof = []
@app.on_message(filters.command(["قفل التقييد", "تعطيل التقييد"], ""), group=419)
async def muttlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in muttof:
        return await message.reply_text("تم معطل من قبل🔒")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقييد بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["فتح التقييد", "تفعيل التقييد"], ""), group=424)
async def muttopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in muttof:
        return await message.reply_text("التقييد مفعل من قبل ✅")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقييد بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")
        
        
@app.on_message(filters.command(["الغاء تقييد","الغاء التقييد"], ""), group=94) 
async def mute(client: Client, message: Message):
   global restricted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
    if message.chat.id in muttof:
      return   	   	
    await app.restrict_chat_member(
                       chat_id=message.chat.id,
                       user_id=message.reply_to_message.from_user.id,
                       permissions=unmute_permissions,
                   )
    await app.send_message(message.chat.id, f"✅ ¦ تـم الغاء الكتـم بـنجـاح\n {message.reply_to_message.from_user.mention} ")


restricted_users = []
@app.on_message(filters.command(["تقييد"], ""), group=62)
async def mute(client: Client, message: Message):
    global restricted_users
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.id == 6438745713:
            await app.send_message(message.chat.id, "عذرا لا يمكنك تقييد المطور")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=mute_permission,
            )
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await app.send_message(message.chat.id, f"✅ ¦ تـم الكتـم بـنجـاح\n {restricted_user.mention} ")

@app.on_message(filters.command(["مسح المقيدين"], ""), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    user_id = message.from_user.id
    count = len(restricted_users)
    for user in restricted_users:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user,
            permissions=unmute_permissions,
        )
        restricted_users.remove(user)
    await message.reply_text(f"↢ تم مسح {count} من المقيديد")
    

@app.on_message(filters.command(["المقييدين"], ""))
async def get_restr_users(client: Client, message: Message):
   global restricted_users
   count = len(restricted_users)
   user_ids = [str(user.id) for user in restricted_users]
   response = f"⌔ قائمة المقيدين وعددهم : {count}\n"
   response += "\n"
   response += "\n".join(user_ids)
   await message.reply_text(response)



gaaof = []
@app.on_message(filters.command(["تعطيل الحظر", "تعطيل الطرد"], ""), group=504)
async def gaalock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in gaaof:
        return await message.reply_text("تم معطل من قبل🔒")
      gaaof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الطرد و الحظر بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر"], ""), group=412)
async def gaaopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in gaaof:
        return await message.reply_text("الطرد و الحظر مفعل من قبل ✅")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")
        
banned_users = []
@app.on_message(filters.command(["حظر"], ""), group=39)
async def mute(client: Client, message: Message):
    global banned_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6438745713:
        return
    if message.chat.id in gaaof:
        return
    if message.reply_to_message.from_user.id == 6438745713:
        await app.send_message(message.chat.id, "عذرا لا يمكنك طرد المطور")
    else:
        banned_user = message.reply_to_message.from_user
        banned_users.append(banned_user)
        await app.ban_chat_member(message.chat.id, banned_user.id)
        await app.send_message(message.chat.id, f"✅ ¦ تـم الحظر بـنجـاح\n {banned_user.mention} ")

@app.on_message(filters.command(["مسح المحظورين"], ""), group=19)
async def unban_all(client: Client, message: Message):
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in banned_users.copy():
        user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المحظورين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين محظورين ليتم مسحهم")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المحظورين")
        
        
@app.on_message(filters.command(["الغاء حظر","/unban"], ""), group=42)
async def mute(client: Client, message: Message):
   global banned_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
    await app.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id) 
    banned_users.remove(user)
    await app.send_message(message.chat.id, f"✅ ¦ تـم الغاء الحظر بـنجـاح\n {message.reply_to_message.from_user.mention} ")


@app.on_message(filters.command(["المحظورين"], ""))
async def get_restricted_users(client: Client, message: Message):
   global banned_users
   count = len(banned_users)
   user_ids = [str(user.id) for user in banned_users]
   response = f"⌔ قائمة المحظورين وعددهم : {count}\n"
   response += "\n"
   response += "\n".join(user_ids)
   await message.reply_text(response)




muted_users = []
@app.on_message(filters.command(["كتم"], ""), group=39)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6438745713:
        return
    if message.reply_to_message.from_user.id == 6438745713:
        await app.send_message(message.chat.id, "عذرا لا يمكنك طرد المطور")
    else:	
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            if user_id not in muted_users:
                muted_users.append(user_id)
                await message.reply_text(f"العضو {user_id} تم كتمه بنجاح.")
            else:
                await message.reply_text(f"المستخدم محظور بالفعل")
        else:
            await message.reply_text("قم بعمل ريبلاي")

@app.on_message(filters.command(["الغاء الكتم"], ""), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:	
    user_id = message.reply_to_message.from_user.id
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f"تم الغاء كتم المستخدم {user_id}")
        
       
        
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and message.from_user.id in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    count = len(muted_users)
    user_ids = [str(user) for user in muted_users]
    response = f"⌔ قائمة المكتومين وعددهم : {count}\n"
    response += "\n"
    response += "\n".join(user_ids)
    await message.reply_text(response)


@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المكتومين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المكتومين")

   
@app.on_message(filters.command(["اطردني"], ""), group=268)
async def fire_user(client, message):
    await message.reply_text("اطلع برا اصلا مش عايزينك")
    await client.ban_chat_member(message.chat.id, message.from_user.id)




@app.on_message(filters.command(["البوتات"], "") & filters.group, group=56555)
async def list_bots(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    bot_usernames = []
    count = 0 
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            bot_usernames.append("@" + member.user.username)
            count += 1

    if count > 0:
        bot_list = "\n".join(bot_usernames)
        await message.reply_text(f"عدد البوتات في المجموعة: {count} \n يوزرات البوتات: {bot_list}")
    else:
        await message.reply_text("لا يوجد بوتات في المجموعة.")