

from bot import TeleHook
from telehook import Filters


@TeleHook.on_message(Filters.command('start'))
def start_cmd(client, message):
    name = message.from_user.first_name
    message.reply_text('Hello')
