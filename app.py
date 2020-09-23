import os
import telegram
from flask import Flask, request
from resources.credentials import bot_token, URL
from resources.db import db, insert_data
from resources.utils import validate_data
from flask_sqlalchemy import SQLAlchemy


global TOKEN
global bot
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="igormbq",
    password="bancodedados",
    hostname="igormbq.mysql.pythonanywhere-services.com",
    databasename="igormbq$fizzbuzzdb",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # Retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

   # Extract data from message
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()

    # Execute fizzbuzz logical
    response = validate_data(text)

    # Insert of message and response into DB
    insert_data(text, update)
    insert_data(response, update)

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
    port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True)

# DB FINISH
#
# @app.message_handler(commands=['start'])
# def start():
#     update = telegram.Update.de_json(request.get_json(force=True), bot)
#     chat_id = update.message.chat.id
#     msg_id = update.message.message_id
#
#     bot.sendMessage(chat_id=chat_id, text='Hello, welcome to test FizzBuzz!', reply_to_message_id=msg_id)
