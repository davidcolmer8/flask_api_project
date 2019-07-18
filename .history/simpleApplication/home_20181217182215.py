from flask import Flask, jsonify 
import json
import uuid


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id=str(uuid.uuid1())
    jsonID = id.
    return id