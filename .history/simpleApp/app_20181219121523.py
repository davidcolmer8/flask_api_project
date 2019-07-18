from flask import Flask

from . import tra
def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app


