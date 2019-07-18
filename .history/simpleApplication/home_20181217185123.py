from flask import Flask, jsonify 
import uuid
import json


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id=jsonify(uuid.uuid1())
    

    return y