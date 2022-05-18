# © @DKBOTZHELP Or https://github.com/DKBOTZHELP


import os
import urllib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs import Config
#from dkbotz.command import command Not Required

@Client.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
    await cmd.reply_text(
        f"""**Hello {cmd.from_user.mention}**

**I Am Most Powerful Media Info Bot Created By The ꉓ𝕺ค.**

**Use Me To Generate Infomation Of Media Like Photo, Videos And Document.**

**I Also Work in Group**""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('➕ Add Me To Your Group ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐔𝐋𝐓𝐈𝐕𝐄𝐑𝐒𝐄 ', url='http://t.me/defenderofthemultiverse'),
            InlineKeyboardButton('𝓽ꫝꫀ ᥴ𝘳ꫀꪖ𝓽ꪮ𝘳 ꪮᠻ ꪖꪶꪶ', url=f'http://t.me/{Config.SUPPORT_GROUP}')
            ],[
            InlineKeyboardButton('ꉓ𝕺ค', url='https://t.me/ANKIT3690'),
            InlinekeyboardButton('꧁༒༺☠︎☬ S҉₳𝖀𝕽₳V҉☠︎☬༒꧂', url='https://t.me/Saurav3BV6SA9LLElon7Musk')
            ],[
            InlineKeyboardButton('⌦ Close The Menu ⌫', callback_data='close_data')
        ]]
        ),
     disable_web_page_preview=True
    )
