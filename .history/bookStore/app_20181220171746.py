from flask import Flask

def create_app():
    app = Flask('bookStore')
    
    return app

from bookstore import books

