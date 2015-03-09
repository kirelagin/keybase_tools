from binascii import unhexlify
from base64 import b64decode
import hmac
import json
import requests
import scrypt


KEYBASE_DOMAIN = 'keybase.io'
KEYBASE_PATH = '/_/api/1.0/'

def api_get(method, session=requests, **kwargs):
    r = session.get('https://' + KEYBASE_DOMAIN + KEYBASE_PATH + method + '.json', params=kwargs)
    j = r.json()
    if j['status']['code'] != 0:
        raise Exception(j['status'])
    return j

def api_post(method, session=requests, **kwargs):
    r = session.post('https://' + KEYBASE_DOMAIN + KEYBASE_PATH + method + '.json', params=kwargs)
    return r

def authenticate(username, password):
    s = requests.Session()
    r = api_get('getsalt', s, email_or_username=username)
    salt, challenge = r['salt'], r['login_session']
    pwh = scrypt.hash(password, unhexlify(salt), N=(1<<15), r=8, p=1, buflen=224)[192:224]
    h = hmac.new(pwh, digestmod='sha512',  msg=b64decode(challenge.encode('ascii'))).hexdigest()
    r = api_post('login', s, raw=True, email_or_username=username, hmac_pwh=h, login_session=challenge)
    if 'session' not in s.cookies.get_dict():
        raise Exception('Wrong username or password')
    return s


def get_uid(username):
    return api_get('user/lookup', username=username, fields='none')['them']['id']

def get_sigchain(uid):
    return api_get('sig/get', uid=uid)['sigs']
