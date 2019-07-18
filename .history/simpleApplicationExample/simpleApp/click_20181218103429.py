import click
from flask.cli import FlaskGroup



@click.group()
def cli():
    pass


if __name__=='__main__':
    cli()
