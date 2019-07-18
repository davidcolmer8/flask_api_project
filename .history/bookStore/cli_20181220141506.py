import click
from bookStore.books.book import create_app

def startSimpleApp(info):
    return create_app(cli=True)

@click.group(startApp=startSimpleApp)
def cli():
    """start click and app
    """

@cli.command("init")
def init(cli):
    click.echo('start app')

if __name__=='__main__':
    cli()