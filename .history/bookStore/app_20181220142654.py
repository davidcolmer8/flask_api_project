from flask import Flask
from . import books

def create_app():
    app = Flask('bookStore')
    
    return app