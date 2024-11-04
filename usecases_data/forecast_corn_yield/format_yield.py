import pandas as pd
import numpy as np

dat = pd.read_csv('../usda_quick_stat/state_level_1950_2023_corn_yield.csv')

bad_cols = ['Unnamed: 0', 'state_ansi', 'state_fips_code', 'state_alpha',
            'statisticcat_desc', 'state_name']
cols_singular = dat.nunique() <= 1  # 0 values exist
bad_cols.extend(cols_singular[cols_singular].index)

dat.drop(columns=bad_cols, inplace=True)
print(dat.shape)
print(dat.columns)

vals = dat.Value.apply(lambda s: s.replace(',', ''))
vals = vals.apply(
    lambda x: np.nan
    if x == '0' or not x.isnumeric()
    else float(x))
dat.Value = vals

# Get year-month-day from time
dat.load_time = dat.load_time.str[:10]

dat.head(3)
assert dat.state_name.equals(dat.location_desc)
grps = dat.groupby(['short_desc', 'location_desc', 'year', 'load_time'])

form_data = {
    var: pd.DataFrame(data=np.nan,
                      index=list(range(dat.year.min(),
                                       dat.year.max())),
                      columns=dat.state_name.unique())
    for var in ['mass', 'area']}

# Resolve issue when there are multiple values per year/state combo
# a = iter(grps.groups.items())
# grp, inds = next(a)
for grp, inds in grps.groups.items():
    d = dat.iloc[inds]
    print(d.shape)
    if len(inds) > 1:
        is_census = d.source_desc == 'CENSUS'
        if any(is_census):
            val = d.Value[is_census].values[0]
        else:
            val = d.sort_values('load_time').Value.values[-1]
    else:
        val = d.Value.values[0]

    V = 'mass' if grp[2] == 'PRODUCTION' else 'area'
    form_data[V].loc[grp[1], grp[0]] = val


yld = form_data['mass'] / form_data['area']
yld.to_csv('yld_bu_ac.csv')
form_data['mass'].to_csv('mass_bu.csv')
form_data['area'].to_csv('area_ac.csv')
