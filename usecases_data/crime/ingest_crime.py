from pathlib import Path
import json
import logging
import time

import requests

log_file = 'data_gov.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)

cred_file = Path("../credentials.json")
cred = json.load(cred_file.open('r')).get('data_gov_api_key')

with Path('state_abbr.txt').open('r') as f:
    states = [f.read(2) for _ in f]

url = ("https://api.usa.gov/crime/fbi/sapi/api/summarized/state"
       "/{state_abbr}/{offense}/{since_year}/{until_year}")
params = {"api_key": cred}
# Offense types are: bulglary, larceny, motor-vehicle-theft, homocide,
# rape, robbery, arson, violent-crime, property-crime

all_dat = {}
for state in states:
    logging.info('processiong state {}'.format(state))
    state_dat = []
    params.update({'page': 0})
    formatted_url = url.format(
        state_abbr=state,
        offense='violent-crime',
        since_year=2010,
        until_year=2019)

    while True:
        resp = requests.get(formatted_url, params=params)
        if resp.status_code != 200:
            logging.error("Non-200 status at page {}", params.get('page'))
            break

        dat = resp.json()
        state_dat.extend(dat.get('results'))
        if params.get('page') == dat.get('pagination').get('pages'):
            logging.info("Finish all pages")
            break
        params.update({'page': params.get('page') + 1})
        time.sleep(1)

    all_dat.update({state: state_dat})

json.dump(all_dat, Path('state_crime.json').open('w'))
oris = {val['ori'] for dat in all_dat.values()
        for val in dat}

agency_url = "https://api.usa.gov/crime/fbi/sapi/api/agencies/{ori}"
params.pop('page')
all_ori = []
for ori in oris:
    if len(all_ori) % 500 == 0:
        logging.info("all ori progress at {} out of {}".format(
            len(all_ori), len(oris)))
    attempt = 0
    while attempt < 4:
        resp = requests.get(agency_url.format(ori=ori), params=params)
        if resp.status_code == 200:
            all_ori.append(resp.json())
            break
        elif attempt == 3:
            logging.error('ORI {} had non-200 status'.format(ori))
        attempt += 1
    time.sleep(0.5)

json.dump(all_ori, Path('all_ori_metadata.json').open('w'))
