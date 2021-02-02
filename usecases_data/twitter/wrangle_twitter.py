from pathlib import Path
import json

import pandas as pd

data_path = Path('3106_twitter.json')
twitter = json.load(data_path.open('r'))

len(twitter)
type(twitter[0])

twitter[0].keys()
twitter[0]

sans_retweet = [r for r in twitter if not r['text'].startswith('RT')]

template = {
    "created_at": '',
    "text": '',
    "dc_flag": False,
    "inaug_flag": False,
    "steal_flag": False}

records = []
for tweet in sans_retweet:
    record = template.copy()
    lowered_text = tweet['text'].lower()
    record.update({
        'created_at': tweet['created_at'],
        'text': tweet['text'],
        'dc_flag': 'dc' in lowered_text,
        'inaug_flag': 'inaug' in lowered_text,
        'steal_flag': 'steal' in lowered_text})
    if not tweet.get('entities'):
        continue
    annotations = tweet.get('entities').get('annotations')
    if not annotations:
        continue
    for anno in annotations:
        record.update({anno['normalized_text'].lower(): anno['probability']})
    records.append(record)

df = pd.DataFrame(records)
non_zero = df.apply(lambda x: (x != 0).sum(), 0)
sdf = df.loc[:, non_zero > 50]
sdf.to_csv("non_retweets_dc_inaug_steal.csv")
