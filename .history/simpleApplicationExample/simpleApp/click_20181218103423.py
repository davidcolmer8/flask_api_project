import click
from flask.cli import Flask

@click.group()
def cli():
    pass


if __name__=='__main__':
    cli()
