import click

from simpleApp.home.home import startApp

def startSimpleApp(info):
    return startApp(cli=True)

@click.group(startApp=sta)
def cli():
    """start click and app
    """

@cli.command()
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()
