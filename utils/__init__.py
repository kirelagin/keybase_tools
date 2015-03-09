from datetime import datetime, timedelta
import json


def recursive_fix(data, fix):
    if not data:
        return
    for k, v in data.items():
        if v:
            data[k] = fix(k, v)
        if k.endswith('_json'):
            recursive_fix(data[k], fix)

def load_json_fields(data):
    def fix(k, v):
        if k.endswith('_json') and v:
            return json.loads(v)
        return v
    recursive_fix(data, fix)

def parse_times(data):
    def fix(k, v):
        if k in ('ctime', 'etime', 'last_check', 'last_success',):
            d = datetime.fromtimestamp(int(v))
            return '{} ({})'.format(d.isoformat(), v)
        elif k in ('expire_in',):
            d = timedelta(seconds=int(v))
            return '{} ({})'.format(d, v)
        return v
    recursive_fix(data, fix)
