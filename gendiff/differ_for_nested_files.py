import os.path
from gendiff.parser import parse


def geniff_nested(file1_nested, file2_nested):
    data1_nested = get_nested_path(file1_nested)
    data2_nested = get_nested_path(file2_nested)
    return gendiff_diff_nested(data1_nested, data2_nested)


def get_file_format(file_path):
    extension = get_nested_path(file_path)
    return parse(open(file_path), extension)


def get_nested_path(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]