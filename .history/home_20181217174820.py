from flask import Flask, jsonify
import uuid
from 

app = Flask(__name__)

@app.route('/')
def home():
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = 
    return id