# © @DKBOTZHELP Or https://github.com/DKBOTZHELP

from datetime import datetime
from sys import version_info
from time import time
from dkbotz.Duration import TimeFormatter
from pyrogram import Client, filters
from dkbotz.humanbytes import humanbytes
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs import Config


@Client.on_message((filters.photo) & ~filters.channel)
async def help(client: Client, message: Message):
    if message.document:
       media = message.document
    if message.video:
       media = message.video
    if message.audio:
       media = message.audio
    if message.photo:
       media = message.photo

    text = ""

    text = "**🎢 Photo Details:**\n\n"
    text += f"__✏️ **Caption** : __ `{message.caption}`\n\n" if message.caption else ""
    text += f"🔰 __**Width** :__ `{media.width}`\n\n" if media.width else ""
    text += f"⭕ __** Height **:__ `{media.height}`\n\n" if media.height else ""
    text += f"📊 __** File Size** :__ `{humanbytes(media.file_size)}`\n\n" if media.file_size else ""
    text += f"**__**꧁༒༺☠︎☬ S҉₳𝖀𝕽₳V҉☠︎☬༒꧂**:__ **@Saurav3BV6SA9LLElon7Musk**\n\n
    text += f"__**ꉓ𝕺ค**:__ **@ANKIT3690**\n\n"
    text += f"**Generated By @{Config.BOT_USERNAME}**\n\n"
    
    await message.reply_text(text, quote=True)

