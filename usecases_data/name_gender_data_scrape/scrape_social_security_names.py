import time
import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


logging.basicConfig(
    level=logging.INFO,
    filename='social_security_scraping.log',
    format="%(asctime)-15s %(message)s")

years = list(range(1970, 2003))
logging.info('processing years {} to {}'.format(min(years), max(years)))
dfs = []
for year in years:
    params = {
        'year': str(year),
        'top': '500',
        'number': 'n'}
    resp = requests.post(
        url='https://www.ssa.gov/cgi-bin/popularnames.cgi',
        data=params)
    logging.info('{} status for year {}'.format(
        resp.status_code, params['year']))

    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.find_all('tr', align='right')

    fields = ['rank', 'male_name', 'male_name_num',
              'female_name', 'female_name_num']
    name_freqs = []
    for row in rows:
        name_data = [child.text.replace(',', '') for child in row.children
                     if isinstance(child, Tag)]
        name_freqs.append({
            fields[i]: datum for i, datum in enumerate(name_data)})

    out = pd.DataFrame(name_freqs)
    out['year'] = year
    dfs.append(out)
    time.sleep(2)
    logging.info('got year {}'.format(year))


df = pd.concat(dfs)
df.to_csv("gender_names_ssa.csv")
logging.info('wrote data to csv with {} rows of data'.format(df.shape[0]))
