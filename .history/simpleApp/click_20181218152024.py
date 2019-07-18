import click

from simp home.home import startApp

def startSimpleApp(info):
    return startApp(cli=True)

@click.group()
def cli():
    pass

@cli.command()
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()
