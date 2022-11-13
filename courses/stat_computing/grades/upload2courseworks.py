import csv
import re

import pandas as pd
import numpy as np


grade = pd.read_csv('../data/Midterm_Fall_2022_grading - Sheet1.csv')
grade_col = [col for col in grade.columns if re.search('^Q[1-9]', col)]
len(grade_col)
weird_cols = [col for col in grade_col if grade.dtypes[col] != 'float']
grade.loc[grade[weird_cols[0]] == "Can't find file", weird_cols[0]] = np.nan
grade[weird_cols] = grade[weird_cols].astype(float)

# some questions got negative points
per_q_grade = {}
for i in range(1, 7):
    q_col = [col for col in grade_col if re.match(f'^Q{i}', col)]
    q_grade = grade[q_col].sum(axis=1).apply(lambda x: max(x, 0))
    per_q_grade.update({f'Q{i}': q_grade})
per_q_df = pd.DataFrame(per_q_grade)

total = per_q_df.apply(lambda x: np.nansum(x), axis=1)
per_q_df['Total'] = total
per_q_df['Uni'] = grade.Uni
# 40% students got higher grades
(total > grade.Total).mean()
(total - grade.Total).max()

cw_export = pd.read_csv('../data/2022-10-18T1457_Grades-STATGR5206.csv')
cw_export.head()

cw = cw_export[["Student", "ID", "SIS User ID", "SIS Login ID", "Section"]]
cw_upload = cw.merge(per_q_df[['Uni', 'Total']], how='left', left_on='SIS User ID', right_on='Uni')
assert cw_upload.shape[0] <= cw.shape[0]
cw_upload.loc[0, 'Total'] = 75
(cw_upload.Total >= 0).mean()  # NaN 2 students
cw_upload.head()

cw_upload.to_csv('midterm_grades.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
