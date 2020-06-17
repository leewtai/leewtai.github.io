import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm


age_cap = 18

sns.set()
df = pd.read_csv("../../../../usecases_data/health_nutrition_survey"
                 "/nhanes_2015_2015_demo.csv")
# We intentionally choose the minors to avoid the extreme bimodal distribution
# that might confuse the students. We also ignore the "sampling weights" in
# NHANES
youth = df.loc[df.age_years < age_cap, :]
sns.distplot(youth.weight_kg, kde=False)
plt.title('Weight Dist of Minors in NHANES 2015-2016 (Unweighted)')
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/nhanes_weight_dist.png')
plt.close()

sns.distplot(youth.weight_kg, kde=False)
plt.title('Weight Dist of Minors in NHANES 2015-2016 (Unweighted)')
plt.vlines(x=[youth.weight_kg.mean() + np.random.uniform(-3, 3, 2),
              youth.weight_kg.median() + np.random.uniform(-3, 3, 2)],
           ymin=-1, ymax=450)
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/nhanes_weight_dist_with_guesses_for_center.png')
plt.close()

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter.png')
plt.close()

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
lin_loc = [youth.height_cm.min(), youth.height_cm.max()]
lin_y = [youth.weight_kg.mean() for x in lin_loc]
plt.plot(lin_loc, lin_y)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter_with_avg.png')
plt.close()

X = sm.add_constant(youth.height_cm)
ols = sm.OLS(youth.weight_kg, X, missing='drop').fit()
lin_y = [ols.params[0] + ols.params[1] * x for x in lin_loc]

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
plt.plot(lin_loc, lin_y)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter_with_ols.png')
plt.close()


