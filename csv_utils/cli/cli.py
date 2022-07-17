import click

from csv_utils import *
from pathlib import Path
from csv_utils.cli.helpers import MutuallyExclusiveOption

@click.group()
def cli():
    pass

@cli.command('split')
@click.argument(
    'filename', nargs = 1, type = click.File(mode = 'r', lazy = False)
)
@click.argument(
    'directory', nargs = 1, type = click.Path(file_okay = False, path_type = Path)
)
@click.option(
    '--ntables', type = click.INT, cls = MutuallyExclusiveOption, mutually_exclusive = ['nrows']
)
@click.option(
    '--nrows', type = click.INT, cls = MutuallyExclusiveOption, mutually_exclusive = ['ntables']
)
@click.option(
    '--format', type = click.Choice(['csv', 'tsv'], case_sensitive=False)
)
def split(filename, directory, ntables, nrows, format):
    # Load the tabular data
    table = load_table(filename)
    
    # Determine which `splitting` operation to perform
    if ntables is not None:
        tables = split_ntables(table, ntables = ntables)
    elif nrows is not None:
        tables = split_(table, nrows_per_table = nrows)

    # Store generated tables in specified directory
    directory.mkdir(exists = False)
    for _id, table in enumerate(tables):
        if format == 'tsv':
            save_tsv(table, directory / _id)
        elif format == 'csv':
            save_csv(table, directory / _id)
        

if __name__ == '__main__':
    cli()