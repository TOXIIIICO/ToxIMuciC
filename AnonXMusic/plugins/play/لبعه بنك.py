

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint




@app.on_message(filters.command(["مهدي","المهدي","مطور السورس"], ""), group=666)
async def kas(client, message):
    usr = await client.get_chat("MHWOn")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"ɴᴀᴍᴇᚐ: {name}\nᴜsᴇʀᚐ: @{usr.username}\nɪᴅᚐ: `{usr.id}`\nʙɪᴏᚐ: {usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )