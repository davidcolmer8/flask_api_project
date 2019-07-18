from flask import Flask
from books import book

def create_app():
    app = Flask('bookStore')
    
    return app


