from flask import Flask
import uuid
from simpleApplication.createUUID import createUUID

app = flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = createUUID
    print (id)
    print('ji')
    return id + 'hi'