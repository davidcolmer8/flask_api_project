from flask import Flask, jsonify 
import json
import uuid


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = UUIDEncoder.encodeUUID(re)
    return id

class UUIDEncoder(json.JSONEncoder):
    def encodeUUID(self, obj):
        return json.JSONEncoder.default(self, obj)

def createUUIDs():
    return uuid.uuid4