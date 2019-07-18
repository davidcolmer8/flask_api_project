from flask import Flask, jsonify 
import uuid
# import json


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    return buildJSON()

def createID():
    return uuid.uuid1()

def buildJSON():
    json=jsonify({"id": createID()})
    return json