import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app  

ABHI = [
"https://graph.org/file/7b053a55193351974f7f1.jpg",
"https://graph.org/file/8386a5aa07dddcf5bb185.jpg,
]

NYKAA = [
    "https://graph.org/file/8386a5aa07dddcf5bb185.jpg",
    "https://graph.org/file/7b053a55193351974f7f1.jpg",       
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖\n\n"
               
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {message.chat.title}\n"
                f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {message.chat.id}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{message.chat.username}\n"
                f"● ɢʀᴏᴜᴘ ʟɪɴᴋ ➥ {link}\n"
                f"● ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➥ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➥ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(ABHI), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❖ <b>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</b> ❖\n\n● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {title}\n\n● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat_id}\n\n● ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➥ {remove_by}\n\n❖ ʙᴏᴛ ɴᴀᴍᴇ ➥ Kɪʟʟᴇʀ Mᴜsɪᴄ"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NYKAA), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#welcome

