from flask import Flask, jsonify
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = str(uuid.uuid4)
    resp = jsonify(id)
    return id