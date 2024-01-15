import json
import yaml


def parse(data, extension):
    if extension == 'json':
        return json.load(data)
    if extension == 'yml':
        return yaml.safe_load(data)
    else:
        raise ValueError('Неподдерживаемый формат файла ')
