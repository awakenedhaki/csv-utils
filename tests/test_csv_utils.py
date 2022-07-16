# LOADING LIBRARIES
import os

from io import StringIO
from pytest import fixture
from csv_utils import *

# CONSTANTS
TEST_SCRIPT = os.path.realpath(__file__)
TEST_DIR = os.path.split(TEST_SCRIPT)[0]

DATA_DIR = os.path.join(TEST_DIR, 'data')
ORIGINAL = os.path.join(DATA_DIR, 'titanic.csv')
TWO_SPLIT = os.path.join(DATA_DIR, 'two-split')
FOUR_SPLIT = os.path.join(DATA_DIR, 'FOUR-split')

# FIXTURES
@fixture
def generate_file_object():
    def _generate_file_object(nrows):
        data = list(range(0, nrows + 1))
        return StringIO('\n'.join(data))
    return _generate_file_object

@fixture
def generate_lines():
    def _generate_lines(nrows):
        file = generate_file_object(nrows)
        return file.readlines()
    return _generate_lines

# TEST FUNCTIONS
def test_version():
    assert __version__ == '0.1.0'