import pandas as pd
from nltk.corpus import names

# files come from nltk.download()
male_names = [n.lower() for n in names.words('male.txt')]
female_names = [n.lower() for n in names.words('female.txt')]

df = pd.read_csv("nyc_payroll_2019.csv")
df.first_name = df.first_name.astype(str)


def id_gender(first_name):
    first_name = first_name.lower()
    if first_name in male_names:
        return 'm'
    elif first_name in female_names:
        return 'f'
    else:
        return 'other'


gender = df.apply(lambda x: id_gender(x['first_name']), 1)
gender.value_counts()

k = 15
gender.head(k)
df.first_name.head(k)
df['gender_from_name'] = gender

df.drop(columns=['payroll_number'],
        inplace=True)

titles = df.title_description.value_counts()
(titles < 50).mean()
rare_title = titles.loc[titles < 50].index
df['rare_title'] = df.apply(lambda x: x['title_description'] in rare_title, 1)

df.to_csv('processed_nyc_payroll_2019.csv', index=False)
