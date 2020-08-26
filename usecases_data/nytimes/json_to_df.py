import json
import numpy as np
import pandas as pd


arch = json.load(open('nytimes_2020_arch.json', 'r'))
comments = json.load(open('nytimes_2020_articles_with_comments.json', 'r'))

art_bag = []
for uri in arch:
    art = arch[uri]
    first_rank_auth = [person for person in art['byline']['person']
                       if person['rank'] == 1]
    lastname = first_rank_auth[0]['lastname'] if first_rank_auth else 'NA'
    firstname = first_rank_auth[0]['firstname'] if first_rank_auth else 'NA'
    art_bag.append({
        'uri': uri,
        'lastname': lastname,
        'firstname': firstname,
        'pub_date': art['pub_date'],
        'news_desk': art['news_desk']})

archive_df = pd.DataFrame(art_bag)

comment_bag = []
for uri in comments:
    comms = comments[uri]
    for comm in comms:
        words = comm.get('commentBody').split(' ')
        comment_bag.append({
            'uri': uri,
            'num_rec': comm.get('recommendations'),
            'display_name': comm.get('userDisplayName'),
            'update_date': comm.get('updateDate'),
            'approve_date': comm.get('approveDate'),
            'editorsSelection': comm.get('editorsSelection'),
            'word_count': len(words),
            'uniq_word_count': len(set(words))})

comments_df = pd.DataFrame(comment_bag)

rank_dfs = []
for grp, index in comments_df.groupby('uri').groups.items():
    sub_df = comments_df.loc[index]
    ranks = np.argsort(sub_df.update_date) + 1
    rank_dfs.append(pd.DataFrame(
        {'uri': grp, 'rank': ranks, 'update_date': sub_df.update_date}))

rank_df = pd.concat(rank_dfs)

df = comments_df.merge(rank_df).merge(archive_df)
df.to_csv('nytimes_202003_comments_with_meta.csv')
