import logging
import os
import re
from time import sleep
from itertools import product

import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='census.log')
census_key = os.getenv('CENSUS_KEY')

# Define the range of years we want
years = list(range(2019, 2023))

# Define the variable we want to analyze - default CensusReporter profile variables
# https://api.census.gov/data/2022/acs/acs5/variables.html
tables = ['B01001', #population by age
          'B03002', #race
          'B19001', #household income
          'B25064', #median gross rent
          'B25077', #median home value
          'B25088', #median monthly housing costs
          'B12001', #marital status
          #'B25003', #owner occupied
          'B25002', #occupied vs vacant housing units
          #'B08006', #means of transportation to work
          #'B25024', #type of structure
          #'B07003', #geographical mobility
          'B15002', #educational attainment
  ]

table_pattern = '(' + '|'.join(tables) + ')'
pattern = f'.*name="({table_pattern}_[0-9]{{3}}[EMP]+)".*'
re.search(pattern, s)
re.sub(pattern, '\\1', s)

var_doc_resp = requests.get('https://api.census.gov/data/2022/acs/acs5/variables.html')
var_doc = {tab: [] for tab in tables}
for s in var_doc_resp.text.split('\n'):
    if re.search(pattern, s):
        var_name = re.sub(pattern, '\\1', s)
        if len(var_name) > 12:
            continue
        tab_name = var_name.split('_')[0]
        var_doc[tab_name].append(var_name)
get_param = ','.join(var_doc)

# Explanation for the geographies: https://www.census.gov/newsroom/blogs/random-samplings/2014/07/understanding-geographic-relationships-counties-places-tracts-and-more.html
# ANSI codes: https://www.census.gov/library/reference/code-lists/ansi.html#schdist
# https://www2.census.gov/geo/docs/reference/codes2020/national_state2020.txt
states = [6, 8, 15, 30, 36, 47, 50]
dfs = []
for year in years:
    df_states = []
    for state_code in states:
        df_base = None
        for tab in tables:
            # state_code = 6
            # year = 2021
            # tab = 'B01001'
            URL = f"https://api.census.gov/data/{year}/acs/acs5"
            get_param = 'NAME,' + ','.join(var_doc[tab])
            payload = {
                'get': get_param,
                'for': 'place:*',
                'in': f'state:{state_code:02}',
                'key': census_key
            }
            resp = requests.get(URL, params=payload)
            assert resp.status_code == 200
            logging.info(f'Processing state code {state_code} for year {year} and table {tab}')
            sleep(10)
            dat = resp.json()
            df = pd.DataFrame(dat[1:], columns=dat[0])
            df['year'] = year
            if df_base is None:
                df_base = df
            else:
                df_base = df_base.merge(df, on=['NAME', 'state', 'place', 'year'],
                                        how='outer')
        df_states.append(df_base)
    dfs.append(pd.concat(df_states))
bdf = pd.concat(dfs)
del dfs, df_states, df_base, df
                
bdf.to_csv('census_data_19_22.csv', index=False)


