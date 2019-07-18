import click

from simpleApp.home.home import startApp

def startSimpleApp(info):
    return startApp(cli=True)

@click.group()
def cli():
    '''start click

@cli.command()
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()
