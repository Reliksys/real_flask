from flask import render_template, redirect

from app import app
from app.forms import LoginForm


def get_db_connection(user, password):
    try:
        # Переменные для глобального использования
        global user_login
        global user_password
        user_login = user
        user_password = password

        # Указываем параметры подключения
        conn_param = f'host=server.ru port=1234 dbname=mydb user={user} password={password}'

        # Создаем подключение и включаем автокомит
        conn = pg.connect(conn_param)
        conn.autocommit = True

        return conn
    except pg.OperationalError:
        # В случае ошибки выводим сообщение
        print("EGOOOOOOOOOOOOOOOOOOOR:", pg.OperationalError)
        return 0


@app.route('/')
@app.route('/index')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)
