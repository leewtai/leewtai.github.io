import datetime as dt
from datetime import timedelta

# Parametrize the script
# Monday is 0, Sunday is 6
lecture_days_of_week = [4]
# lecture_days_of_week = [0, 2]
begin = '2021-01-18'
end = '2021-05-02'
final_date = 'TBD'

first_dt = dt.datetime.strptime(begin, '%Y-%m-%d')
last_dt = dt.datetime.strptime(end, '%Y-%m-%d')
day = first_dt

# Body of script
print("|Date|Topic|Reference|Due|")
print("|---|---|---|---|")

while day <= last_dt:
    if day.weekday() not in lecture_days_of_week:
        day += timedelta(days=1)
        continue
    line = '|{date}|TOPIC or No Class|||'.format(
        date=dt.datetime.strftime(day, '%Y-%m-%d')
    )
    print(line)
    day += timedelta(days=1)


print('|TBD|Measure understanding|Final Exam|You!|')
