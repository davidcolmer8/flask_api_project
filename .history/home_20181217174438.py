from flask import Flask, jsonify
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = uuid.uuid2
    resp = jsonify(id)
    return id