import flask
import os.path
import random
from app.databaser import *
from flask import *

app = flask.Flask(__name__)

def getRandTemp():
    return f"{random.randrange(40,95)}°c"

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/messages')
def messages():
    name = request.args.get('n')
    if name is not None:
        name = name[0:16]
        return render_template('messages.html', messages = get_messages(), name=name)
    else:
        return redirect("/")

@app.route('/sendmsg/<name>')
def send_message(name):
    inputtext = request.args.get('txt')
    create_message(name, inputtext)
    return redirect(f"/messages?n={name}")

def start(ip):
    app.run(host=ip)