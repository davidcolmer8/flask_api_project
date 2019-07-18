from flask import Flask, jsonify 
import uuid


app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id=jsonify(uuid.uuid1())
    jsonDATAdata = {"uuid":id}
    return data 