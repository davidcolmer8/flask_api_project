from flask import Flask, jsonify 
import json
from uuid import UUID


app = Flask(__name__)

@app.route('/ss')
def home():
    return 'server is running'

@app.route('/')
def getUUID():
    id = UUIDEncoder.createUUID()
    return id

class UUIDEncoder(json.JSONEncoder):
    def createUUID(self, obj):
        return json.JSONEncoder.default(self, obj)