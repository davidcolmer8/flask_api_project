from flask import Flask

from . import trade
def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app


