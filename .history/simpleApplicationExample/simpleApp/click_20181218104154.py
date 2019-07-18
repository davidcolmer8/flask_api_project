import click


@click.group()
def cli():
    pass

@click.command()
def init():
    click.echo('start app')


cli.add_command(init)
