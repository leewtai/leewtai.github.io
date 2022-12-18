import time
import json
from pathlib import Path

import requests


employer2stock = {
    "INFOSYS LIMITED": "INFY",
    "ACCENTURE LLP": "ACN",
    "NTT DATA": "NTDTY",
    "MICROSOFT": "MSFT",
    "AMAZON WEB SERVICES": "AMZN",
    "INTEL": "INTC",
    "NVIDIA": "NVDA",
    "ORACLE AMERICA": "ORCL",
    "QUALCOMM TECHNOLOGIES": "QCOM",
    "VMWARE": "VMW"
}

cred_file = Path('../credentials.json')
api_key = json.load(cred_file.open('r'))['alpha_vantage_api_key']
URL = "https://www.alphavantage.co/query"
params = {"function": "TIME_SERIES_MONTHLY_ADJUSTED",
          "symbol": "GDXJ",
          "apikey": api_key}

perf = {}
for empl in employer2stock:
    sym = employer2stock[empl]
    params.update({'symbol': sym})
    resp = requests.get(URL, params=params)
    perf.update({sym: resp.json()})
    time.sleep(30)


with open('stocks_monthly_adjusted.json', 'w') as f:
    json.dump(perf, f)
