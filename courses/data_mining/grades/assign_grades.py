import re

import matplotlib.pyplot as plt
import pandas as pd

canvas = pd.read_csv('data/2021-04-28T1108_Grades-STATUN3106_001_2021_1_-_APPLIED_DATA_MINING.csv')
# Remove placeholder row that indicates whether data was manually entered
canvas = canvas.loc[1:, :]

hw_cols = [col for col in canvas.columns if re.search('homework.*', col.lower())]
hw = canvas[hw_cols].astype(float)
hw.fillna(value=0, inplace=True)
hw_norm = hw.apply(lambda x: x/x.max(), axis=0)


def calc_hw_avg(x):
    skip = 1
    return(x.sort_values()[skip:].mean())


hw_perc = hw_norm.apply(calc_hw_avg, 1)


projs_cols = [col for col in canvas.columns if re.search('proj.*', col.lower())]
projs = canvas[projs_cols].astype(float)
projs_perc = projs.apply(lambda x: x/x.max(), axis=0)

partic_cols = [col for col in canvas.columns if re.search('.*lec.*', col.lower())]
partic = canvas[partic_cols].astype(float)
partic_norm = partic.apply(lambda x: x/x.max(), axis=0)
partic_norm.fillna(value=0, inplace=True)
partic_perc = partic_norm.apply(lambda x: x.mean(), axis=1)
partic_perc.loc[partic_perc >= 0.48] = 1

grades = pd.concat((hw_perc,
                    partic_perc,
                    projs_perc,
                    canvas[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['hw', 'partic', 'proj1', 'proj2', 'proj3', 'uni', 'name']

grades['grades'] = grades.apply(lambda x:
    x['hw'] * 0.2 + x['proj2'] * 0.7 / 3
    + x['proj1'] * 0.7 / 3 + x['proj3'] * 0.7 / 3
    + x['partic'] * 0.1, axis=1)

grades.sort_values(by='grades', inplace=True)

cumden = [(grades.grades <= i).mean() for i in grades.grades]
plt.scatter(grades.grades, cumden)
plt.axvline(0.88)
plt.axvline(0.88)
plt.savefig('grade_cumdistr.png')
plt.close()

grades['diff'] = grades.grades.diff()
grades[['grades', 'diff']]

grades['letters'] = ''
cutoffs2019 = [1, 0.9, 0.86, 0.8, 0.75, 0.7, 0.5, 0]
letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
for i, (t, b) in enumerate(zip(cutoffs2019[:-1], cutoffs2019[1:])):
    grades['letters'][(grades.grades <= t) & (grades.grades > b)] = letters[i]

