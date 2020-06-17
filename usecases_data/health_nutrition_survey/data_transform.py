import pandas as pd


exam = pd.read_sas("body_measures_2015_2016.xpt")
demo = pd.read_sas("demographic_2015_2016.xpt")
nhanes_exam_variable_map = {
    "SEQN": "id",
    "BMXWT": "weight_kg",
    "BMXHT": "height_cm"}

nhanes_demo_variable_map = {
    "SEQN": "id",
    "WTINT2YR": "interview_weights",
    "WTMEC2YR": "exam_weights",
    "RIDAGEYR": "age_years",
    "RIAGENDR": "gender2",  # 1 = male, 2 = female
    "RIDRETH1": "reported_ethn"}
exam = exam[nhanes_exam_variable_map.keys()]
exam.rename(columns=nhanes_exam_variable_map, inplace=True)
demo = demo[nhanes_demo_variable_map.keys()]
demo.rename(columns=nhanes_demo_variable_map, inplace=True)
# This has the same row number as "exam"
df = demo.merge(exam, on=['id'], how='left')
df.to_csv("nhanes_2015_2015_demo.csv")

