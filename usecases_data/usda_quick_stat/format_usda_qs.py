import pandas as pd
import numpy as np

data = pd.read_csv("state_level_1950_2018_corn_yield.csv")
vals = data.Value.apply(lambda s: s.replace(',', ''))
vals = vals.apply(
    lambda x: np.nan
    if x == '0' or not x.isnumeric()
    else float(x))
data.Value = vals

data = data[data.state_name != 'OTHER STATES'].reset_index()
data = data[['Value', 'state_name', 'year',
             'statisticcat_desc', 'load_time', 'source_desc']]
grps = data.groupby(['state_name', 'year', 'statisticcat_desc'])

form_data = {
    var: pd.DataFrame(data=np.nan,
                      index=list(range(data.year.min(),
                                       data.year.max())),
                      columns=data.state_name.unique())
    for var in ['mass', 'area']}

# Resolve issue when there are multiple values per year/state combo
for grp, inds in grps.groups.items():
    d = data.iloc[inds]
    if len(inds) > 1:
        is_census = d.source_desc == 'CENSUS'
        if any(is_census):
            val = d.Value[is_census].values[0]
        else:
            val = d.sort_values('load_time').Value.values[-1]
    else:
        val = d.Value.values[0]

    v = 'mass' if grp[2] == 'PRODUCTION' else 'area'
    form_data[v].loc[grp[1], grp[0]] = val


yld = form_data['mass'] / form_data['area']
yld.to_csv('yld_bu_ac.csv')
form_data['mass'].to_csv('mass_bu.csv')
form_data['area'].to_csv('area_ac.csv')
