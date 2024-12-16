
import os
from telehook import TeleClient, logger

# Configure the bot token and webhook URL
BOT_TOKEN = "8186222249:AAEh0MnDoUYzKvo2p1J97JabgHsoIN6v9nE"
WEBHOOK_URL = "https://pup-solid-publicly.ngrok-free.app/"

# Initialize TeleHook with the plugins folder
TeleHook = TeleClient(
    token=BOT_TOKEN,
    url=WEBHOOK_URL,
    plugins={"root": "bot.plugins"}
)

LOGGER = logger