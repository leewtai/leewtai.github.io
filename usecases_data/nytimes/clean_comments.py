import json


with open('nytimes_2020_arch.json', 'r') as f:
    arch = json.load(f)

with open('nytimes_article_comments_2020.json', 'r') as f:
    comments = json.load(f)


with_comments = {aid: comments[aid] for aid in comments
                 if isinstance(comments[aid], list)}

print('detecting {} articles with comments', len(with_comments))
with open('nytimes_2020_articles_with_comments.json', 'w') as f:
    json.dump(with_comments, f)
