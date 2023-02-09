# Files from https://data.humdata.org/dataset/cod-ab-gtm?

import csv

import pandas as pd
import geopandas as gpd
from bs4 import BeautifulSoup


with open('/home/taiphoon/Downloads/Mayan Languages of Guatemala_ Interactive (EN) map_files/Dashboard1.html', 'r') as f:
    html = '\n'.join(f.readlines())

soup = BeautifulSoup(html)
lang_nodes = soup.find_all('div', 'tab-vizHeaderWrapper')
langs = [node.text for node in lang_nodes]

df = gpd.read_file('/home/taiphoon/Downloads/gtm_adm_ocha_conred_2019_SHP/gtm_admbnda_adm1_ocha_conred_20190207.shp')
df.shape
sdf = df.loc[:, ['ADM1_ES', 'geometry']]
sdf.head(3)
sdf.ADM1_ES.to_numpy()

pd.DataFrame(columns=sdf.ADM1_ES, index=langs).to_csv('mayan_lang_loss.csv', quoting=csv.QUOTE_NONNUMERIC)
