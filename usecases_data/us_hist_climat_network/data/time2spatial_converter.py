import glob
import re
from math import floor

import pandas as pd


rep_vars = ['value', 'dmflag', 'qcflag', 'dsflag']
months = list(range(12))
variables = ['prcp', 'tmin', 'tmax']
st_data = {}
for var in variables:
    csvs = glob.glob('csvs/US*{var}.csv'.format(var=var))
    station_data = []
    for csv in csvs:
        station = re.sub('.*/(USH[0-9]+)\..*', '\\1', csv)
        datum = pd.read_csv(csv)
        months_data = []
        for m in months:
            val_vars = [v + str(m) for v in rep_vars]
            md = datum[['id', 'year'] + val_vars].copy()
            md.rename(columns={v + str(m): var + '_' + v
                               for v in rep_vars},
                      inplace=True)
            md['month'] = m + 1
            months_data.append(md)
        station_data.append(pd.concat(months_data, sort=True))
    st_data.update({var: pd.concat(station_data)})


all_data = st_data['prcp'].merge(
    st_data['tmin'], how='outer').merge(
    st_data['tmax'], how='outer')
all_data = all_data[all_data.year >= 1900]

# merge with meta data to get lon/lat
stat_meta = pd.read_csv('csvs/station_metadata.csv')
stat_meta.drop(
    columns=['country_code', 'coop_id', 'component_1',
             'component_2', 'component_3', 'id_place_holder', 'name',
             'network_code'], inplace=True)
all_data = all_data.merge(stat_meta, how='left', on='id')

ym_comb = (all_data.year * 100 + all_data.month).unique()
for ym in ym_comb:
    y = floor(ym / 100)
    m = ym - y * 100
    spatial_data = all_data[(all_data.year == y) & (all_data.month == m)]
    spatial_data.to_csv('spatial_data/{ym}.csv'.format(ym=ym), index=False)
