from flask import Flask
from . import books

def create_app():
    app = Flask(''__name__'')
    
    return app