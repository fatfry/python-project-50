from gendiff.constants import CHANGES_FORMATS


def create_difference_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = {}
    for key in keys:
        if key not in data2:
            result[key] = {'type': CHANGES_FORMATS.REMOVED, 'value': data1[key]}
        elif key not in data1:
            result[key] = {'type': CHANGES_FORMATS.ADDED, 'value': data2[key]}

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'type': CHANGES_FORMATS.NESTED,
                'value': create_difference_tree(data1[key], data2[key]),
            }

        elif data1[key] != data2[key]:
            result[key] = {'type': CHANGES_FORMATS.UPDATED,
                           'old_value': data1[key], 'new_value': data2[key]}
        else:
            result[key] = {'type': CHANGES_FORMATS.UNCHANGED, 'value': data1[key]}

    return result
