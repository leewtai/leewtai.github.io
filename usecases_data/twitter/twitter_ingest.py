from time import sleep
from itertools import product
from pathlib import Path

import json
from base64 import b64encode
from urllib.parse import quote

import requests

cred_file = Path('../credentials.json')
creds = json.load(cred_file.open('r'))
twitter_api_key = creds['twitter_api_key']
twitter_api_secret_key = creds['twitter_api_secret_key']

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
dates = ['%02d' % i for i in range(4, 10)]
twitter_handles = ['realDonaldTrump', 'JoeBiden', 'BarackObama']
out = []
for twitter_handle, date in product(twitter_handles, dates):
    params = {
        'query': 'from:{}'.format(twitter_handle),
        'start_time': '2020-11-{}T00:00:01Z'.format(date),
        'end_time': '2020-11-{}T23:59:59Z'.format(date),
        'expansions': 'author_id',
        'user.fields': 'name,entities,id,username,verified',
        'max_results': 100,
        'tweet.fields': 'author_id,created_at,entities,public_metrics',
    }

    response = requests.get(url=SEARCH_URL,
                            params=params,
                            headers=headers)
    assert response.status_code == 200
    if not response.json()['meta']['result_count']:
        continue
    out.extend(response.json()['data'])
    sleep(10)


json.dump(out, open('5206_twitter.json', 'w'))
