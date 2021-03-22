# Based off these instructions: https://api.biorxiv.org/covid19/help
import logging
import json

import requests

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename="ingest.log",
                    level=logging.INFO)

url = "https://api.biorxiv.org/covid19/{}"

cursor = 0
limit = 30

dat = []
while True:
    if cursor % 1000 == 0:
        logging.info('cursor is now at {}'.format(cursor))
    resp = requests.get(url=url.format(cursor))
    if resp.status_code != 200:
        logging.error('Status non 200 at cursor {}'.format(cursor))
        break
    out = resp.json()
    dat.extend(out.get('collection'))

    count = out.get('messages')[0].get('count')
    cursor += count
    if count < limit or cursor > out.get('messages')[0].get('total'):
        logging.info('reached end of daabase')
        break

json.dump(dat, open('bioRxiv.json', 'w'))
