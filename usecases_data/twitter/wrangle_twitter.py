from csv import QUOTE_NONNUMERIC
from collections import Counter
from pathlib import Path
import json
import re

import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

stopword_list = stopwords.words('english')
tokenizer = TweetTokenizer()
stemmer = PorterStemmer()
data_path = Path('3106_twitter.json')
twitter = json.load(data_path.open('r'))

len(twitter)
type(twitter[0])

twitter[0].keys()
twitter[0]

sans_retweet = [r for r in twitter if not r['text'].startswith('RT')]
del twitter


def twitter_symbol_conversion(token):
    token = re.sub('^@', 'AT_', token)
    token = re.sub('^#', 'HASHTAG_', token)
    return token


def process_tweet(tweet):
    tweet = re.sub('(washingtonDC|washingtondc|WashingtonDC|Washington DC|DC)',
                   'washington_dc', tweet)
    tokens = tokenizer.tokenize(tweet.lower())
    lwt = [twitter_symbol_conversion(stemmer.stem(token))
           for token in tokens
           if (len(re.sub('[^\\w]', '', token)) > 2 and
               token not in stopword_list)]
    return Counter(lwt)


records = []
counter = 0
for tweet in sans_retweet:
    counter += 1
    if counter % 3 != 0:
        continue
    text = tweet['text']
    proc_text = process_tweet(text)
    if len(proc_text) < 8:
        continue
    record = {
        "retweet_count": tweet['public_metrics']['retweet_count'],
        "reply_count": tweet['public_metrics']['reply_count'],
        "like_count": tweet['public_metrics']['like_count'],
        'created_at': tweet['created_at'],
        'tweet_body': text,
        **dict(proc_text)}
#     if not tweet.get('entities'):
#         continue
#     annotations = tweet.get('entities').get('annotations')
#     if annotations:
#         for anno in annotations:
#             record.update({anno['normalized_text'].lower(): anno['probability']})
#     mentions = tweet.get('entities').get('mentions')
#     if mentions:
#         for mention in mentions:
#             record.update({mention['username'].lower(): 1})
#     if not annotations and not mentions:
#         continue
    records.append(record)

df = pd.DataFrame(records)
df.fillna(value=0, inplace=True)
non_zero = df.apply(lambda x: (x != 0).sum(), 0)
sdf = df.loc[:, non_zero > 50]
sdf.to_csv("non_retweets_dc_inaug_steal.csv", index=False,
           quoting=QUOTE_NONNUMERIC)
