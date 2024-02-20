from glob import glob
from datetime import datetime
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

course = 'reg'
semester = f'fall{datetime.today().year}'
fn = glob(f'data/{semester}_{course}_grades.csv')
assert len(fn) == 1
df = pd.read_csv(fn[0])

# Drop first row that tells us whether things were posted manually or automatically
df = df.iloc[1:,]
df.columns
df.head(3)


def lowest_dropped_mean(x, k=1):
    return x.sort_values()[k:].mean()


hw_cols = [col for col in df.columns if re.search('homework.*', col.lower())]
hw = df[hw_cols].astype(float)
hw.fillna(value=0, inplace=True)
hw.iloc[5, -2] = 1
hw_norm = hw.apply(lowest_dropped_mean, axis=1)

mid_cols = [col for col in df.columns if re.search('^mid.*', col.lower())]
mid = df[mid_cols].astype(float)
mid.fillna(value=0, inplace=True)
mid_norm = mid / np.ones(mid.shape).dot(np.diag([40, 95]))

# Everyone got 100% for the recording
fin_cols = [col for col in df.columns if re.search('^final .*', col.lower())]
fin = df[fin_cols].astype(float)
fin.fillna(value=0, inplace=True)
fin_norm = fin.apply(lambda x: x/110).iloc[:, 0]

lec_cols = [col for col in df.columns if re.search('(survey|quiz|lec).*', col.lower())]
lec = df[lec_cols].astype(float)
lec.fillna(value=0, inplace=True)
# One free survey for everyone
# lec['free_survey'] = 1
lec_norm = lec.apply(lambda x: x/x.max())
lec_norm = lec_norm.apply(lambda x: x.mean(), axis=1)
lec_norm[lec_norm >= 0.75] = 1


# .1 is attendance, no one missed more than 50%
# 0.05 is for the recording for the final presentation
mid_weighted = mid_norm.dot(np.diag([0.15, 0.3])).apply(sum, axis=1)

course_perc = hw_norm * .15 + mid_weighted  + fin_norm * 0.35 + 0.05 * lec_norm
# Brian L is index 20
i = 20
course_perc[i]
mid_weighted[i] = mid_norm.iloc[20, 0] * 0.15
hw_norm[i] * .15 + mid_weighted[i] + fin_norm[i] * 0.65 + 0.05 * lec_norm[i]
course_perc.iloc[5]

grades = pd.concat((lec_norm, hw_norm, mid_weighted,
                    fin_norm, course_perc,
                    df[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['participation', 'hw', 'mid',
                  'final', 'grades', 'uni', 'name']

grades.sort_values(by='grades', inplace=True)
grades['diff'] = grades.grades.diff()

grades

cumden = [(grades.grades <= i).mean() for i in grades.grades]
plt.scatter(grades.grades, cumden)
plt.axvline(.83)
plt.axvline(.77)
plt.axvline(.75)
plt.axvline(.7)
plt.savefig('grade_cumdistr.png')
plt.close()

grades['letters'] = ''
grades['letters_curved'] = ''

cutoffs_curved = [1, 0.87, .83, 0.77, 0.7, 0.6, 0.5, 0] # 0.6 was 0.7 before
cutoffs_naive = [1, 0.93, 0.9, 0.87, 0.83, 0.8, 0.6, 0]
letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'F']

for i, (t, b) in enumerate(zip(cutoffs_curved[:-1], cutoffs_curved[1:])):
    grades['letters_curved'][(grades.grades <= t) & (grades.grades > b)] = letters[i]

for i, (t, b) in enumerate(zip(cutoffs_naive[:-1], cutoffs_naive[1:])):
    grades['letters'][(grades.grades <= t) & (grades.grades > b)] = letters[i]


grades.letters_curved.value_counts() / grades.shape[0]
