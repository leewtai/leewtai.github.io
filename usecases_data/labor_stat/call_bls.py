import json

import requests

cred = json.load(open('../credentials.json', 'r'))

url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# ,
# CWUS0000SA0: CPI for Urban Wage Earners and Clerical Workers (adjusted)
# LNS14000000: Unemployment Rate (Seasonally Adjusted)
headers = {
    'registrationkey': cred['bureau_of_labor_stat_api_key'],
    'Content-type': 'application/json'
}

params = {
    'startyear': 2000,
    'endyear': 2020,
    'seriesid': ['LNS14000000', 'CWUS0000SA0']}

out = requests.post(url=url, data=json.dumps(params), headers=headers)
assert out.status_code == 200

dat = out.json()
assert len(dat['Results']['series']) == len(params['seriesid'])

filename = 'unemployment_cpi_unempl_{}_{}.json'.format(
    params['startyear'], params['endyear'])
json.dump(dat, open(filename, 'w'))
