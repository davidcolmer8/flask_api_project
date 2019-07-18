from flask import Flask
from .bookstore import books

def create_app():
    app = Flask('bookStore')
    
    return app


