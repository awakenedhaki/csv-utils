from typing import Iterable, Generator, List

def split_(table: Iterable, nrows_per_table: int) -> Generator[List, None, None]:
    '''
    Splits an iterable object into n number of iterables.

    Parameters
    ----------
    table : Iterable
        An iterable object that contains more than 1 element.
    ntables : int
        The number of iterables that `table` should be split into.

    Returns
    -------
    Generator
        A generator of tuples of the partitioned Iterable.
    '''
    # Initial starting slice point
    previous_cutoff_index = 0
    # Iterate over the indices to be used to split the tabular data into `ntables`
    for current_cutoff_index in range(nrows_per_table, len(table) + nrows_per_table, nrows_per_table):
        subset = table[previous_cutoff_index:current_cutoff_index]
        subset[-1] = subset[-1].strip()
        yield subset
        previous_cutoff_index = current_cutoff_index

def split_ntables(table: Iterable, *args, ntables: int = 2, **kwargs) -> Generator[List, None, None]:
    table = list(table)
    nrows_per_table = len(table) // ntables
    yield from split_(table, *args, nrows_per_table = nrows_per_table, **kwargs)
