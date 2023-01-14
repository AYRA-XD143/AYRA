import random
from pyrogram import __version__ as pyrover
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from AaruRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from AaruRobot.events import register
from AaruRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/99911b42bef56a2545ba4.jpg",
    "https://telegra.ph/file/38aacaa806d942f1fa2a9.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴀʏʀᴀ ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [⏤͟͟͞͞x𝐃🥀| 𓆩 𝐂𝐎𝐃𝐄𝐑 𓆪 |∘𖣘︎⃞⃟🔥°](https://t.me/YoungFaiz)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/Miss_Ayra_bot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/ayrabots"),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
  
  ##AARU ALIVE MOD
