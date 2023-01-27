import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_stata('individual_v11_new.dta')
samp_countries = df.groupby('country').count().reset_index().sample(8, random_state=1101)['country']
samp_countries

cond = df.country.apply(lambda x: x in samp_countries.to_numpy())

df = df.loc[cond, :].sort_values('country')
df.corr()
x_var = 'patience'
y_var = 'posrecip'

agg_df = df.groupby('country').mean().reset_index()
agg_df.corr()


ind_corr = round(df[[x_var, y_var]].corr().iloc[0, 1], 2)
agg_corr = round(agg_df[[x_var, y_var]].corr().iloc[0, 1], 2)

fig, axes = plt.subplots(1, 2, sharex=True, figsize=(12, 6))
sns.scatterplot(data=df, x=x_var, y=y_var, hue='country', ax=axes[0])
axes[0].set_title(f'Ind level data Corr is {ind_corr}')
sns.scatterplot(data=agg_df, x=x_var, y=y_var, hue='country', ax=axes[1])
axes[1].set_title(f'Country level data Corr is {agg_corr}')
plt.savefig('ecological_fallacy_demo.png')
plt.close()


(np.abs(df.corr()) > 0.1) & (np.sign(df.corr()) != np.sign(agg_df.corr()))

x_var = 'subj_math_skills'
y_var = 'altruism'
b = df.corr()
a = df.loc[df.country == 'Japan', :].corr()
(np.sign(a) != np.sign(b)) & (np.abs(a) > 0.1)
df.groupby('country')[[x_var, y_var]].corr()
