import re
from glob import glob
import pandas as pd

import numpy as np

cw_file = glob('fall2023/2023-*.csv')[0]
ed_files = glob('fall2023/Homework*.csv')
ed_files = [fn for fn in ed_files if re.search('[45]', fn)]


def calc_perc(scores, max_scores):
    overall_frac = sum(scores) / sum(max_scores)
    # complete_frac = np.mean([i == j for i, j in zip(scores, max_scores) if j > 0])
    # max_frac = max(overall_frac, complete_frac)
    # hw_grade = 1 if max_frac >= 0.75 else max_frac
    return overall_frac #hw_grade


cw = pd.read_csv(cw_file)
edfs = []
col_names = []
for ef in ed_files:
    hw = pd.read_csv(ef, skiprows=2)
    is_score = hw.dtypes == 'int64'
    max_scores = hw.loc[:, is_score].max()
    sum(max_scores)
    fracs = hw.loc[:, is_score].apply(lambda x: calc_perc(x, max_scores), 1)
    assert (fracs > 0.5).mean() > 0.8
    unis = hw.iloc[:, 0]
    frac_name = re.sub('.*/([^ ]+ ?[0-9]) .*', '\\1', ef)
    col_names.append(frac_name)
    edfs.append(pd.DataFrame({'uni': unis, frac_name: fracs}))

edf = edfs[0]
for i in range(len(edfs) - 1):
    edf = edf.merge(edfs[i + 1], how='outer', on='uni')

# Exceptions
# edf.loc[edf.uni == 'e.sangal', 'uni'] = 'es3692'
## Zhonghao had a family emergency and I allowed him to submit late.
# edf.loc[edf.uni == 'zx2337', 'hw3'] = 1

cw = cw.loc[:, ["Student", "ID", "SIS User ID", "SIS Login ID", "Section"]]
cw_upload = cw.merge(edf, how='left', left_on='SIS User ID', right_on='uni')

cw_upload.loc[cw_upload['Student'] == '    Points Possible', edf.columns[1:]] = 1
std_cols = ['Student', 'ID', 'SIS User ID', 'SIS Login ID',
                              'Section', 'uni']
std_cols.extend(col_names)
cw_upload = cw_upload.loc[:, std_cols]
cw_upload.to_csv("ed_homework_upload_courseworks.csv", index=False)
