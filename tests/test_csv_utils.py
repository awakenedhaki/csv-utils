# LOADING LIBRARIES ============================================================
import os

from io import StringIO
from pytest import fixture
from csv_utils import __version__
from csv_utils import *

# CONSTANTS ====================================================================
TEST_SCRIPT = os.path.realpath(__file__)
TEST_DIR = os.path.split(TEST_SCRIPT)[0]

DATA_DIR = os.path.join(TEST_DIR, 'data')

# FIXTURES =====================================================================
@fixture
def generate_lines():
    def _generate_lines(nrows):
        data = [str(num) for num in list(range(0, nrows))]
        file = StringIO('\n'.join(data))
        return file.readlines()
    return _generate_lines

@fixture
def read_sample():
    def _read_sample(id, file_format):
        sample_path = os.path.join(DATA_DIR, 'sample', f'sample-{id}.{file_format}')
        with open(sample_path, 'r') as f:
            return f.readlines()
    return _read_sample

# TEST FUNCTIONS ===============================================================
def test_version():
    assert __version__ == '0.1.0'

# . Loading Tables
def test_load_table_csv_one_column(read_sample):
    expected = read_sample('01', 'csv')
    path_sample = os.path.join(DATA_DIR, 'sample', 'sample-01.csv')
    observed = next(load_table(path_sample))
    assert observed == expected

def test_load_table_csv_two_columns(read_sample):
    expected = read_sample('02', 'csv')
    sample_path = os.path.join(DATA_DIR, 'sample', 'sample-02.csv')
    observed = next(load_table(sample_path))
    assert observed == expected

def test_load_tables_csv_two_columns(read_sample):
    expected = [read_sample('01', 'csv'), read_sample('02', 'csv')]
    
    sample_paths = []
    for i in range(1, 3):
        sample_paths.append(os.path.join(DATA_DIR, 'sample', f'sample-0{i}.csv'))

    observed = [sample for sample in load_tables(sample_paths)]
    assert observed == expected

def test_load_tables_csv_two_columns_reverse(read_sample):
    expected = [read_sample('02', 'csv'), read_sample('01', 'csv')]
    
    sample_paths = []
    for i in range(2, 0, -1):
        sample_paths.append(os.path.join(DATA_DIR, 'sample', f'sample-0{i}.csv'))

    observed = [sample for sample in load_tables(sample_paths)]
    assert observed == expected

def test_load_tables_tsv_two_columns_(read_sample):
    expected = [read_sample('01', 'tsv'), read_sample('02', 'tsv')]
    
    sample_paths = []
    for i in range(1, 3):
        sample_paths.append(os.path.join(DATA_DIR, 'sample', f'sample-0{i}.tsv'))

    observed = [sample for sample in load_tables(sample_paths)]
    assert observed == expected

# . Splitting
def test_split_single_column_with_round_number_rows(read_sample, generate_lines):
    first_expected = read_sample('03', 'csv')
    second_expected = read_sample('04', 'csv')

    sample = generate_lines(10)
    first, second = [list(output) for output in split(sample, 2, header = False)]
    assert (first == first_expected) & (second == second_expected)
    
def test_split_single_column_with_non_round_number_rows(read_sample, generate_lines):
    first_expected = read_sample('03', 'csv')
    second_expected = read_sample('04', 'csv')
    third_expected = read_sample('05', 'csv')

    sample = generate_lines(11)
    first, second, third = [list(output) for output in split(sample, 2, header = False)]
    assert (first == first_expected) & (second == second_expected) & (third == third_expected)
    
    