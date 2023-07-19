# Files from https://data.humdata.org/dataset/cod-ab-gtm?

import csv

import pandas as pd
import geopandas as gpd
from bs4 import BeautifulSoup

# https://public.tableau.com/app/profile/eric.deluca/viz/GuatemalaMayanlanguagesmap/Dashboard1
with open('data/Dashboard1.html', 'r') as f:
    html = '\n'.join(f.readlines())

soup = BeautifulSoup(html)
lang_nodes = soup.find_all('div', 'tab-vizHeaderWrapper')
langs = [node.text for node in lang_nodes]

gdf = gpd.read_file('data/gtm_adm_ocha_conred_2019_SHP/gtm_admbnda_adm1_ocha_conred_20190207.shp')
gdf.shape
sdf = gdf.loc[:, ['ADM1_ES', 'geometry']]
sdf.head(3)
sdf.ADM1_ES.to_numpy()

pd.DataFrame(columns=sdf.ADM1_ES, index=langs).to_csv('data/mayan_lang_loss.csv', quoting=csv.QUOTE_NONNUMERIC)

# https://docs.google.com/spreadsheets/d/18kB5OyebrS-iMg8TS9i6a6__SMkVy93TJWSr5MO2_wM/edit?usp=sharing
df = pd.read_csv('data/mayan_language_count.csv')
df.rename(columns={'Unnamed: 0': 'Language'}, inplace=True)

assert (df.Language == langs).all()
dft = df.T.iloc[1:, :]
dft.head(3)
dft.columns = langs
dft = dft.reset_index()
dft.rename(columns={'index': 'ADM1_ES'}, inplace=True)
sdf = sdf.merge(dft, on='ADM1_ES')
sdf.head(3)
type(sdf)

sdf.to_csv('data/mayan_language_map.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
