from flask import Flask, jsonify, request
from flasgger import Swagger

def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    swagger = Swagger(app)
    from simpleAp import home
    return app




