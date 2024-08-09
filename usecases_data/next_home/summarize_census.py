import re

import pandas as pd
import numpy as np

df = pd.read_csv('census_data_19_22.csv')
df.sample(3)
assert 'year' in df.columns
assert 'state' in df.columns
assert 'place' in df.columns

breaks = {
    'age': {
      'male age dist': {
        'total' : 'B01001_002E',
        'breaks': [
          'B01001_005E',  # male 9-14
          'B01001_006E', # male 15-17
          'B01001_009E',  # male 21
          'B01001_012E',  # male -29
          'B01001_015E',  # male -49
          'B01001_019E',  # male -64
          'B01001_024E',  # male -85
          'B01001_025E',  # male over 85
          ]},
      'female age dist': {
        'total' : 'B01001_026E',
        'breaks': [
          'B01001_029E',  # female 9-14
          'B01001_030E', # male 15-17
          'B01001_033E',  # female 21
          'B01001_036E', # female -29
          'B01001_039E', # female -49
          'B01001_043E', # female -64
          'B01001_048E', # female -85
          'B01001_049E',
          ]}},
    'edu': {
      'male over 25 max schooling': {
        'total' : 'B15002_002E',
        'breaks': [
          'B15002_003E',  # male over 25 no school
          'B15002_011E', # male over 25 high school graduate
          'B15002_015E',  # male over 25 with Bachelors
          'B15002_018E'  # male over 25 with Doctorate
          ]},
      'female over 25 max schooling': {
        'total' : 'B15002_019E',
        'breaks': [
          'B15002_020E',  # female over 25 with no school
          'B15002_028E',
          'B15002_032E',
          'B15002_035E']}}
        }



def rolling_census(df, total_col, break_cols):
    census_suffix_pattern = r'([0-9]+)[EMP]+'
    total = df[total_col]
    prefix, suffix = total_col.split('_')
    last_ind = int(re.sub(census_suffix_pattern , '\\1', suffix))
    ests = {}
    for i in range(len(break_cols)):
        suffix = break_cols[i].split('_')[1]
        end_ind = int(re.sub(census_suffix_pattern, '\\1', suffix))
        grp_total = np.zeros(len(df))
        for j in range(last_ind+1, end_ind+1):
            col = f'{prefix}_{j:03}E'
            grp_total += df[col].to_numpy()
        ests.update({f'{prefix}_{last_ind+1}_{end_ind}': grp_total})
        last_ind = end_ind
    ests.update({'total': total})
    return pd.DataFrame(ests)

total_col = breaks['edu']['male over 25 max schooling']['total']
break_cols = breaks['edu']['male over 25 max schooling']['breaks']

new_df = rolling_census(df, total_col, break_cols)
new_df.sample(4)
