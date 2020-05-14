# Calling an API from NYCOpenData
import json
from glob import glob

import pandas as pd
import requests

cred = json.load(open('../credentials.json', 'r'))
params = {'fiscal_year': 2019,
          'agency_name': 'POLICE DEPARTMENT',
          '$limit': 50000,
          '$offset': 0,
          '$where': 'agency_start_date between "2019-01-01" and "2019-01-31"'}
# 2019 is about 100MB
for i in range(100):
    params.update({'$offset': i * params['$limit']})
    data = requests.get(
        url="https://data.cityofnewyork.us/resource/k397-673e.json",
        params=params,
        headers={'X-App-Token': cred['nycopendata_demo_token']})
    payroll = data.json()
    df = pd.DataFrame(payroll)
    df.to_csv('data/nyc2019_payroll_offset_{}.csv'.format(params['$offset']))
    if df.shape[0] < params['$limit']:
        print('terminating loop at {} iterations'.format(i))
        break


dfs = []
file_names = glob('data/*')
dfs = [pd.read_csv(file_name) for file_name in file_names]
df = pd.concat(dfs)
df.to_csv('nyc_payroll_201901.csv')
