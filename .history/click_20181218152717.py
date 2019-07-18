import click
from simpleApp.main.home import startApp

def startSimpleApp(info):
    return startApp(cli=True)

@.group(startApp=startSimpleApp)
def cli():
    """start click and app
    """

@cli.command("init")
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()
