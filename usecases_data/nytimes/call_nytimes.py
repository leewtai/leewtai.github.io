import json
import logging
import time
from pathlib import Path

import requests


log_file = 'call_nytimes.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)
# Connecting requests error logs to logging
logger = logging.getLogger('urllib3')
logger.setLevel(logging.INFO)

cred = json.load(open('../credentials.json', 'r'))
# NYTImes limits to 4000 calls a day
cap = 2000
calls_today = 0

comments_url = 'https://api.nytimes.com/svc/community/v3/user-content/url.json'

file = Path('nytimes_2020_arch.json')

if file.exists():
    logging.info('Archive file exists, using existing file')
    with file.open() as f:
        archs = json.load(f)
else:
    archive_url = 'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json'
    months = list(range(1, 7))
    logging.info('Extracting archive data for {} months'.format(len(months)))
    archs = {}
    for month in months:
        arch_url_2020 = archive_url.format(year=2020, month=month)
        params = {'api-key': cred['nytimes_api_key']}
        arch_resp = requests.get(url=arch_url_2020, params=params)
        calls_today += 1
        if arch_resp.status_code != 200:
            logging.info('month {month} failed'.format(month=month))
        out = arch_resp.json()
        logging.info('got month {}'.format(month))
        # Archives have duplicate entries, take the later one arbitrarily
        uniq_arts = {article['_id']: article
                     for article in out['response']['docs']}
        archs.update(uniq_arts)
        time.sleep(6.1)

    json.dump(archs, file.open('w'))


comment_fields = [
    'userID', 'userDisplayName', 'commentBody', 'updateDate',
    'approveDate', 'recommendations', 'replyCount', 'editorsSelection',
    'isAnonymous']


def extract_comments(comments):
    filtered_comments = [{field: comm[field] for field in comment_fields}
                         for comm in out['comments']]
    return filtered_comments


def call_comments(article_url, offset=0,
                  api_key=cred['nytimes_api_key'], calls_today=0):
    params = {'api-key': api_key,
              'url': article_url,
              'offset': offset}
    if calls_today > cap:
        out = 'fail safe: API call limit hit at {} calls'.format(
                calls_today)
        logging.warning(out)
        return out

    try:
        time.sleep(6.1)
        out = requests.get(url=comments_url, params=params)
        out.raise_for_status()
    except requests.exceptions.ConnectionError:
        out = 'fail safe: connection error with url {}, and offset {}'.format(
                article_url, offset)
    except requests.exceptions.Timeout:
        out = 'fail safe: timeout error with url {}, and offset {}'.format(
                article_url, offset)
    except requests.exceptions.HTTPError:
        code = out.status_code
        meta = 'API call failed, status {}, call number {}, id {}'.format(
                code, calls_today, article_url)
        out = meta + out.text

    return out


def bad_call(resp, calls_today):

    if calls_today > cap:
                status = True
    return status


file = Path('nytimes_article_comments_2020.json')
if file.exists():
    with file.open() as f:
        art_comments = json.load(f)
    logging.info('comments file exists')
    has_comment = sum(1 for aid in art_comments
                      if isinstance(art_comments[aid], list))
else:
    art_comments = {}
    has_comment = 0

logging.info('start comment extraction')
logging.info('Initial state: {} processed, {} with comments'.format(
    len(art_comments), has_comment))
for i, art_id in enumerate(archs):
    if art_id in art_comments:
        continue
    comment_resp = call_comments(archs[art_id]['web_url'],
                                 calls_today=calls_today)
    calls_today += 1
    if isinstance(comment_resp, str):
        if 'fail safe' in comment_resp:
            break
        else:
            art_comments.update({art_id: comment_resp})
            continue
    out = comment_resp.json().get('results')
    if not out or out['totalCommentsFound'] == 0:
        art_comments.update({art_id: '200 status but no comments found'})
        continue
    comments = extract_comments(out['comments'])
    # 25 comments is the most NYTime's API will return
    num_pages = out['totalCommentsFound']//25 + 1
    for offset in range(num_pages):
        if offset == 0:
            continue
        comment_resp = call_comments(archs[art_id]['web_url'], offset=offset,
                                     calls_today=calls_today)
        calls_today += 1
        if isinstance(comment_resp, str):
            break
        out = comment_resp.json().get('results')
        comments.extend(extract_comments(out['comments']))

    if offset == (num_pages - 1):
        art_comments.update({art_id: comments})
    else:
        logging.info('likely hit cap, calls today {}'.format(calls_today))
        break


has_comment = sum(1 for aid in art_comments
                  if isinstance(art_comments[aid], list))
logging.info('overwriting comments file')
logging.info('end state: {} processed, {} with comments'.format(
    len(art_comments), has_comment))
json.dump(art_comments, file.open('w'))
