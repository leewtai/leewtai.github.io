import re

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('spring2021/2021-04-28T1633_Grades-STATGR5206'
                 '_001_2021_1_-_STAT_COMP_&_INTRO_DATA_SCIENCE.csv')
df = pd.read_csv('spring2021/2021-05-14T2053_Grades-STATGR5206'
                 '_001_2021_1_-_STAT_COMP_&_INTRO_DATA_SCIENCE.csv')

# Drop first row that tells us whether things were posted manually or automatically
df = df.iloc[1:,]
df.columns
df.head(3)

hw_cols = [col for col in df.columns if re.search('hw.*', col.lower())]
hw = df[hw_cols].astype(float)
hw.fillna(value=0, inplace=True)
hw_norm = hw.apply(lambda x: x.mean(), axis=1)

mid_cols = [col for col in df.columns if re.search('mid.*', col.lower())]
mid = df[mid_cols].astype(float)
mid.fillna(value=0, inplace=True)
mid_norm = mid.apply(lambda x: x/x.max()).iloc[:, 0]

# Everyone got 100% for the recording
fin_cols = [col for col in df.columns if re.search('final project \\(due.*', col.lower())]
fin = df[fin_cols].astype(float)
fin.fillna(value=0, inplace=True)
fin_norm = fin.apply(lambda x: x/x.max()).iloc[:, 0]

fin_graded_cols = [col for col in df.columns if re.search('final project.*peer', col.lower())]
fin_graded = df[fin_graded_cols].astype(float)
fin_graded.fillna(value=0, inplace=True)
fin_graded_norm = fin_graded.apply(lambda x: x/x.max()).iloc[:, 0]


lec_cols = [col for col in df.columns if re.search('(quiz|lec).*', col.lower())]
lec = df[lec_cols].astype(float)
lec.fillna(value=0, inplace=True)
lec_norm = lec.apply(lambda x: x/x.max())
lec_norm = lec_norm.apply(lambda x: x.mean(), axis=1)


# .1 is attendance, no one missed more than 50%
# 0.05 is for the recording for the final presentation
course_perc = hw_norm * .2 + .1 + mid_norm * 0.3 + fin_norm * 0.34 + 0.05 + 0.01 * fin_graded_norm
course_perc

grades = pd.concat((hw_norm, mid_norm, fin_norm, course_perc,
                    df[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['hw', 'mid', 'final', 'grades', 'uni', 'name']

grades.sort_values(by='grades', inplace=True)
grades['diff'] = grades.grades.diff()

cumden = [(grades.grades <= i).mean() for i in grades.grades]
plt.scatter(grades.grades, cumden)
plt.axvline(.86)
plt.axvline(.82)
plt.axvline(.77)
plt.savefig('grade_cumdistr.png')
plt.close()

grades['letters'] = ''
grades['letters_correct'] = ''
cutoffs2021 =             [1, 0.85, 0.8,   0.77, 0.7, 0.5, 0]
cutoffs2021_sans_racing = [1, 0.86, .82, 0.77, 0.65, 0.5, 0]
letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+']
for i, (t, b) in enumerate(zip(cutoffs2021[:-1], cutoffs2021[1:])):
    grades['letters'][(grades.grades <= t) & (grades.grades > b)] = letters[i]

for i, (t, b) in enumerate(zip(cutoffs2021_sans_racing[:-1], cutoffs2021_sans_racing[1:])):
    grades['letters_correct'][(grades.grades <= t) & (grades.grades > b)] = letters[i]


grades
