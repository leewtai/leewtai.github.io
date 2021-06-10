from itertools import product
import json
import logging
import time
from pathlib import Path

import requests


log_file = 'get_archives.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)

# Connecting requests error logs to logging
logger = logging.getLogger('urllib3')
logger.setLevel(logging.INFO)

cred = json.load(open('../credentials.json', 'r'))
# NYTImes limits to 4000 calls a day
cap = 2000
calls_today = 0

months = list(range(1, 13))
years = list(range(2010, 2021))
file = Path('nytimes_{}_{}_arch.json'.format(min(years), max(years))

archive_url = 'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json'
logging.info('Extracting archive data for {} months'.format(len(months)))
for year, month in product(years, months):
    arch_url = archive_url.format(year=year, month=month)
    params = {'api-key': cred['nytimes_api_key']}
    arch_resp = requests.get(url=arch_url, params=params)
    calls_today += 1
    if arch_resp.status_code != 200:
        logging.info('year {year}, month {month} failed'.format(
            year=year, month=month))
    out = arch_resp.json()
    logging.info('got year {}, month {}'.format(year, month))
    # Archives have duplicate entries, take the later one arbitrarily
    uniq_arts = {article['_id']: article
                 for article in out['response']['docs']}
    json.dump(uniq_arts,
              open('nyt_arch_{}_{}.json'.format(year, month), 'w'))
    time.sleep(6.1)
