import re
from itertools import product
from glob import glob
import pandas as pd
import numpy as np

csvs = glob('data/csvs/*tmax.csv')


def process_csvs(csv):
    station_id = re.sub('.*/(USH[^\.]+).*', '\\1', csv)
    df = pd.read_csv(csv)
    years = df.year
    val_cols = [col for col in df.columns if col.startswith('value')]
    sort_cols = sorted(val_cols, key=lambda x: int(x.replace('value', '')))
    vals = df.loc[:, sort_cols]
    vals.replace(-9999, np.nan, inplace=True)
    flat_vals = vals.to_numpy().reshape(-1) / 100
    year_month = ['{:04d}_{:02d}'.format(year, month + 1)
                  for year, month in product(years, range(12))]
    return pd.DataFrame({'year_month': year_month, station_id: flat_vals})


dfs = [process_csvs(csv) for csv in csvs]

bdf = dfs[0]
for df in dfs[1:]:
    bdf = bdf.merge(df, how='outer',
                    on='year_month')

bdf.sort_values(by='year_month', inplace=True)
bdf.to_csv('ushcn.csv', index=False)
