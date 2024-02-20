# Calling an API from NYCOpenData
import csv
import json
from glob import glob

import pandas as pd
import requests

cred = json.load(open('../credentials.json', 'r'))
params = {'fiscal_year': 2021,
          '$limit': 50000,
          '$offset': 0,
          #'$where': 'agency_start_date between "2020-01-01" and "2020-01-31"'
          '$where': 'agency_name = "POLICE DEPARTMENT"'
          }
# 2020 is about 100MB
for i in range(100):
    params.update({'$offset': i * params['$limit']})
    data = requests.get(
        url="https://data.cityofnewyork.us/resource/k397-673e.json",
        params=params,
        headers={'X-App-Token': cred['nycopendata_demo_token']})
    payroll = data.json()
    df = pd.DataFrame(payroll)
    out_fn = f'data/nyc{params["fiscal_year"]}_payroll_offset_{params["$offset"]}.csv'
    df.to_csv(out_fn, index=False, quoting=csv.QUOTE_NONNUMERIC)
    if df.shape[0] < params['$limit']:
        print(f'terminating loop at {i} iterations')
        break


dfs = []
file_names = glob(f'data/*{params["fiscal_year"]}*')
dfs = [pd.read_csv(file_name) for file_name in file_names]
df = pd.concat(dfs)
df.to_csv(f'nyc_payroll_{params["fiscal_year"]}.csv',
          index=False, quoting=csv.QUOTE_NONNUMERIC)