#!/usr/bin/env python3
###
#
# Get the signature chain of a user
# and pretty-print it as (almost valid) JSON
#
# Usage: sigs.py <username> > sigs.json
#
###

import json
import sys

from keybase import get_uid, get_sigchain
from utils import load_json_fields


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <username>'.format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]

    sigs = get_sigchain(get_uid(username))

    for i, sig in enumerate(sigs, start=1):
        sig['_'] = i  # Just add the number on the top
        load_json_fields(sig)
        print(json.dumps(sig, sort_keys=True, indent=4, separators=(',', ': ')))
