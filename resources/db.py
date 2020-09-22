from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200))
    telegram_id = db.Column(db.String(4096), unique=True, nullable=False)
    messages = db.relationship('Message', backref='user', lazy=True)


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(4096))
    chat_id = db.Column(db.String(4096))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def insert_data(text, msg_id, update):
    # existUser = User.query.filter_by(telegram_id=update.message.chat.id)
    message = Message(text=text, chat_id=msg_id)
    user = User(first_name=update.message.chat.first_name, telegram_id=update.message.chat.id)

    user.messages.append(message)
    db.session.add(user)
    db.session.add(message)
    db.session.commit()