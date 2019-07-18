from flask import Flask
import uuid
from simpleApplication.createUUID import createUUID

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = createUUID
    print(id)
    return id