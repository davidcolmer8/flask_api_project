import click


@click.group()
def cli():
    pass

@cli.command()
def ii():
    click.echo('start app')


if __name__=='__main__':
    cli()
