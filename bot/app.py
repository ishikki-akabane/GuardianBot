from flask import Flask, request
from bot import TeleHook, BOT_TOKEN
import requests

app = Flask(__name__)

@app.route("/")
def home_endpoint():
    return "Telegram Bot is running."

@app.route('/webhook', methods=['POST'])
def webhook_endpoint():
    try:
        update = request.get_json()
        TeleHook.process_update(update)      
    except Exception as e:
        print(e)
    return 'ok'

@app.route("/run")
def run_endpoint():
    result = TeleHook.setup_webhook()
    return result

TeleHook.load_plugins()
