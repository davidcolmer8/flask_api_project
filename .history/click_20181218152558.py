import click
from main.home import startApp
def startSimpleApp(info):
    return startApp(cli=True)

@click.group(startApp=startSimpleApp)
def cli():
    """start click and app
    """

@cli.command("init")
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()
