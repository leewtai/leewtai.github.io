from itertools import product
import requests
import pandas as pd

# Need to include CTY_CODE to get data for "all countries"
BASE_URL = "https://api.census.gov/data/timeseries/intltrade/{ie}/enduse?"
URL = BASE_URL + ("get=CTY_NAME,{IE}_ENDUSE_LDESC,VES_VAL_MO,AIR_WGT_MO,"
                  "CNT_WGT_MO,CNT_VAL_MO,AIR_VAL_MO,CTY_CODE,{add_vars},"
                  "VES_WGT_MO,CC_MO,{IE}_ENDUSE&YEAR={yr}&MONTH={mo}")

# See https://api.census.gov/data/timeseries/intltrade/imports/enduse/variables.html
import_add_vars = ['CON_VAL_MO', 'GEN_VAL_MO']
# See https://api.census.gov/data/timeseries/intltrade/exports/enduse/variables.html
export_add_vars = ["ALL_VAL_MO"]

months = range(1, 13)
years = range(2019, 2020)
ies = ['imports', 'exports']

for ie, year, month in product(ies, years, months):
    if len(str(month)) == 1:
        month = '0' + str(month)
    if ie == "imports":
        ie_init = "I"
        add_vars = import_add_vars
    else:
        ie_init = "E"
        add_vars = export_add_vars
    resp = requests.get(URL.format(add_vars=",".join(add_vars),
                                   IE=ie_init, ie=ie, yr=year, mo=month))
    if resp.status_code != 200:
        print(resp.text)
        continue
    dat = resp.json()
    df = pd.DataFrame(dat[1:], columns=dat[0])
    df.to_csv("{ie}_{yr}_{mo}.csv".format(ie=ie, yr=year, mo=month))
