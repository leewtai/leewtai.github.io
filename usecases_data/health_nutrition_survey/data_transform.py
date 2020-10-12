import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt


exam = pd.read_sas("body_measures_2015_2016.xpt")
demo = pd.read_sas("demographic_2015_2016.xpt")
nhanes_exam_variable_map = {
    "SEQN": "id",
    "BMXWT": "weight_kg",
    "BMXHT": "height_cm"}

nhanes_demo_variable_map = {
    "SEQN": "id",
    # "WTINT2YR": "interview_weights",
    # "WTMEC2YR": "exam_weights",
    "RIDAGEYR": "age_years",
    "DMDYRSUS": "length_in_us",
    "DMDEDUC3": "education_if_minor",
    "DMDEDUC2": "education_if_adult",
    "RIDEXPRG": "pregnancy_status",
    "RIAGENDR": "gender2",  # 1 = male, 2 = female
    "DMDHHSIZ": "household_size",
    "DMDFMSIZ": "family_size",
    "DMDHREDU": "household_head_edu",
    "DMDHRMAR": "household_head_marital_status",
    "INDHHIN2": "household_income",
    "INDFMIN2": "family_income",
    "RIDRETH1": "reported_ethn"}
exam = exam[nhanes_exam_variable_map.keys()]
exam.rename(columns=nhanes_exam_variable_map, inplace=True)
demo = demo[nhanes_demo_variable_map.keys()]
demo.rename(columns=nhanes_demo_variable_map, inplace=True)
# This has the same row number as "exam"
df = demo.merge(exam, on=['id'], how='left')
df.to_csv("nhanes_2015_2015_demo.csv")

sns.distplot(df.weight_kg, kde=False)
plt.title('Body Mass Dist in NHANES 2015-2016 (Unweighted)')
plt.savefig('nhanes_2015_2016_weights_hist.png')
plt.close()

sns.scatterplot(x=df.height_cm, y=df.weight_kg, hue=df.gender2)
plt.title('Body Mass by Height in NHANES 2015-2016 (Unweighted)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.savefig('nhanes_2015_2016_weights_height_scatter.png')
plt.close()


age_cap = 18
youth = df.loc[df.age_years < age_cap, :]
sns.distplot(youth.weight_kg, kde=False)
plt.title('Body Mass Dist of Minors in NHANES 2015-2016 (Unweighted)')
plt.xlabel('Weight (kg)')
plt.savefig('nhanes_2015_2016_minor_weight_dist.png')
plt.close()

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg, hue=youth.gender2)
plt.title('Body Mass by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.savefig('nhanes_2015_2016_minor_weights_height_scatter.png')
plt.close()
