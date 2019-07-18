from flask import Flask, jsonify 
import uuid


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    data = {"uuid"}

    id=jsonify(uuid.uuid1())
    data = id
    return data 