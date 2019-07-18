from flask import Flask

from . import trades
def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app


