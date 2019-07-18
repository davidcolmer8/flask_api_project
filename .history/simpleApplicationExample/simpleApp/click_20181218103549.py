import click
from flask.cli import FlaskGroup

from .home import home

@click.group()
def cli():
    pass


if __name__=='__main__':
    cli()
