import logging
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path

import json
from base64 import b64encode
from urllib.parse import quote

import requests

log_file = 'twitter_ingest.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)

cred_file = Path('../credentials.json')
creds = json.load(cred_file.open('r'))
twitter_api_key = creds['twitter_api_key']
twitter_api_secret_key = creds['twitter_api_secret_key']
OUTFILE = Path('3106_twitter.json')

SEARCH_URL = 'https://api.twitter.com/2/tweets/search/recent'

bearer_token = (quote(twitter_api_key)
                + ':'
                + quote(twitter_api_secret_key))
bearer_b64 = b64encode(bytes(bearer_token, 'utf-8')).decode('utf-8')

# Create the necessary inputs, in the right format to
# communicate with Twitter's API
auth_headers = {
    'Authorization': 'Basic {}' + bearer_b64,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
auth_response = requests.post(url='https://api.twitter.com/oauth2/token',
                              headers=auth_headers,
                              data={'grant_type': 'client_credentials'})
headers = {
    'Authorization': 'Bearer ' + auth_response.json()['access_token']
}
# These are the parameters to customize my query
twitter_queries = ['inauguration', 'StopTheSteaI2020', 'WashingtonDC']
if OUTFILE.exists():
    out = json.load(OUTFILE.open('r'))
    since_id = max(record['id'] for record in out)
else:
    out = []
    since_id = ''

max_results = 100

temp_out = []
for tq in twitter_queries:
    counter = 0
    max_diff = 0
    while counter < 50 and max_diff == 0:
        params = {
            'query': tq,
            'since_id': since_id,
            'user.fields': 'name,entities,id,username,verified',
            'max_results': 100,
            'tweet.fields': 'author_id,created_at,entities,public_metrics',
        }
        if not since_id:
            params.pop('since_id')
            start_time = datetime.utcnow() - timedelta(days=7, minutes=-1)
            end_time = datetime.utcnow() - timedelta(days=6)
            params.update({
                'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%SZ')})

        response = requests.get(url=SEARCH_URL,
                                params=params,
                                headers=headers)
        assert response.status_code == 200
        if not response.json()['meta']['result_count']:
            continue
        results = response.json()['data']
        max_diff = max_results - len(results)
        if max_diff != 0:
            logging.info('max results hit at {} for query {}'.format(
                counter * params['max_results'] + len(results), tq))
        counter += 1
        if counter == 50:
            logging.info('hit max iteration cap for query {}'.format(
                tq))
        temp_out.extend(results)
        since_id = max(record['id'] for record in results)
        sleep(0.1)


out.extend(temp_out)
json.dump(out, OUTFILE.open('w'))
