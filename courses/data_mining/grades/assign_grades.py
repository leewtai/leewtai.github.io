import re

import matplotlib.pyplot as plt
import pandas as pd

midterm_skip = ["mjd2283"]

canvas = pd.read_csv('courses/intro-stat/grades/2023-05-13T0142_Grades-STAT1101_Sec_2.csv')
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

partic_cols = [col for col in canvas.columns if re.search('.*(survey|quiz).*', col.lower())]
len(partic_cols)
partic = canvas[partic_cols].astype(float)
partic_norm = partic.apply(lambda x: x/x.max(), axis=0)
partic_norm.fillna(value=0, inplace=True)
partic_perc = partic_norm.apply(lambda x: x.mean(), axis=1)
partic_perc.loc[partic_perc >= 0.75] = 1

mid_cols = [col for col in canvas.columns if re.search('.*midterm.*', col.lower())]
mid = canvas[mid_cols].astype(float)
mid_norm = mid.apply(lambda x: x/x.max(), axis=0)
mid1 = mid_norm[mid_cols[0]]
mid2 = mid_norm[mid_cols[1]]

final = canvas[['Final (1052258)']].astype(float)
final_norm = final.apply(lambda x: x/x.max(), axis=0)
final = final_norm['Final (1052258)']

grades = pd.concat((hw_perc,
                    partic_perc,
                    mid1,
                    mid2,
                    final,
                    canvas[['SIS User ID', 'Student']]), axis=1)
grades.columns = ['hw', 'partic', 'mid1', 'mid2', 'final', 'uni', 'name']

grades['grades'] = grades.apply(lambda x:
    x['hw'] * 0.3 + x['mid1'] * 0.15
    + x['mid2'] * 0.15 + x['final'] * 0.35
    + x['partic'] * 0.05, axis=1)
grades['grades1'] = grades.apply(lambda x:
    x['hw'] * 0.3 + x['mid1'] * 0.075
    + x['mid2'] * 0.15 + x['final'] * 0.425
    + x['partic'] * 0.05, axis=1)
grades['grades2'] = grades.apply(lambda x:
    x['hw'] * 0.3 + x['mid1'] * 0.15
    + x['mid2'] * 0.075 + x['final'] * 0.425
    + x['partic'] * 0.05, axis=1)
special = grades.uni.isin(midterm_skip)
grades.loc[special, 'grades'] = grades[special].apply(lambda x:
    x['hw'] * 0.3 + x['mid1'] * 0
    + x['mid2'] * 0.15 + x['final'] * 0.5
    + x['partic'] * 0.05, axis=1)


grade_cols = [col for col in grades.columns if re.search('^grade.*', col)]
assert len(grade_cols) == 3

for gcol in grade_cols:
    grades.sort_values(by=gcol, inplace=True)

    cumden = [(grades[gcol] <= i).mean() for i in grades[gcol]]
    plt.scatter(grades[gcol], cumden)
    plt.axvline(0.805)
    plt.axvline(0.78)
    plt.axvline(0.71)
    # plt.axvline(0.7)
    # plt.axvline(0.6)
    # plt.axvline(0.5)
    plt.savefig(f'courses/intro-stat/grades/{gcol}_cumdistr.png')
    plt.close()
    grades[f'diff_{gcol}'] = grades[gcol].diff()

# Manual inspection
gcol = 'grades2'
grades.sort_values(by=gcol, inplace=True, ascending=False)
grades[['final', gcol, f'diff_{gcol}', 'name']].tail(30)

(grades[gcol] > 0.805).mean()
(grades[gcol] > 0.807).mean()
(grades[gcol] > 0.75).mean()
(grades[gcol] > 0.6).mean()
letters = {'0': 'A', '1': 'A-', '2': 'B+',
           '3': 'B', '4': 'B-', '5': 'C+',
           '6': 'C', '7': 'F', '': ''}
cutoffs2023 = {
    'grades': [1, 0.807, 0.77, 0.73, 0.7, 0.6, 0.5, 0],
    'grades1': [1, 0.807, 0.77, 0.74, 0.69, 0.6, 0.5, 0],
    'grades2': [1, 0.805, 0.78, 0.75, 0.7, 0.63, 0.57, 0.5, 0]
}

for gcol in grade_cols:
    grades[f'letters_{gcol}'] = ''
    for i, (t, b) in enumerate(zip(cutoffs2023[gcol][:-1], cutoffs2023[gcol][1:])):
        grades[f'letters_{gcol}'].loc[(grades[gcol] <= t) & (grades[gcol] > b)] = str(i)

ggcols = [f'letters_{col}' for col in grade_cols]
grades['best_letter'] = grades[ggcols].apply(lambda x: letters[x.min()], axis=1)
grades[['name', 'best_letter']]

grades['best_letter'].value_counts() / grades.shape[0]
grades.to_csv('courses/intro-stat/grades/best_grades.csv')