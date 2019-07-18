import click
from flask.cli import FlaskGroup
from simp

def startSimpleApp():
    return startApp()

@click.group(cls=FlaskGroup)
def cli():
    """start click and app
    """

@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

    click.echo("...init complete")


cli.add_command(init)
