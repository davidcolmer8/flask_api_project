from flask import Flask, jsonify 
import json
import uuid


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = UUIDEncoder.createUUID(uuid.uuid4)
    return id

class UUIDEncoder(json.JSONEncoder):
    def createUUID(self, obj):
        return json.JSONEncoder.default(self, obj)

def createUUID():
    return uuid.uuid