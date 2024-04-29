from app import app


@app.route('/')
@app.route('/index')
def login():
    return ('Hello, World!')
