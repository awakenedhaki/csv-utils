import click
from pip import main

from commands import split, merge

@click.group()
def cli():
    pass

cli.add_command(split)

if __name__ in '__main__':
    cli()