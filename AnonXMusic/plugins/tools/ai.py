import random
import time
import requests
from AnonXMusic import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

API_URL = "https://chatgpt.apiitzasuraa.workers.dev/"  # Replace with a reliable API endpoint

@app.on_message(filters.command(["chatgpt","ai","ask","gpt","solve"], prefixes=["+", ".", "/", "-", "", "$","#","&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "❖ ᴇxᴀᴍᴘʟᴇ ➥ /ask Where is TajMahal ?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            try:
                response = requests.get(f'{API_URL}?question={a}')
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

                # Check if "answer" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                         f"♥︎ {x}  \n\n❖ ᴀɴsᴡᴇʀɪɴɢ ʙʏ ➥ Kɪʟʟᴇʀ Mᴜsɪᴄ",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'answer' key found in the response.")
            except requests.exceptions.RequestException as e:
                await message.reply_text(f"Network error: {e}")
    except Exception as e:
        await message.reply_text(f"Error - {e}")