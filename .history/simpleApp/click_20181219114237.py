import click
from flask.cli import FlaskGroup
from simpleApp.app import startApp

def startSimpleApp():
    return startApp(cli=True)

@click.group(cls=FlaskGroup)
def cli():
    """start click and app
    """


