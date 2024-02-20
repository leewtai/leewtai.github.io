import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.graphics import mosaicplot

df = pd.read_csv("processed_nyc_payroll_2021.csv")
df.columns


gdf = df.groupby("work_location_borough").count()['fiscal_year']

a = gdf.reset_index().rename(columns={"fiscal_year": "count"})
sns.barplot(data=a, x='work_location_borough', y='count')
plt.savefig("graphs/barplot_demo_borough.png")
plt.close()


gdf = df.groupby("gender_from_name").count()['fiscal_year']
a = gdf.reset_index().rename(columns={"fiscal_year": "count"})
sns.barplot(data=a, x='gender_from_name', y='count')
plt.savefig("graphs/barplot_demo_gender.png")
plt.close()

gdf = df.groupby("title_description").count()['fiscal_year']
a = gdf.reset_index().rename(columns={"fiscal_year": "count"})
sns.barplot(data=a, x='title_description', y='count')
plt.savefig("graphs/barplot_demo_title.png")
plt.close()

sns.histplot(data=df, x='base_salary')
plt.savefig("graphs/histplot_demo_salary.png")
plt.close()


df['compensation'] = df.regular_gross_paid + df.total_ot_paid + df.total_other_pay
df['compensation'] = np.where(df.compensation >=0, df.compensation, 0)
df['log_compensation'] = np.log(df.compensation + 1)
bins = [0, 20000, 60000, 80000, 100000, 150000, 200000, df.compensation.max() + 1]
# log_bins = [np.log(i + 1) for i in bins]
# ax = sns.histplot(x=df.log_compensation, bins=log_bins)
ax = sns.histplot(x=df.compensation, bins=bins, stat='density')
ax.set(xlabel="Compensation")
plt.savefig("graphs/histplot_demo_compensation.png")
plt.close()

cond = (df.compensation > bins[1]) & (df.compensation <= bins[2])
cond.mean()

cond = df.title_description == 'ELECTION WORKER'
cond.sum()
ax = sns.histplot(x=df.compensation[cond], stat='density')
ax.set(xlabel="Compensation of Election Workers")
plt.savefig("graphs/histplot_demo_compensation_filter.png")
plt.close()

df['is_election_worker'] = np.where(cond, "election", "not elect")
ax = sns.boxplot(data=df, x='compensation', y='is_election_worker')
plt.savefig("graphs/boxplot_demo.png")
plt.close()


