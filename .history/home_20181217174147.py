from flask import Flask
import uuid
from flask import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = str(uuid.uuid4)
    resp = jsonify(id)
    return id