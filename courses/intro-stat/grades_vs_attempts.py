import csv
import re
from glob import glob

import pandas as pd

# Grab files that start with Homework in Downloads
h_files = glob('/Users/waynetailee/Downloads/Homework*.csv')

def get_attempt_num(f_name):
    df = pd.read_csv(f_name)
    gdf = df.groupby("sis_id").size().reset_index().rename(columns={0: "count"})
    return gdf

pre1, pre2 = [get_attempt_num(f) for f in h_files if re.search(r' [23] ', f)]
pre = pd.merge(pre1, pre2, on='sis_id', suffixes=('_1', '_2'))
pre['count'] = (pre['count_1'] + pre['count_2']) / 2

post1, post2 = [get_attempt_num(f) for f in h_files if re.search(r' [45] ', f)]
post = pd.merge(post1, post2, on='sis_id', suffixes=('_1', '_2'))
post['count'] = (post['count_1'] + post['count_2']) / 2

overall = pd.merge(pre, post, on='sis_id', suffixes=('_pre', '_post'))[['sis_id', 'count_pre', 'count_post']]
overall.head(4)

mid1 = pd.read_csv('grades/midterm_grades.csv')[['SIS User ID', 'Total']]
mid1['Total'] = mid1.Total / mid1.max()[0] * 100

overall = overall.merge(mid1, left_on='sis_id', right_on='SIS User ID').drop(columns=['SIS User ID'])
overall.head(4)

overall = overall[overall.Total > 0]
overall.head(3)

survey = pd.read_csv("/Users/waynetailee/Downloads/Survey 1 Survey Student Analysis Report.csv")
survey = survey[["sis_id",
                 "1213717: Do you rather be famous\n\nonly when you're alive or\nforever after you're dead\n",
                 '1213720: Do you like dogs or cats more?',
                 '1213721: How much do you think your first take-home "real" paycheck will be once you\'re done with school?']].copy()
survey.columns = ['sis_id', 'fame', 'pet', 'paycheck']
survey['pet'] = survey.pet.fillna("Neither")
survey['fame'] = survey.fame.fillna("Neither")
survey['paycheck'] = survey.paycheck.fillna("0")
survey['paycheck'] = survey.paycheck.str.replace(',', '').astype(float)

survey.dtypes
survey.head(3)

df = pd.merge(overall, survey, on='sis_id')
df.head(3)

df.to_csv("attempts_vs_midterm1.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)