from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

""" 
Creates the URI that will be used to define app.config in the application
"""
DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="igormbq",
    password="bancodedados",
    hostname="igormbq.mysql.pythonanywhere-services.com",
    databasename="igormbq$fizzbuzzdb",
)


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
    is_reply = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def insert_data(text, update, is_reply):
    """
    This function checks if the user is already stored in the database,
    if true just save the message, if not then save the user and the message

    :param text: Message content.
    :param update: All data from telegram that we use some attributes.
    :param is_reply: 0 - If False it means that it's' a message sent by the user.
                     1 - If True is a bot response
    """
    exist_user = User.query.filter_by(telegram_id=update.message.chat.id).first()

    if exist_user:
        message = Message(text=text, user_id=exist_user.id, is_reply=is_reply)
    else:
        user = User(first_name=update.message.chat.first_name, telegram_id=update.message.chat.id)
        db.session.add(user)
        message = Message(text=text, user_id=user.id, is_reply=is_reply)
        user.messages.append(message)

    db.session.add(message)
    db.session.commit()