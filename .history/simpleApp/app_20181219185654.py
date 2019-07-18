from flask import Flask, jsonify, request
import uuid
from flasgger import Swagger

def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    swagger = Swagger(app)

   

    return app




