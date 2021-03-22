from itertools import product
from pathlib import Path
import json

import pandas as pd

crime = json.load(Path('state_crime.json').open('r'))
years = range(2000, 2020)
with Path('state_abbr.txt').open('r') as f:
    states = [f.read(2) for _ in f]

final = {}
for state in crime:
    year_oris = crime.get(state)
    years = {}
    for yr_ori in year_oris:
        yr = yr_ori.get('data_year')
        yr_ori.pop('data_year')
        yr_ori.pop('state_abbr')
        if yr in years:
            years.get(yr).append(yr_ori)
        else:
            years.update({yr: [yr_ori]})
    final.update({state: years})

json.dump(final, Path('2102_mid2_violent_crime.json').open('w'))

oris = json.load(Path('all_ori_metadata.json').open('r'))

df = pd.DataFrame(oris)
df.to_csv("oris_metadata.csv", sep=";", index=False)
