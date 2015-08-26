from flask import render_template
from app import app
from random import randint

@app.route('/')
@app.route('/index')
def index():
    title = 'oh shit'
    ran = [str(randint(0,9)) for i in range(20)]
    return render_template('index.html',
                           title=title)

@app.route('/fuck')
def fuck():
    return 'fuck you'
