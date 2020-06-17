import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


age_cap = 18

sns.set()
df = pd.read_csv("../../../../usecases_data/health_nutrition_survey"
                 "/nhanes_2015_2015_demo.csv")
youth = df.loc[df.age_years < age_cap, :]
# non-representative sample
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


