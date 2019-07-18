from flask import Flask, jsonify 
import json
from uuid import UUID


app = Flask(__name__)

@app.route('/ss')
def home():
    return 'server is running'

@app.route('/')
def getUUID():
    UUIDcreateUUID
    return id + 'hi'

class UUIDEncoder(json.JSONEncoder):
    def createUUID(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)