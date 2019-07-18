from flask import Flask, jsonify, request
import uuid
import click

def create_app():
    app = Flask(__name__)
    
    
    return app