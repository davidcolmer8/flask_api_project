import click
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp(cli=True)

@click.group
def cli():
    """start click and app
    """


