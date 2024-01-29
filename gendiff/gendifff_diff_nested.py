def gendiff_diff_nested(data1, data2):
    diff = {}
    for key in keys:
        if key not in data2:
            diff[key] = {
                'type': 'removed',
                'value': data1[key]
            }
        elif key not in data1:
            diff[key] = {
                'type': 'added',
                'value': data2[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            ...
        else data1[key] = data2[key]:
            diff[key] = {
                'type': 'changes'
                        'old_value':data1[key]
                        'new_value':data2[key]
            }

