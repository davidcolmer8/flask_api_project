from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/ss')
def home():
    return 'server is running'

@app.route('/')
def getUUID():
    id = jsonify(uuid.uuid1)
    return id + 'hi'