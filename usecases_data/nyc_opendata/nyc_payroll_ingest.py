# Calling an API from NYCOpenData
import csv
import json
from glob import glob

import pandas as pd
import requests

cred = json.load(open('../credentials.json', 'r'))
# The comments allow us to alter betrween 
params = {#'fiscal_year': 2023,
          '$limit': 50000,
          '$offset': 0,
          #'$where': 'agency_start_date between "2020-01-01" and "2020-01-31"'
          #'$where': 'agency_name = "POLICE DEPARTMENT"'
          '$where': '(created_date between "2023-01-01" and "2023-12-31") AND (complaint_type LIKE "%Noise%" OR complaint_type LIKE "%Graffiti%")'
          }
for i in range(100):
    params.update({'$offset': i * params['$limit']})
    data = requests.get(
        url="https://data.cityofnewyork.us/resource/erm2-nwe9.json", # 311
        # url="https://data.cityofnewyork.us/resource/k397-673e.json", # Payroll
        params=params,
        headers={'X-App-Token': cred['nycopendata_demo_token']})
    payroll = data.json()
    payroll[100]['complaint_type']
    df = pd.DataFrame(payroll)
    # out_fn = f'data/nyc{params["fiscal_year"]}_311_offset_{params["$offset"]}.csv'
    out_fn = f'data/nyc_311_offset_{params["$offset"]}.csv'
    df[['complaint_type', 'created_date', 'incident_zip']].to_csv(out_fn, index=False, quoting=csv.QUOTE_NONNUMERIC)
    if df.shape[0] < params['$limit']:
        print(f'terminating loop at {i} iterations')
        break


dfs = []
file_names = glob(f'data/nyc_311*.csv')
dfs = [pd.read_csv(file_name) for file_name in file_names]
df = pd.concat(dfs)
df.to_csv(f'nyc_311_noise_graffiti_2023.csv',
          index=False, quoting=csv.QUOTE_NONNUMERIC)
