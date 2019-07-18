from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    UUID
    return uuid.uuid4()