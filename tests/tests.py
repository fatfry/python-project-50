import pytest
from diff_yml import gendiff
from pathlib import Path


def get_fixtures_path(file_name):
    current_dir = Path(__file__).parent
    return f'{current_dir}/fixtures/{file_name}'


def get_fixtures_data(file_name):
    file_path = get_fixtures_path(file_name)
    with open(file_path, 'r') as file:
        return file.read()


def tests_gendiff():
    expected_result = get_fixtures_data('result_json')
    file1 = get_fixtures_path('file1.json')
    file2 = get_fixtures_path('file2.json')
    assert gendiff(file1, file2) == expected_result
    file1 = get_fixtures_path('file1.yml')
    file2 = get_fixtures_path('file2.yml')
    assert gendiff(file1, file2) == expected_result
