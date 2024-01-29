import os

from gendiff.parser import parse
from gendiff.gendiff_build import gendiff_diff


def gendiff(file1, file2):
    data1 = get_file_data(file1)
    data2 = get_file_data(file2)
    return gendiff_diff(data1, data2)


def get_file_data(file_path):
    extension = get_file_extension(file_path)
    return parse(open(file_path), extension)


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


# print(gendiff('/home/oleg/python-project-50/tests/fixtures/file2.json',
#               '/home/oleg/python-project-50/tests/fixtures/file1.yml'))
