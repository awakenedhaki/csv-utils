import os
import pytest

from csv_utils import load_table, load_tables
from tests.utils import DATA_DIR, read_sample

@pytest.mark.parametrize('sample_id', [
    '01',
    '02'
])
def test_load_table_csv_one_column(sample_id, read_sample):
    expected = read_sample(sample_id, 'csv')
    path_sample = os.path.join(DATA_DIR, 'sample', f'sample-{sample_id}.csv')
    observed = next(load_table(path_sample))
    assert observed == expected

pytest.mark.parametrize('sample_ids', [
    ['01', '02', 'csv'],
    ['02', '01', 'csv']
    ['01', '02', 'tsv'],
    ['02', '01', 'tsv']
])
def test_load_tables_csv_two_columns(sample_ids, read_sample):
    file_type = sample_ids.pop()
    expected = [read_sample(sample_ids[0], file_type), read_sample(sample_ids[1], file_type)]
    
    sample_paths = []
    for id in sample_ids:
        sample_paths.append(os.path.join(DATA_DIR, 'sample', f'sample-{id}.{file_type}'))
    observed = [sample for sample in load_tables(sample_paths)]
    assert observed == expected