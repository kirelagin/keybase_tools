#!/usr/bin/env python3
###
#
# Tell Keybase.io to try to check a failed proof again
#
# Usage: retry.py <username> <password> <proof_id>
# Works only when `proof_state = PERM_FAILURE`.
#
###

import json
from pprint import pprint
import sys

from keybase import api_get, authenticate
from utils import load_json_fields


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} <username> <password> <proof_id>'.format(sys.argv[0]))
        sys.exit(1)
    username, password, proof_id = sys.argv[1:4]

    s = authenticate(username, password)

    res = api_get('sig/retry', s, proof_id=proof_id)
    pprint(res)
