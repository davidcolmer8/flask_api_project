from flask import Flask
from .bookStore import books

def create_app():
    app = Flask('bookStore', static_folder=None)
    return app



