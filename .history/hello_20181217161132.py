from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    str(UUID) = uuid.uuid4()
    return s