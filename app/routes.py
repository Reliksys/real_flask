from flask import render_template, redirect

from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/templates/index')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)