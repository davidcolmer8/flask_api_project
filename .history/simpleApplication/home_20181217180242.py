from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/ss')
def home():
    return 'server is running'

@app.route('/')
def getUUID():
    id=str(uuid.uuid4)
    return id +hi