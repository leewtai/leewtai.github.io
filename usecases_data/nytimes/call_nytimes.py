import json
import requests

import credentials


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

params = {'q': 'flu', 'api-key': credentials.api_key}
response = requests.get(url=url, params=params)
out = response.json()

json.dump(out, open('nytimes_article_search_20200401.json', 'w'))
