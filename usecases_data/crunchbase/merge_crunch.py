import json

import pandas as pd
import requests

with open("../credentials.json", "r") as f:
    creds = json.load(f)['crunchbase_api_key']


crunch = pd.read_csv('~/Downloads/organizations.csv',
                     usecols=['uuid', 'name', 'primary_role',
                              'short_description', 'country_code',
                              'combined_stock_symbols'])
layoffs = pd.read_csv('../airtable/layoff.csv')

crunch.head(3)
crunch.country_code.value_counts()

company = 'Lokalise'
uuid = crunch.loc[crunch.name == company, 'uuid'].iloc[0]

uuid = '1dcf3d60-e7a2-95f0-0fbb-0c7a307184c0'
resp = requests.get(url=f'https://api.crunchbase.com/api/v4/entities/organizations/{uuid}',
                    params={
                        'user_key': creds,
                        'card_ids': ['raised_funding_rounds']})
assert resp.status_code == 200
dat = resp.json()
dat
