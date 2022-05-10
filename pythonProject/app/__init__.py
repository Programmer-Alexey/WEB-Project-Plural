import datetime

from flask import Flask
from data import db_session
from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
from data.usersmodel import User
from data.newsmodel import News
from sqlalchemy import orm
# from flask import session


def add_to_db(obj):
    db_sess = db_session.create_session()
    db_sess.add(obj)
    db_sess.commit()


def create_user(name, about, email):
    user = User()
    user.name = name
    user.about = about
    user.email = email
    return user


def create_news(title, content, user_id, is_private=False):
    news = News(title=title, content=content,
                user_id=user_id, is_private=is_private)
    return news


app = Flask(__name__)
#app.app_context().push()
#app.config['SECRET_KEY'] = '5UP3R_53CR3T_K37'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'





from app.views import *

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)