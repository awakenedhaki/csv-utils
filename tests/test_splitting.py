from src import split_, split_ntables
from tests.utils import read_sample, generate_lines

def test_split_single_column_with_round_number_rows():
    first_expected = read_sample('03', 'csv')
    second_expected = read_sample('04', 'csv')

    sample = generate_lines(10)
    first, second = [list(output) for output in split_ntables(sample, ntables = 2)]
    assert (first == first_expected) & (second == second_expected)
    
def test_split_single_column_with_non_round_number_rows():
    first_expected = read_sample('03', 'csv')
    second_expected = read_sample('04', 'csv')
    third_expected = read_sample('05', 'csv')

    sample = generate_lines(11)
    first, second, third = [list(output) for output in split_ntables(sample, ntables = 2)]
    assert (first == first_expected) & (second == second_expected) & (third == third_expected)
    