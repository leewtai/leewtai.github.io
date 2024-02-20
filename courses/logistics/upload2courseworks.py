import csv
import re
from glob import glob

import pandas as pd
import numpy as np


grade = pd.read_csv('data/gradescope_hw.csv')
grade_col = [col for dt, col in zip(grade.dtypes, grade.columns)
             if dt in ['float64', 'int64']]
len(grade_col)
print(grade.shape)

df = pd.DataFrame({'Uni': grade.SID})
df = df.loc[~df.Uni.isna(), :]

for i in range(8):
    q_cols = [col for col in grade_col if re.search(f'Homework {i}', col)]
    frac = grade[q_cols[0]] / grade[q_cols[1]]
    df = df.merge(pd.DataFrame({f'Homework{i}': frac, 'Uni': grade.SID}), how='left')

#total_col = [col for col in grade_col if re.search('total', col.lower())]
#
#if len(total_col) == 1:
#    total_col = total_col[0]
#    total = grade[total_col]
#else:
#    total = grade[grade_col].apply(lambda x: np.nansum(x), axis=1)
#
#df = pd.DataFrame({'Total': total, 'Uni': grade.UNI})

cw_export = pd.read_csv(glob('data/cw_export.csv')[0])
cw_export.head()

cw = cw_export[["Student", "ID", "SIS User ID", "SIS Login ID", "Section"]]
#cw_upload = cw.merge(df[['Uni', 'Total']], how='left', left_on='SIS User ID', right_on='Uni')
cw_upload = cw.merge(df, how='left', left_on='SIS User ID', right_on='Uni')

assert cw_upload.shape[0] <= cw.shape[0]
# cw_upload.loc[0, 'Total'] = 110
cw_upload.head()

cw_upload.to_csv('hw_grades.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
