import flask, flask.views
from flask import render_template, request
from flask import session, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import os
import time

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefqwefe2323234dvsv'

class Convo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(30))
    message = db.Column(db.String(140))
    created_at = db.Column(db.String(10))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session:
        return redirect('/loginpage')
    messages=Convo.query.all()
    return flask.render_template('index.html',messages=messages)

@app.route('/loginpage', methods=['GET', 'POST'])
def login_page():
    return flask.render_template('login.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    sender = 'Jasper'
    message = flask.request.form.get('message')
    create = time.strftime('%b %d, %H:%S %p')
    a = Convo(sender=sender, message=message, created_at=create);
    db.session.add(a)
    db.session.commit()
    messages=Convo.query.all()
    return flask.render_template('send.html',messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get("username", "alternate_default_value")
    password = request.form.get("password", "alternate_default_value")
    print username
    print password
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        messages=Convo.query.all()
        return flask.render_template('index.html',messages=messages)
    return redirect('/loginpage')




@app.route('/db/rebuild', methods=['GET', 'POST'])
def rebild_database():
    db.create_all()
    a = Convo(sender="Bot", message="Welcome to TamChat!", created_at='Nov 30 2:19 AM')
    db.session.add(a)
    db.session.commit()

    b = User(username="jasperbarcelona", password="jasper", first_name='Jasper', last_name='Barcelona')
    db.session.add(b)
    db.session.commit()

    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')

    # port=int(os.environ['PORT']), host='0.0.0.0'