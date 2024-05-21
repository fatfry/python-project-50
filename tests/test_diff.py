from gendiff.generate_difference import generate_diff
from pathlib import Path
import pytest


FIXTURES_PATH = f'{Path(__file__).parent}/fixtures'


def get_result_data(file_name):
    with open(f'{FIXTURES_PATH}/{file_name}') as output:
        return output.read()


@pytest.mark.parametrize(
    ('file1', 'file2'),
    [
        ('nested_file1.json', 'nested_file2.json'),
        # ('nested_file1.yml', 'nested_file2.yml'),
    ]
)
def test_nested_json_diff(file1, file2):
    file1_path = f'{FIXTURES_PATH}/{file1}'
    file2_path = f'{FIXTURES_PATH}/{file2}'

    assert (generate_diff(file1_path, file2_path)
            == get_result_data('nested_result'))

    assert (generate_diff(file1_path, file2_path, 'stylish')
            == get_result_data('nested_result'))

    assert (generate_diff(file1_path, file2_path, 'plain')
            == get_result_data('nested_plain_result'))

    assert (generate_diff(file1_path, file2_path, 'json')
            == get_result_data('nested_json_result'))
