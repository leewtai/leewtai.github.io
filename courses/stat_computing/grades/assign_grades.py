import re

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/2020-12-26T1147_Grades-STATGR5206_003_2020_3_'
                 '-_STAT_COMP_&_INTRO_DATA_SCIENCE.csv')
df = pd.read_csv('data/20201226_132800_courseworks.csv')
df.columns
df.head(3)

hw_cols = [col for col in df.columns if re.search('hw.*', col.lower())]
hw = df[hw_cols].astype(float)
hw.fillna(value=0, inplace=True)
hw_norm = hw.apply(lambda x: x.mean(), axis=1)

mid_auto = df['midterm']
mid_manual = df['midterm_twitter']
mid_man_norm = mid_manual / mid_manual.max()
mid_norm = (mid_auto.astype(float) * 2 + mid_man_norm) / 3

final_auto = df['final']
final_manual = df['final_business']
final_man_norm = final_manual / final_manual.max()
final_norm = (final_auto.astype(float) + final_man_norm) / 2

# .1 is attendance, no one missed more than 50%
course_perc = hw_norm * .2 + .1 + mid_norm * 0.35 + final_norm * 0.35
course_perc

grades = pd.concat((hw_norm, mid_norm, final_norm, course_perc,
                    df[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['hw', 'mid', 'final', 'grades', 'uni', 'name']

grades.sort_values(by='grades', inplace=True)
cumden = [(grades.grades <= i).mean() for i in grades.grades]
plt.scatter(grades.grades, cumden)
plt.axvline(0.8)
plt.axvline(0.65)
plt.axvline(0.58)
plt.savefig('grade_cumdistr.png')
plt.close()

grades
