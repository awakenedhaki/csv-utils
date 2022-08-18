# DEPENDENCIES =================================================================
from pathlib import Path
from typing import Iterable, List, Union, Generator

# FUNCTIONS ====================================================================
def load_tables(paths: Iterable[Union[str, Path]]) -> Generator[str, None, None]:
    '''
    Loads tabular data files which paths have been specified.

    Parameters
    ----------
    paths : Iterable
        A list of paths that that direct to the tabular data files.
    
    Returns
    -------
    A generator with each element corresponding to an iterable of the lines within the file.
    '''
    for path in paths:
        yield load_table(path)

def load_table(path: Union[str, Path]) -> List[str]:
    '''
    Load a singular tabular data file.
    
    Parameters
    ----------
    path : str | Path
        A path that directs to a tabular data file.
    '''
    with open(path, 'r') as f:
        return f.readlines()