# Data is from https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub
# Super buggy!

import csv
import re
from glob import glob

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

fns = glob('data/h1b*')


int_cols = ['Initial Approval', 'Initial Denial', 'Continuing Approval',
            'Continuing Denial']


def process_h1b(h1b):
    fix = h1b.copy()
    for int_col in int_cols:
        fix[int_col] = h1b[int_col].astype(str)
        fix[int_col] = fix[int_col].str.replace(',', '')
        fix[int_col] = fix[int_col].astype(int)
    fix = fix.loc[fix.Employer.notna()]
    return fix


dfs = []
for fn in fns:
    df = pd.read_csv(fn)
    if int_cols[0] not in df.columns:
        df.rename(columns={col + 's': col for col in int_cols}, inplace=True)
    dfs.append(process_h1b(df))

h1b = pd.concat(dfs)
h1b.to_csv('h1b_datahubexport.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
# GOOGLE LLC vs GOOGLE INC
# h1b['Employer'] = h1b.Employer.apply(lambda x: re.sub(' INCORPORATED$', ' INC', x))
h1b['Employer'] = h1b.Employer.apply(lambda x: re.sub(' CORPORATION$', ' CORP', x))
h1b['Employer'] = h1b.Employer.apply(lambda x: re.sub(' (LLC|INC|CORP)$', '', x))
# LINKEDIN CORP vs LINKEDIN CORPORATION
h1b.shape

h1b.head(3)

h1b = h1b.groupby(['Fiscal Year', 'Employer']).sum()[int_cols].reset_index()
demo = h1b.groupby(['Fiscal Year']).sum()[int_cols].reset_index()

h1b.sample(10)
h1b.loc[(h1b.Employer.str.find('^INC') > -1) & (h1b['Fiscal Year'] == 2022)]
h1b.loc[h1b.Employer.apply(lambda x: re.search('^INC', x) is not None) & (h1b['Fiscal Year'] == 2022)]

demo = h1b.loc[h1b.Employer == 'GOOGLE']
demo
sns.scatterplot(data=demo, x='Fiscal Year', y='Continuing Approval')
plt.show()


elite = h1b.groupby('Employer').count()['Initial Approval'].reset_index()
elite.shape
elite.head(3)
elite.iloc[:, 1].max()
elite.loc[elite.Employer.str.find('LINKEDIN') > -1]
elite.loc[elite.Employer.str.find('AMAZON') > -1]
a = h1b.loc[h1b.Employer.str.find('LLC') > 0].iloc[4540:4560,:]





tokenizer = CountVectorizer()
presence = tokenizer.fit_transform(h1b.Employer).toarray() > 0
tokens = tokenizer.get_feature_names_out()
doc_freq = np.apply_along_axis(np.mean, 0, presence)
doc_freq.shape
tokens[np.where(doc_freq > 0.01)]


