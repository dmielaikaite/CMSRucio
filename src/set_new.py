#!/usr/bin/env python

from __future__ import print_function
from rucio.client.client import Client

cl = Client(account='root')
print(cl.whoami())

for campaign in ['NanoAODv5', 'Nano1June2019']:
    filters = {'name': '*%s*' % campaign}

    for did in list(cl.list_dids(scope='cms', filters=filters)):
        try:
            print('Fixing up %s' % did)
            cl.set_metadata(scope='cms', name=did, key='is_new', value=True)
        except:
            print(' failed')
