import click


@click.group()
def cli():
    pass

@cli.command()
def ini():
    click.echo('start app')


if __name__=='__main__':
    cli()
