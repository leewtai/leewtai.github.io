import csv
import re
from glob import glob

import pandas as pd
from nltk.corpus import names


df_fns = glob("nyc_payroll_*.csv")

# files come from nltk.download()
male_names = [n.lower() for n in names.words('male.txt')]
female_names = [n.lower() for n in names.words('female.txt')]

def id_gender(first_name, male_names, female_names):
    first_name = first_name.lower()
    is_male = first_name in male_names
    is_female = first_name in female_names
    if is_male and not is_female:
        return 'male'
    elif not is_male and is_female:
        return 'female'
    elif is_male and is_female:
        return 'both'
    else:
        return 'other'


def process_nyc_payroll(df):
    df.drop(columns=['payroll_number', 'agency_name',
                     'fiscal_year', 'base_salary'], inplace=True)
    bad_pay = ((df.regular_gross_paid < 0)
                | (df.total_ot_paid < 0)
                | (df.total_other_pay < 0))
    df = df.loc[~bad_pay, :].copy()
    df['total_pay'] = df.regular_gross_paid + df.total_ot_paid + df.total_other_pay
    df['regular_pay_to_total'] = df.regular_gross_paid / df.total_pay
    df['ot_pay_to_total'] = df.total_ot_paid / df.total_pay
    df['total_hours'] = df.regular_hours + df.ot_hours
    df['ot_hours_to_total'] = df.ot_hours / df.total_hours
    df['hourly_wage'] = df.total_pay / df.total_hours
    df['is_chief_or_captain'] = df.title_description.apply(lambda x: 1 if re.search("(captain|chief)", x.lower()) is not None else 0)
    return df
    

dfs = {fn: process_nyc_payroll(pd.read_csv(fn)) for fn in df_fns}
dfy1 = dfs['nyc_payroll_2019.csv']
dfy2 = dfs['nyc_payroll_2020.csv']
dfy3 = dfs['nyc_payroll_2021.csv']

dfy1.columns
dfy2.columns
dfy3.columns
# There are 2 Jose A Perez who started on 1996, 07, 21
# They're in different boroughs with different titles
# but many people changed boroughs and titles
# Removing the 2 people to avoid complicating things
merge_cols = ['last_name', 'first_name', 'mid_init', 'agency_start_date']
is_dup_y1 = dfy1[merge_cols].duplicated()
is_dup_y1.sum()
profile = dfy1.loc[is_dup_y1, merge_cols]
profile
target = (dfy1.first_name.isin(profile.first_name)
          & dfy1.last_name.isin(profile.last_name)
          & dfy1.agency_start_date.isin(profile.agency_start_date))
target.sum()

dfy1.drop(columns=['leave_status_as_of_july_31'], inplace=True)
dfy2.drop(columns=['pay_basis'], inplace=True)
dfy1 = dfy1.loc[~target, :]
mdf = dfy1.merge(dfy2, on=merge_cols,
    how='left', suffixes=['_y1', '_y2'])
assert mdf.shape[0] == dfy1.shape[0]
mdf['left_y2'] = (mdf.leave_status_as_of_july_31.isna() | (mdf.leave_status_as_of_july_31 != 'ACTIVE')) * 1
mdf.drop(columns=['leave_status_as_of_july_31'], inplace=True)

mdf['title_changed'] = (mdf.title_description_y1 != mdf.title_description_y2) * 1
mdf['borough_changed'] = (mdf.work_location_borough_y1 != mdf.work_location_borough_y2) * 1
mdf['hourly_wage_percent_change'] = (mdf.hourly_wage_y2 - mdf.hourly_wage_y1) / mdf.hourly_wage_y1 * 100
mdf['total_hours_percent_change'] = (mdf.total_hours_y2 - mdf.total_hours_y1) / mdf.total_hours_y1 * 100
mdf['total_pay_percent_change'] = (mdf.total_pay_y2 - mdf.total_pay_y1) / mdf.total_pay_y1 * 100

good_cols = dfy3.columns.intersection(merge_cols + ['leave_status_as_of_july_31'])
dfy3 = dfy3[good_cols]

mdf.shape
bdf = mdf.merge(dfy3, on=merge_cols, how='left')
assert mdf.shape[0] == bdf.shape[0]
bdf['left_y3'] = (bdf.leave_status_as_of_july_31.isna() | (bdf.leave_status_as_of_july_31 != 'ACTIVE')) * 1
bdf['gender_from_name'] = bdf.apply(lambda x: id_gender(x['first_name'], male_names, female_names), 1)
bdf.drop(columns=['leave_status_as_of_july_31'], inplace=True)

mdf['agency_start_date'] = pd.to_datetime(mdf.agency_start_date.str[:10])
mdf['tenure_days'] = (pd.to_datetime('2023-11-20') - mdf.agency_start_date).dt.days
mdf.tenure_days.head(10)

bdf.shape
bdf.to_csv('mid2_payroll.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
