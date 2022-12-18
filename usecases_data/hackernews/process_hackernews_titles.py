import re

import pandas as pd

pattern = re.compile(r'([0-9]+),([0-9]+),([0-9]+),([0-9]+),(.*)')

dat = []
with open('hackernews_titles.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        datum = [pattern.sub(f'\\{i}', line).strip() for i in range(1, 6)]
        dat.append(datum)

cols = ['id', 'year', 'month', 'day', 'title']
df = pd.DataFrame(dat, columns=cols)
for i in cols[:4]:
    df[i] = df[i].astype(int)


lower_title = df.title.str.lower()
pattern = re.compile(r'\b(layoff|firing|severance|unemployment)s?\b')
df['has_key'] = lower_title.apply(lambda x: pattern.search(x) is not None)
grp_vars = ['year', 'month', 'day']
df_grp = df.groupby(grp_vars)

bag = []
for grp, ind in df_grp.groups.items():
    # grp, ind = next(iter(df_grp.groups.items()))
    sdf = df.loc[ind, :]
    out = {k: v for k, v in zip(grp_vars, grp)} # sdf.has_key.count()
    out.update({
        'n': sdf.has_key.count(),
        'avg': sdf.has_key.mean()})
    bag.append(out)

layoff_df = pd.DataFrame(bag)

has_key = (df.title.str.lower().str.find('layoff') > 0)
has_key = (df.title.str.lower().str.find('firing') > 0)
has_key = (df.title.str.lower().str.find('severance') > 0)
has_key = (df.title.str.lower().str.find('unemployment') > 0)
has_key = (df.title.str.lower().str.find('sack') > 0)
has_key.sum()
df.loc[has_key, :]
df.head()
df.tail()
df.iloc[2876, 4]
