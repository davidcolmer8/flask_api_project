from flask import Flask, jsonify, request
from flasgger import Swagger
from 

def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    swagger = Swagger(app)

    return app




