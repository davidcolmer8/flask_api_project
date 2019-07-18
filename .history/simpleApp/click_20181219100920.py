import click
from flask.cli import FlaskGroup
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp(cli=True)

@click.group()
def cli():
    """start click and app
    """

