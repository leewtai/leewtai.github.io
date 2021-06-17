import json

import requests

cred = json.load(open('../credentials.json', 'r'))

params = {
    "agency_name": "Department of Housing Preservation and Development",
    "incident_zip": 11212,
    "$where": "created_date between '2020-01-01' and '2020-01-31'"}
# Detailed API docs
# https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9
URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

req_out = requests.get(url=URL, params=params)

dat = req_out.json()
json.dump(dat, open('housing.json', 'w'))
