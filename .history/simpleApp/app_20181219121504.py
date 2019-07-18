import uuid

def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app


