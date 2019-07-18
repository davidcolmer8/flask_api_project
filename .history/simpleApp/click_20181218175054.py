import click
from simpleApp.main.home import startApp

def startSimpleApp():
    return startApp(cli=True)

@click.group(startApp=startSimpleApp())
def cli():
    """start click and app
    """

@cli.command("init")
def init(cli):
    click.echo('start app')

cli.add_command(init)
