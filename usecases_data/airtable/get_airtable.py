import csv
import json
from pathlib import Path

import pandas as pd

# Find the fetch initiator
layoff_path = Path('layoff.json')
with layoff_path.open('r') as f:
    dat = json.load(f)

assert dat.get('msg') == 'SUCCESS'
dat = dat.get('data').get('table')
columns = dat.get('columns')
attr_maps = {}
for col in columns:
    if col['typeOptions'] is None or col['typeOptions'].get('choices') is None:
        continue
    choices = col['typeOptions']['choices']
    attr_map = {choice: choices[choice]['name'] for choice in choices}
    attr_maps.update({col['id']: attr_map})

col_map = {col.get('id'): col.get('name') for col in columns}

rows = []
for row in dat.get('rows'):
    row_dat = row['cellValuesByColumnId']
    for attr in attr_maps:
        if attr not in row_dat:
            continue
        row_col_val = row_dat[attr]
        if not isinstance(row_col_val, list):
            row_dat[attr] = attr_maps[attr][row_col_val]
            continue
        jstr = ';'.join(attr_maps[attr][val] for val in row_col_val)
        row_dat[attr] = jstr
    rows.append(row_dat)
df = pd.DataFrame(rows)
df.rename(columns=col_map, inplace=True)
df.head(3)
df.drop(columns=['List of Employees Laid Off'], inplace=True)
df.to_csv('layoff.csv', quoting=csv.QUOTE_NONNUMERIC, index=False)
