from flask import Flask

from . import
def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app


