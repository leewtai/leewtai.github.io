import json
from pathlib import Path

import pandas as pd
import re
import requests

cred_file = Path('../credentials.json')
api_key = json.load(cred_file.open('r'))['alpha_vantage_api_key']
URL = "https://www.alphavantage.co/query"
params = {"function": "TIME_SERIES_WEEKLY_ADJUSTED",
          "symbol": "GDXJ",
          "apikey": api_key}


layoffs = pd.read_csv('layoff.csv')
crunch = pd.read_csv('../crunchbase/organizations.csv')
crunch.columns
crunch.drop(columns=['uuid', 'twitter_url', 'facebook_url', 'logo_url',
                     'homepage_url', 'linkedin_url', 'cb_url', 'type',
                     'city', 'region', 'domain'],
            inplace=True)
crunch_sans_na = crunch.loc[crunch.combined_stock_symbols.notna()].copy()
crunch_sans_na.shape
crunch_sans_na.sample(10)

layoffs.drop(columns=['Location'], inplace=True)
layoffs['Company'] = layoffs.Company.str.lower()
crunch_sans_na['name'] = crunch_sans_na.name.str.lower()

jdf = layoffs.merge(crunch_sans_na, how='left',
                    left_on='Company', right_on='name')
jdf.combined_stock_symbols.notna().mean()

symbols = jdf.loc[jdf.combined_stock_symbols.notna()].combined_stock_symbols
sym_pattern = re.compile(r'[a-z]+:([A-Z]+)')
syms = symbols.apply(lambda x: sym_pattern.sub('\\1', x))

sym = syms[0]
sym
params = {"function": "TIME_SERIES_WEEKLY_ADJUSTED",
          "symbol": "GDXJ",
          "apikey": api_key}
params.update({'symbol': sym})

resp = requests.get(URL, params=params)
weekly_price = resp.json()
price = pd.DataFrame(weekly_price['Weekly Adjusted Time Series'])
price.T


lo_date = layoffs['Date Added']
lo_date = pd.to_datetime(lo_date)
lo_date[0]
