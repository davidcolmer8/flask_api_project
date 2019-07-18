import click


@click.group()
def cli():
    pass

@cli.command()
def inti():
    cli


if __name__=='__main__':
    cli()
