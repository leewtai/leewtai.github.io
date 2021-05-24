from itertools import product
from pathlib import Path
import json
import re

import pandas as pd

crime = json.load(Path('state_crime.json').open('r'))
years = range(2000, 2020)
with Path('state_abbr.txt').open('r') as f:
    states = [f.read(2) for _ in f]

filter_states = ['CA', 'NY', 'WY', 'AK', 'SC', 'MO', 'NC', "PA", "WA"]
final = {}
for state in crime:
    if state not in filter_states:
        continue
    year_oris = crime.get(state)
    years = []
    for yr_ori in year_oris:
        yr_ori.pop('state_abbr')
        datum = {'ori': yr_ori.get('ori'),
                 'year': yr_ori.get('data_year'),
                 'offenses': {yr_ori.get('offense'): {
                     'cleared': yr_ori.get('cleared'),
                     'actual': yr_ori.get('actual')}}}
        if state == 'NY':
            datum.get('offenses').update(
                {'fake_offense': {'cleared': 0, 'actual': 0}})

        years.append(datum)
    final.update({state: years})

json.dump(final, Path('2102_mid2_violent_crime.json').open('w'))

oris = json.load(Path('all_ori_metadata.json').open('r'))

df = pd.DataFrame(oris)
condition = df.state_abbr.apply(lambda x: x in filter_states)
df = df.loc[condition, :]
condition2 = df.state_abbr == 'WA'
df.nibrs_start_date[condition2] = df.nibrs_start_date[condition2].apply(
    lambda x: re.sub('([0-9]+)/([0-9]+)/([0-9]+)', '\\3-\\2-\\1', x) if x else None)
df.to_csv("oris_metadata.csv", sep=";", index=False)
