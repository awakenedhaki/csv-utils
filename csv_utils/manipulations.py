from typing import Iterable, Generator, Tuple

# FUNCTIONS
def split(table: Iterable, ntables: int, header: bool = True) -> Generator[Tuple, None, None]:
    '''
    Splits an iterable object into n number of iterables.

    Parameters
    ----------
    table : Iterable
        An iterable object that contains more than 1 element.
    ntables : int
        The number of iterables that `table` should be split into.
    header : bool
        If the first element in `table` should persist for each generated iterable.
    
    Returns
    -------
    Generator
        A generator of tuples of the partitioned Iterable.
    '''
    # Extract the `header` of the tabular data, if one exists
    header_row = None
    if header:
        header_row = next(table)

    # Convert `table` into a tuple type
    table = list(table)
    # Determine the number of rows per table for the specified number of tables to generate
    nrows_per_table = len(table) // ntables
    # Initial starting slice point
    previous_cutoff_index = 0
    # Iterate over the indices to be used to split the tabular data into `ntables`
    for current_cutoff_index in range(nrows_per_table, len(table) + nrows_per_table, nrows_per_table):
        subset = table[previous_cutoff_index:current_cutoff_index]
        subset[-1] = subset[-1].strip()
        yield subset
        previous_cutoff_index = current_cutoff_index