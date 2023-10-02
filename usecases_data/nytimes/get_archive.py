from itertools import product
from datetime import datetime
import json
import logging
import re
import time
from pathlib import Path

import requests


log_file = 'get_archive.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)

# Connecting requests error logs to logging
logger = logging.getLogger('urllib3')
logger.setLevel(logging.INFO)

cred = json.load(open('../credentials.json', 'r'))
# NYTImes limits to 4000 calls a day
pattern = 'climat'

months = range(1, 13)
min_y = 2022
max_y = 2023
years = range(min_y, max_y + 1)
today = datetime.today()


# relev_docs = []
archive_url = 'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json'
for year, month in product(years, months):
    if year == today.year or month == today.month:
        break
    logging.info('Extracting archive data for year {} and month {}'.format(
                 year, month))
    arch_url = archive_url.format(year=year, month=month)
    params = {'api-key': cred['nytimes_api_key']}
    arch_resp = requests.get(url=arch_url, params=params)
    if arch_resp.status_code != 200:
        logging.info('year {year}, month {month} failed'.format(
            year=year, month=month))
    out = arch_resp.json()
    logging.info('got year {}, month {}'.format(year, month))
    docs = out.get('response').get('docs')
    json.dump(docs, open('archive/nyt_arch_{}_{}.json'.format(year, month),
                         'w'))
    # only keep articles with the keyword
    # for doc in docs:
    #     kws = ';'.join([kw.get('value') for kw in doc.get('keywords')])
    #     hls = ';'.join([hl for hl in doc.get('headline').values() if hl])
    #     search_space = (kws + ';' + hls).lower()
    #     if re.search(pattern, search_space):
    #         relev_docs.append(doc)

    time.sleep(6.1)


# json.dump(relev_docs,
#           open('nyt_arch_{}_{}_to_{}.json'.format(pattern, min_y, max_y),
#                'w'))
