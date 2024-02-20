import pandas as pd
from nltk.corpus import names

# files come from nltk.download()
male_names = [n.lower() for n in names.words('male.txt')]
female_names = [n.lower() for n in names.words('female.txt')]

df = pd.read_csv("nyc_payroll_2021.csv")
df.first_name = df.first_name.astype(str)


def id_gender(first_name):
    first_name = first_name.lower()
    is_male = first_name in male_names
    is_female = first_name in female_names
    if is_male and not is_female:
        return 'm'
    elif not is_male and is_female:
        return 'f'
    else:
        return 'other'


gender = df.apply(lambda x: id_gender(x['first_name']), 1)
gender.value_counts()

df['gender_from_name'] = gender
k = 15
df[['first_name', 'gender_from_name']]

df.drop(columns=['Unnamed: 0', 'payroll_number',
                 'Unnamed: 0.1', 'agency_name',
                 'last_name'],
        inplace=True)

titles = df.title_description.value_counts()
(titles < 50).mean()
rare_title = titles.loc[titles < 50].index
df['rare_title'] = df.apply(lambda x: x['title_description'] in rare_title, 1)

df.to_csv('processed_nyc_payroll_2021.csv', index=False)
