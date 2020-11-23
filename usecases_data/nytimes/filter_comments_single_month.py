import json
from pathlib import Path

import requests


cred = json.load(open('../credentials.json', 'r'))
# NYTImes limits to 4000 calls a day

# Use the NYTimes archive to make sure the data is consistent with
# what students will get
archive_url = 'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json'
arch_url_2020 = archive_url.format(year=2020, month=3)
params = {'api-key': cred['nytimes_api_key']}
arch_resp = requests.get(url=arch_url_2020, params=params)
arch = arch_resp.json()
arch_docs = arch['response']['docs']
arch_uris = [a['uri'] for a in arch_docs]

file = Path('nytimes_article_comments_2020.json')
comments = json.load(file.open('r'))

march_comments = {uri: comments[uri] for uri in comments
                  if uri in arch_uris and isinstance(comments[uri], list)}

march_files = Path('nytimes_2020_articles_with_comments.json')
json.dump(march_comments, march_files.open('w'))
