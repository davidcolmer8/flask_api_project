import click


@click.group()
def cli():
    pass

@cli.command()
def inti():
    click.echo


if __name__=='__main__':
    cli()
