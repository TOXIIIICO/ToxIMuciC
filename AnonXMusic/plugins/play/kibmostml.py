
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint



@app.on_message(filters.command(["غنيلي", "غني", "❤️‍🔥غنيلي", "غنيي"], ""), group=7885435500111)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/gukygn/{rl}"
    await client.send_voice(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار الاغـنـية لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )


@app.on_message(filters.command(["صوره", "❤️‍🔥صوره", "صورهه", "صور"], ""), group=78300088111)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار صوره لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )


@app.on_message(filters.command(["❤️‍🔥انمي", "انمي"], ""), group=7881140041)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار انمي لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )


@app.on_message(filters.command(["❤️‍🔥متحركه", "متحركه"], ""), group=7886005111)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار ملصق لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["❤️‍🔥اقتباسات", "اقتباس"], ""), group=788088678844555111)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار اقتباس لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["هيدرا", "❤️‍🔥هيدرات"], ""), group=78817667990011)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار هيدرات لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["❤️‍🔥صور بنات", "صور بنات"], ""), group=7881686688911)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار صوره لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["صور شباب", "❤️‍🔥صور شباب"], ""), group=7886768867111)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار صوره لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["❤️‍🔥قران", "قران"], ""), group=7888080808080111)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["❤️‍🔥الشيخ نقشبندي", "النقشبندي", "نقشبندي"], ""), group=788122345611)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["فيلم", "❤️‍🔥فيلم"], ""), group=788132244511)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,34)
    url = f"https://t.me/gyigkk/{rl}"
    await client.send_audio(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار فلم لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["استوري", "❤️‍🔥استوريهات"], ""), group=7877766611)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار استوري لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["تويته", "تويتات"], ""), group=7899981)
async def ihd(client: Client, message: Message):
    rl = random.randint(4,42)
    url = f"https://t.me/wffhvv/{rl}"
    await client.send_photo(message.chat.id,url,caption="ꨄ  ¦ تـم اختيـار تويت لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
