from pathlib import Path
import json
from glob import glob

import pandas as pd


name_parts = ['firstname', 'middlename', 'lastname']
def collapse_authors(byline):
    authors = byline.get('person')
    if not authors:
        return ''
    names = []
    for author in authors:
        name = [author.get(n) for n in name_parts if author.get(n)]
        name = ' '.join(name) if name else ''
        names.append(name)
    return ';'.join(names)


keyword_types = ['subject', 'glocations', 'persons', 'organizations', 'creative_works']
def collapse_keywords(keywords):
    bag = {kw: [] for kw in keyword_types}
    for kw in keywords:
        assert kw.get('name') in keyword_types
        bag.get(kw.get('name')).append(kw.get('value'))

    out = {}
    for kwt in keyword_types:
        out.update({f'keyword-{kwt}': ';'.join(bag.get(kwt)) if bag.get(kwt) else ''})

    return out

arch_jsons = glob('archive_data/*json')
for arch_json in arch_jsons:
    fp = Path(arch_json)
    with fp.open('r', encoding='utf-8') as f:
        arch = json.load(f)
    flat_out = []
    for art in arch:
        out = {
            'abstract': art.get('abstract'),
            'source': art.get('source'),
            'web_url': art.get('web_url'),
            'lead_paragraph': art.get('lead_paragraph'),
            'pub_date': art.get('pub_date'),
            'news_desk': art.get('news_desk'),
            'section_name': art.get('section_name'),
            'word_count': art.get('word_count'),
            'uri': art.get('uri'),
            'authors': collapse_authors(art.get('byline'))}
        out.update(collapse_keywords(art.get('keywords')))
        flat_out.append(out)
    pd.DataFrame(flat_out).to_csv('archive_data/' + fp.stem + '.csv')
