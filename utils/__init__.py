import json


def load_json_fields(data):
    for k, v in data.items():
        if k.endswith('_json') and v:
            data[k] = json.loads(v)
            load_json_fields(data[k])
