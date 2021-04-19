# Support Channel @Vckyouuu

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), Saya Bot Pengunduh Lagu 🎵

Ketik/Telan /help untuk mengetahui perintah saya

By @Vckyouuu
"""

help_text = """
Perintah saya👇

- /lagu <nama lagu>: unduh lagu melalui Youtube
- /saavn <nama lagu>: mengunduh lagu melalui JioSaavn
- /deezer <nama lagu>: mengunduh lagu melalui Deezer
- Kirim url youtube ke pm saya untuk mendownload music yang anda minta
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Group Support", url="https://t.me/GrupMusik"
                    ),
                    InlineKeyboardButton(
                        text="Owner", url="https://t.me/VckyouuBitch"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("Geez Music Sudah Online!")
idle()
