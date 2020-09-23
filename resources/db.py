from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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


def insert_data(text, update):
    """
    This function verify if theuser has been
    """
    existUser = User.query.filter_by(telegram_id=update.message.chat.id).first()

    if existUser:
        message = Message(text=text, chat_id=msg_id,user_id=existUser.id)


    else:
        user = User(first_name=update.message.chat.first_name, telegram_id=update.message.chat.id)
        db.session.add(user)
        message = Message(text=text, user_id=user.id)
        user.messages.append(message)

    db.session.add(message)
    db.session.commit()