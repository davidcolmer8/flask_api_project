import click
from simpleApp.main.app import startApp

def startSimpleApp():
    return startApp(cli=True)

@click
def cli():
    """start click and app
    """


