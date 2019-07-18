from flask import Flask
from . import books
s
def create_app():
    app = Flask('bookStore', static_folder=None)
    return app



