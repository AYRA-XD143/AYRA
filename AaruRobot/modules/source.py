from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from AaruRobot import pbot as client


Aaru = "https://telegra.ph/file/6ccab5bc360325388e2c4.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Ayra,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴀᴀʀᴜ ✘ ʀᴏʙᴏᴛ-🇮🇳](t.me/MISS_AARU_X_ROBOT)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [❛-𝐌𝐑'𝐁𝐀𝐍𝐍𝐀 🚬 𝐊𝐈𝐍𝐆-𝐱𝐃 ° ](tg://user?id=5489344295)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴀᴀʀᴜ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5489344295"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/BANNA-XD143/AaruRobot")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
