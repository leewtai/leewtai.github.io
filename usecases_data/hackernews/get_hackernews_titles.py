import logging
import random
import time

from datetime import datetime
import requests

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='hackernews.log',
                    level=logging.INFO)


hid_20210730 = 28005630
hid_20221121 = 33690012
hid_start = hid_20221121
i = 0
error_cnt = 0
bag = []
while True:
    if i % 10000 == 0:
        with open('hackernews_titles.txt', 'a') as f:
            f.writelines(bag)
        logging.info(i)
        bag = []
    hid = hid_start + i
    time.sleep(random.uniform(0, 0.5))
    try:
        resp = requests.get('https://hacker-news.firebaseio.com/'
                            f'v0/item/{hid}.json')
    except:
        error_cnt += 1
        logging.error(i)
        if error_cnt >= 3:
            break
    dat = resp.json()
    if dat is None:
        break
    if dat['type'] != 'story':
        i += 1
        continue
    dt = datetime.fromtimestamp(dat['time'])
    bag.append((dat['id'], dt.year, dt.month, dt.day, dat.get('title')))
    i += 1
