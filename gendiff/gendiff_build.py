import json


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    else:
        return value


def gendiff_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))

    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        if key not in data2:
            result.append(f'- {key}: {to_str(data1[key])}')
        elif key not in data1:
            result.append(f'+ {key}: {to_str(data2[key])}')
        elif data1[key] != data2[key]:
            result.append(f'- {key}: {to_str(data1[key])}')
            result.append(f'+ {key}: {to_str(data2[key])}')
        else:
            result.append(f'  {key}: {to_str(data1[key])}')
    result = "\n  ".join(result)
    return f'{{\n  {result}\n}}'
