#!/./bin/bash
# This script installs flask and its dependencies
# first run python -m venv flask to set up virtual environment
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install flipflop
flask/bin/pip install coverage
mkdir app
mkdir app/static
mkdir app/templates
mkdir tmp
touch app/__init__.py
echo "from flask import Flask

app = Flask(__name__)
from app import views" >> app/__init__.py
touch app/views.py
echo "from app import app

@app.route('/')
@app.route('/index')
def index():
    return ''" >> app/views.py
touch app/templates/index.html
echo "{% extends "base.html" %}
{% block content %}
{% endblock %}" >> app/templates/index.html
touch app/templates/base.html
touch run.py
chmod a+x run.py
echo "#!flask/bin/python
from app import app
app.run(debug=True)" >> run.py
touch config.py
echo "import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = 'temp-key'" >> config.py
