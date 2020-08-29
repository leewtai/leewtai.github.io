import time
import requests
from bs4 import BeautifulSoup

auth_citation_url = 'https://scholar.google.com/citations'
author_id = '88cU_4UAAAAJ'
params = {
    'user': author_id,
    'sortby': 'pubdate',
    'pagesize': 100}
out = requests.get(url=auth_citation_url, params=params)

soup = BeautifulSoup(out.text, 'html.parser')
citations = soup.find_all('tr', 'gsc_a_tr')
for entry in citations:
    citation = entry.find_all('td', 'gsc_a_t')[0]
    citation_content = [cont.text for cont in citation.contents]
    pub_year = entry.contents[-1].text
    cited_by = entry.contents[1]
