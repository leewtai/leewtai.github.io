import re
from glob import glob
import pandas as pd

import numpy as np

cw_file = 'spring2021/2021-04-28T1608_Grades-STATGR5206_001_2021_1_-_STAT_COMP_&_INTRO_DATA_SCIENCE.csv'
ed_files = glob('spring2021/HW*')


def calc_perc(scores, max_scores):
    overall_frac = sum(scores) / sum(max_scores)
    complete_frac = np.mean([i == j for i, j in zip(scores, max_scores) if j > 0])
    max_frac = max(overall_frac, complete_frac)
    hw_grade = 1 if max_frac >= 0.75 else max_frac
    return hw_grade



cw = pd.read_csv(cw_file)
edfs = []
for ef in ed_files:
    hw = pd.read_csv(ef, skiprows=1)
    poss_scores = pd.read_csv(ef, nrows=1, header=None)
    start_ind = np.where((poss_scores == 0).to_numpy())[1][0]
    max_scores = poss_scores.iloc[0, start_ind:]
    sum(max_scores)
    hw_start = np.where(hw.columns == 'total score')[0][0] + 1
    fracs = hw.apply(lambda x: calc_perc(x[hw_start:], max_scores), 1)
    unis = hw.apply(lambda x: re.sub('@.*', '', x['email']), 1)
    frac_name = re.sub('.*/([^ ]+) .*', '\\1', ef)
    edfs.append(pd.DataFrame({'uni': unis, frac_name: fracs}))

edf = edfs[0]
for i in range(len(edfs) - 1):
    edf = edf.merge(edfs[i + 1], how='outer', on='uni')

# Exceptions
edf.loc[edf.uni == 'e.sangal', 'uni'] = 'es3692'
## Zhonghao had a family emergency and I allowed him to submit late.
edf.loc[edf.uni == 'zx2337', 'hw3'] = 1

cw = cw.loc[:, ["Student", "ID", "SIS User ID", "SIS Login ID", "Section"]]
cw_upload = cw.merge(edf, how='left', left_on='SIS User ID', right_on='uni')

cw_upload.loc[cw_upload['Student'] == '    Points Possible', edf.columns[1:]] = 1
cw_upload = cw_upload.loc[:, ['Student', 'ID', 'SIS User ID', 'SIS Login ID',
                              'Section', 'uni', 'HW4', 'HW5']]
cw_upload.to_csv("ed_homework_upload_courseworks.csv", index=False)
