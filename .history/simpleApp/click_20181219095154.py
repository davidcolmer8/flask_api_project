import click
from flask.cli import FlaskGroup
from simpleApp.a.home import startApp

def startSimpleApp(info):
    return startApp(cli=True)

@click.group(cls=FlaskGroup, startApp=startSimpleApp())
def cli():
    """start click and app
    """

@cli.command("init")
def init(cli):
    click.echo('start app')

cli.add_command(init)
