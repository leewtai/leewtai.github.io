import json
from pathlib import Path

import requests

cred_file = Path('../credentials.json')
api_key = json.load(cred_file.open('r'))['alpha_vantage_api_key']
URL = "https://www.alphavantage.co/query"
params = {"function": "TIME_SERIES_WEEKLY",
          "symbol": "GDXJ",
          "apikey": api_key}

resp = requests.get(URL, params=params)
gold = resp.json()

params.update({'symbol': "VOO"})
resp = requests.get(URL, params=params)
voo = resp.json()

