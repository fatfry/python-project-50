import json


def gendiff_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))

    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data2:
            print(f'- {key}: {data1[key]}')
        elif key not in data1:
            print(f'+ {key}: {data2[key]}')
        elif data1[key] != data2[key]:
            print(f'- {key}: {data1[key]}')
            print(f'+ {key}: {data2[key]}')
        else:
            print(f'  {key}: {data1[key]}')
