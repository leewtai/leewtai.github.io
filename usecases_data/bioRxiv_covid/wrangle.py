from collections import Counter
from pathlib import Path
from random import randint
import json
import re

from nltk.tokenize.destructive import NLTKWordTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np


blacklist = stopwords.words('english')
stemmer = PorterStemmer()
tokenizer = NLTKWordTokenizer()


dat_file = Path('bioRxiv.json')
dat = json.load(dat_file.open('r'))
freqs = []


def clean_token(token):
    token = re.sub("\\.+$", "", token)
    if token.isalpha():
        out = stemmer.stem(token)
    elif not re.match('[a-zA-Z]', token):
        out = 'non_alpha'
    else:
        out = token
    return out


doc_index = []
for i, datum in enumerate(dat):
    if randint(1, 10) != 1:
        continue
    doc_index.append(i)
    doc = datum.get('rel_title') + ' ' + datum.get('rel_abs')
    tokens = tokenizer.tokenize(doc)
    cln_tokens = [clean_token(token) for token in tokens
                  if token not in blacklist and
                  (len(token) > 2 or token.isupper())]
    freqs.append(Counter(cln_tokens))

df = pd.DataFrame(freqs)
df.loc[:, 'doc_index'] = doc_index
df.fillna(value=0, inplace=True)
wd_use = df.apply(lambda x: sum(x > 0), axis=0)
# 4 is the 80th percentile
np.percentile(wd_use, np.arange(0, 101, 10))
unwanted = wd_use <= 10

df.drop(columns=unwanted.index[unwanted], inplace=True)
df.to_csv("sub_biorxiv_word_freq.csv")
# without cleaning non-alpha: (14180, 93480)
