# To run this, I like to use the following packages
# conda create -n nlp python=3.5 nltk gensim ipykernel

import json

from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()


# Load the congress bill data
bills = json.load(open("bills.json", "r"))
# Filter the data after the 113th congress
bills = {key: bill for key, bill in bills.items()
         if int(key[:3]) >= 110}

# Tokenize the bill text into tokens
stop_words = set(stopwords.words('english'))
common_texts = []
for bill in bills:
    tokens = tokenizer.tokenize(bills[bill][1])
    text_sans_stop_words = [t.lower()
                            for t in tokens
                            if t not in stop_words]
    common_texts.append(text_sans_stop_words)

# Fit word2vec model
ex_mod = Word2Vec(common_texts, sg=1)
word_vecs = ex_mod.wv

# See here for methods:
# https://radimrehurek.com/gensim/models/keyedvectors.html
word_vecs.most_similar('abortion')
word_vecs.most_similar('mother')
word_vecs.most_similar('orientation')
word_vecs.similar_by_vector(word_vecs['immigration'] - word_vecs['legal'])
