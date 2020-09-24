from flask import Flask, request
from resources.credentials import bot_token, URL
from resources.db import insert_data, DATABASE_URI
from resources.utils import fizz_buzz
from flask_sqlalchemy import SQLAlchemy
import telegram


global TOKEN
global bot
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # Retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    #Extract data from message
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()

    # Execute fizzbuzz logical
    response = fizz_buzz(text)

    # Insert message and response into DB
    insert_data(text, update, is_reply = 0)
    insert_data(response, update, is_reply = 1)

    # Sends the reply message to the user
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

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
    app.run(debug=True)