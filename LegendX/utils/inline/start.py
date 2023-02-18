from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🍁 sᴜᴩᴩᴏʀᴛ 🍁", url=f"{config.SUPPORT_GROUP}"
            ),
            InlineKeyboardButton(
                text="✨ ᴜᴘᴅᴀᴛᴇ ✨", url=f"{config.SUPPORT_CHANNEL}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄️ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ❄️", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🥀 ᴍᴀɪɴᴛᴀɪɴᴇʀ 🥀", user_id=OWNER),
            InlineKeyboardButton(
                text="🕊️ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🕊️", url=f"https://telegra.ph/file/9b0455dae14d5639f936d.mp4"
            )
        ],
     ]
    return buttons
