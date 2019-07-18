from flask import Flask
from . import books

def create_app():
    app = Flask('book'__name__'')
    
    return app