
import os
from telehook import TeleClient

# Configure the bot token and webhook URL
BOT_TOKEN = ""
WEBHOOK_URL = ""

# Initialize TeleHook with the plugins folder
TeleHook = TeleClient(
    token=BOT_TOKEN,
    url=WEBHOOK_URL,
    plugins={"root": "bot.plugins"}
)
