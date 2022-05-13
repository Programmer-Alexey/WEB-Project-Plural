from app import app
from app.data import db_session


if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/database.db")
    app.run(port=8000)
