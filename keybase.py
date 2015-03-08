import json
import requests


KEYBASE_DOMAIN = 'keybase.io'
KEYBASE_PATH = '/_/api/1.0/'

def api_get(method, **kwargs):
    r = requests.get('https://' + KEYBASE_DOMAIN + KEYBASE_PATH + method + '.json', params=kwargs)
    j = r.json()
    if j['status']['code'] != 0:
        raise Exception(j['status'])
    return j

def get_uid(username):
    return api_get('user/lookup', username=username, fields='none')['them']['id']

def get_sigchain(uid):
    return api_get('sig/get', uid=uid)['sigs']
