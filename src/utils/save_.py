# DEPENDENCIES =================================================================
import csv
from pathlib import Path
from typing import Iterable, Union

# CONSTANTS ====================================================================
TAB_DELIMETER = '\t'
COMMA_DELIMETER = ','

# FUNCTIONS ====================================================================
def save_(table: Iterable, path: Union[str, Path], *, delimiter: str = None, header: Iterable = None) -> None:
    '''
    Save a nested iterable into a delimited file format.

    Parameters
    ----------
    table : Iterable 
        A nested list of data.
    path : str | Path
        Destination path for data.
    delimiter : str
        The delimiter, or separator, between values in rows.
    header : Iterable
        The names of the columns.
    '''
    with path.open('w') as file:
        tabular_file = csv.writer(file, delimiter = delimiter)
        if header:
            tabular_file.writerow(header)
        tabular_file.writerows(table)

def save_csv(*args, **kwargs) -> None:
    '''
    Saves nested interable data as a comma-separated values file.
    '''
    if 'delimeter' not in kwargs:
        kwargs['delimiter'] = COMMA_DELIMETER
    save_(*args, **kwargs)

def save_tsv(*args, **kwargs) -> None:
    '''
    Saves nested interable data as a tab-separated values file.
    '''
    if 'delimeter' not in kwargs:
        kwargs['delimiter'] = TAB_DELIMETER
    save_(*args, **kwargs)