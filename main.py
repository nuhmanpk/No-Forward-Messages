import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOTUSERNAME

bughunter0 = Client(
     os.environ.get("SESSION_NAME", "No-Forward-Messages"),
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

START_MSG = """👋Hey {}

Simple Telegram Bot to Automatically delete Forwarded messages  in Group.

Maintained By @BugHunterBots
"""

START_BUTTON = InlineKeyboardMarkup([[
InlineKeyboardButton(text="➕️Add Me To Your Chat", url=f"http://t.me/{BOTUSERNAME}?startgroup=botstart")
]]
)

@bughunter0.on_message(filters.private & filters.command("start"))
async def start_handler(bot, update):
    await update.reply_text(
        text=f"""{START_MSG}""".format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
  )


@bughunter0.on_message(filters.forwarded)
async def forward(bot, message):
	await message.delete()

	
bughunter0.run()
