import click
from flask.cli import FlaskGroup
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp()

@click.command()
@click.option('--start', type=bool, default=True)
def cli():
    """start click and app
    """

@click.commmand()

