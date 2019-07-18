from flask import Flask
from . import 

def create_app():
    app = Flask(__name__)
    
    return app