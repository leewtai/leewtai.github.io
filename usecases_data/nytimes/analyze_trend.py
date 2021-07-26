from datetime import datetime, timedelta
import json

import matplotlib.pyplot as plt
import pandas as pd

file_name = 'nyt_arch_climat_2010_to_2020.json'

jdat = json.load(open(file_name, 'r'))

assert len(jdat) > 0

bag = []
for datum in jdat:
    pub_date = datetime.strptime(datum['pub_date'], '%Y-%m-%dT%H:%M:%S+0000')
    headline = ';'.join([i for i in datum['headline'].values() if i])
    lead = datum['lead_paragraph']
    bag.append(
            {'pub_date': pub_date,
             'date': str(pub_date.date()),
             'year': pub_date.year,
             'month': pub_date.month,
             'day': pub_date.day,
             'headline': headline,
             'lead': lead})


df = pd.DataFrame(bag)
counts = df.date.value_counts().sort_index()
mov_avg = counts.rolling(14, min_periods=1).mean()

base_date = datetime.fromisoformat(mov_avg.index[0])
pub_dates = [(datetime.fromisoformat(d) - base_date).days
             for d in mov_avg.index]
plt.plot(pub_dates, mov_avg.to_numpy())
max_ind = mov_avg.argmax()
plt.text(pub_dates[max_ind] * 0.95,
         mov_avg[max_ind] * 1.01, 'Paris Agreement')
plt.text(pub_dates[980 + 279] * 0.95,
         mov_avg[980 + 279] * 1.01, 'US withdraws from\nParis Agreement')
plt.text(pub_dates[1720] * 0.95,
         mov_avg[1720] * 1.01, 'US Heat Wave')
plt.text(pub_dates[755] * 0.95,
         mov_avg[755] * 1.01, 'UN Climate Summit')
plt.xlabel('days since {}'.format(base_date.date()))
plt.savefig('mov_avg_climate_articles.png')
plt.close()
