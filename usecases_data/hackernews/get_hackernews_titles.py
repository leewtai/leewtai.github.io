import logging
import random
import time

from datetime import datetime
import requests

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='hackernews.log',
                    level=logging.INFO)


hid_20211130 = 28254689 + 1144452
hid_start = 29876077  # hid_20211130
i = 0
error_cnt = 0
bag = []
while True:
    if i % 10000 == 0:
        with open('hackernews_titles.txt', 'a') as f:
            f.writelines(bag)
        logging.info(f'i is currently {i}')
        bag = []
    hid = hid_start + i
    time.sleep(random.uniform(0, 0.05))
    try:
        resp = requests.get('https://hacker-news.firebaseio.com/'
                            f'v0/item/{hid}.json')
    except:
        error_cnt += 1
        logging.error(f'Something went wrong at {i}')
        if resp and resp.text:
            logging.error(resp.text)
        continue
        if error_cnt >= 3:
            logging.error(f'errors exceeded 3 at {i}')
            break
    dat = resp.json()
    if dat is None:
        break
    if dat['type'] != 'story':
        i += 1
        continue
    dt = datetime.fromtimestamp(dat['time'])
    line = '{},{},{},{},{}\n'.format(
        dat['id'], dt.year, dt.month, dt.day, dat.get('title'))
    bag.append(line)
    i += 1


logging.info('end of loop')
logging.info(f'i is ending at {i}')
with open('hackernews_titles.txt', 'a') as f:
    f.writelines(bag)
