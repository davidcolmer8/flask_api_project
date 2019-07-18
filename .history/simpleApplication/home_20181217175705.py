from flask import Flask
from simpleApplication.createUUID import createUUID

import uuid

app = Flask(__name__)

@app.route('/ss')
def home():
    return 'server is running'

@app.route('/')
def getUUID():
    return 'hi'