import click
from flask.cli import FlaskGroup
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp()
    
@click.commmand
def cli():
    """start click and app
    """
    return startSimpleApp()

