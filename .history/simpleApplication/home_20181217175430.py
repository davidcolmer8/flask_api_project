from flask import Flask
from simpleApplication.createUUID import createUUID

import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = createUUID
    id.urn
    return id + 'hi'