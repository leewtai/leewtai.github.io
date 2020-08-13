# This file pulls data from USDA
import json
import logging
import requests
import pandas as pd

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='call_usda.log',
                    level=logging.INFO)

creds = json.load(open('../credentials.json', 'r'))

URL = "http://quickstats.nass.usda.gov/api/"

# Explore possible values from a variable
params = {"param": "class_desc",
          "key": creds['usda_quickstat_key']}
out = requests.get(
    url=URL + 'get_param_values',
    params=params)

# Estimate the count of variables since QuickStat has a cap
year_start = 1950
year_end = 2018
params = {"sector_desc": "CROPS",
          "commodity_desc": "CORN",
          "group_desc": "FIELD CROPS",
          "short_desc": ["CORN, GRAIN - ACRES HARVESTED",
                         "CORN, GRAIN - PRODUCTION, MEASURED IN BU"],
          "domain_desc": "TOTAL",
          "agg_level_desc": "STATE",
          "year": list(range(year_start, year_end)),
          "key": creds['usda_quickstat_key']}
out = requests.get(
    url=URL + 'get_counts',
    params=params)
est_rows = out.json()['count']
if est_rows > 50000:
    print("too many records, estimating {}, "
          "data call will fail".format(est_rows))
else:
    print('Estimated {} rows of data'.format(est_rows))

# Calling the desired output
usda_resp = requests.get(
    url=URL + 'api_GET',
    params=params)

assert usda_resp.status_code == 200

data = pd.DataFrame(usda_resp.json()['data'])

data.to_csv("state_level_{}_{}_corn_yield.csv".format(year_start, year_end))
