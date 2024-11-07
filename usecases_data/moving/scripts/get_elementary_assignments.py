import csv

import pandas as pd
import requests

resp = requests.get('https://data.taipei/api/v1/dataset/'
                    'a97b9fae-c20f-4a33-a5d3-fa36e64c304f'
                    '?scope=resourceAquire')

if resp.status_code != 200:
    raise Exception(f'Request Status Code {resp.status_code}: '
                    'when calling elementary school district api')

pd.DataFrame(resp.json()).to_csv('../data/elementary_school_districts.csv',
                                 index=False, quoting=csv.QUOTE_NONNUMERIC)
