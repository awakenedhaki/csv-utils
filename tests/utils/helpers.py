import os

from io import StringIO
from tests.utils import DATA_DIR

def generate_lines(nrows):
    data = [str(num) for num in list(range(0, nrows))]
    file = StringIO('\n'.join(data))
    return file.readlines()

def read_sample(id, file_format):
    sample_path = os.path.join(DATA_DIR, 'sample', f'sample-{id}.{file_format}')
    with open(sample_path, 'r') as f:
        return f.readlines()