import re

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/2021-04-28T1109_Grades-STATUN2102'
                 '_001_2021_1_-_Applied_Statistical_Computing.csv')
# First row is a row indicating which were manually posted,
# does not have grades. Solely for Canvas
df = df.iloc[1:, ]
df.columns
df.head(3)

hw_cols = [col for col in df.columns if re.search('home.*', col.lower())]
hw = df[hw_cols].astype(float)
hw.fillna(value=0, inplace=True)
hw_norm = hw.apply(lambda x: x/x.max(), axis=0)


def calc_hw_avg(x):
    skip = 1
    return(x.sort_values()[skip:].mean())


hw_norm = hw_norm.apply(calc_hw_avg, 1)


mid_cols = [col for col in df.columns if re.search('mid.*', col.lower())]
mid = df[mid_cols].astype(float)
mid.fillna(value=0, inplace=True)
mid_norm = mid.apply(lambda x: x/x.max(), axis=0)
mid_norm = mid_norm.apply(lambda x: x.mean(), 1)

fin_cols = [col for col in df.columns if re.search('final exam.*', col.lower())]
fin = df[fin_cols].astype(float)
fin.fillna(value=0, inplace=True)
fin_norm = fin.apply(lambda x: x/x.max(), axis=0)
fin_norm = fin_norm.apply(lambda x: x.mean(), 1)

lec_cols = [col for col in df.columns if re.search('lec.*', col.lower())]
lec = df[lec_cols].astype(float)
lec.fillna(value=0, inplace=True)
lec_norm = lec.apply(lambda x: x/x.max(), axis=0)
lec_norm.loc[:, 'Lec18_free'] = 1
lec_norm = lec_norm.apply(lambda x: x.mean(), 1)
lec_norm.loc[lec_norm >= 0.4, ] = 1


course_perc = hw_norm * .15 + lec_norm * 0.05 + mid_norm * 0.5 + fin_norm * 0.3
course_perc

grades = pd.concat((lec_norm, hw_norm, mid_norm, fin_norm, course_perc,
                    df[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['partic', 'hw', 'mid', 'final', 'grades', 'uni', 'name']

# I told them that if they can pass the final, they will pass the class
fin_cuts = [1, 0.88, 0.78, 0.7, 0.58, 0.5, 0.38,0.2, 0]
fin_letters = ['4', '3.7', '3.3', '3', '2.7', '2', '1.7', '0']

grades['fin_letters'] = ''
for i, (t, b) in enumerate(zip(fin_cuts[:-1], fin_cuts[1:])):
    grades['fin_letters'][(grades.final <= t) & (grades.final > b)] = fin_letters[i]


# Repeated A category is to rid the people with programming experience already
cutoffs2021 = [1, 0.965, 0.945, 0.915, 0.895, 0.858, 0.82, 0.77, 0.65, 0.57, 0.4, 0]
letters = [     '4.3',   '4',   '4',   '3.7',  '3.3', '3',  '2.7',  '2.3', '2', '1.7', '0']
grades['letters'] = ''
for i, (t, b) in enumerate(zip(cutoffs2021[:-1], cutoffs2021[1:])):
    grades['letters'][(grades.grades <= t) & (grades.grades > b)] = letters[i]

grades['max_letters'] = grades.apply(lambda x: max(x['letters'], x['fin_letters']), 1)
gpa2letter = {'4.3': 'A+', '4': 'A', '3.7': 'A-',
              '3.3': 'B+', '3': 'B', '2.7': 'B-',
              '2.3': 'C+', '2': 'C', '1.7': 'C-',
              '0': 'F'}
grades.replace({'max_letters': gpa2letter}, inplace=True)


grades.to_csv('testb.csv')
