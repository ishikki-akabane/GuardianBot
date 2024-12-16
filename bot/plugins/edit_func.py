from bot import TeleHook
from telehook import Filters


@TeleHook.on_edited(Filters.group)
def handle_private_edit(bot, message):
    message.reply_text(f"Edited message in private chat: {message.text}")
    