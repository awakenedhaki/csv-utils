from pathlib import Path
from typing import Iterable, Union, Generator

# FUNCTIONS

def load_tables(paths: Iterable[Union[str, Path]]) -> Generator[str]:
    '''
    Loads tabular data files which paths have been specified.

    Parameters
    ----------
    paths : iterable
        A list of paths that that direct to the tabular data files.
    
    Returns
    -------
    A generator with each element corresponding to an iterable of the lines within the file.
    '''
    for path in paths:
        yield from _load_table(path)

def _load_table(path: Union[str, Path]) -> Generator[str]:
    '''
    '''
    with open(path, 'r') as f:
        yield f.readlines()