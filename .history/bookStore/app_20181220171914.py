from flask import Flask
from books import books

def create_app():
    app = Flask('bookStore')
    
    return app


