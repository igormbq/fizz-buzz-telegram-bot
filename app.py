import os
import telegram
from flask import Flask, request
from resources.credentials import bot_token, URL
from resources.db import insert_data
from resources.utils import validate_data

app = Flask(__name__)

global TOKEN
global bot
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # response = validate_data(text)
    # insert_data(response, msg_id, update)
    bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    set_webhook()
    return "It's working"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# DB FINISH
#
# @app.message_handler(commands=['start'])
# def start():
#     update = telegram.Update.de_json(request.get_json(force=True), bot)
#     chat_id = update.message.chat.id
#     msg_id = update.message.message_id
#
#     bot.sendMessage(chat_id=chat_id, text='Hello, welcome to test FizzBuzz!', reply_to_message_id=msg_id)
