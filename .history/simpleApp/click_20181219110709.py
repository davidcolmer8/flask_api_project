import click
from flask.cli import FlaskGroup
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp()

def cli():
    """start click and app
    """


