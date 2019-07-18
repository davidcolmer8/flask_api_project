from flask import Flask, jsonify, request
import uuid

def create_app():
    app = Flask(__name__)
    
    
    return app