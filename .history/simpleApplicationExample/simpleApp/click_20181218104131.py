import click


@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo('start app')


cli.commmand
