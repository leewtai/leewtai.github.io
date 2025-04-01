import csv
import os

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import re
import requests
import seaborn as sns

key = os.environ.get('CENSUS_KEY')

URL = 'https://api.census.gov/data/{year}/acs/acs5'
payload = {
        'get': 'group(B11002)',
        'for': 'county:*',
        'key': key}

yr_range = range(2009, 2024)

dfs = []
for yr in yr_range:
    resp = requests.get(URL.format(year=yr), params=payload)
    assert resp.status_code == 200
    dat = resp.json()
    df = pd.DataFrame(dat[1:], columns=dat[0])
    df['year'] = yr
    dfs.append(df)

df = pd.concat(dfs)
df.to_csv('household_cnt.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

# you can download the geometries here: https://www.census.gov/cgi-bin/geo/shapefiles/index.php
geos = gpd.read_file('geos')
geos = geos.loc[:, ['GEOID', 'INTPTLAT', 'INTPTLON']]
geos.INTPTLAT = geos.INTPTLAT.astype(float)
geos.INTPTLON = geos.INTPTLON.astype(float)

df['GEOID'] = df.GEO_ID.apply(lambda x: re.sub(r'.+US', '', x))
bdf = df.merge(geos, left_on='GEOID', right_on='GEOID')
bdf.drop(columns=['GEOID', 'GEO_ID'], inplace=True)

bdf.to_csv('with_geo_household_cnt.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
