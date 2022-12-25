# Wrangling data for different purposes

People used to say that data wrangling was the most time consuming topic in data scientists'
day-to-day job. You likely also heard that many data startups' main value proposition is
around saving people's time with data wrangling. Regardless, the data scientists who are
exploring new frontiers of data likely will still be wrangling data for years to come.

## What is data wrangling?

Data wrangling is essentially the code that makes the data, from its current state, usable for
your problem at hand. This problem appears because the optimal format for storage is often
different from the optimal format for analysis, leading to a translation task between the two.

For example, to analyze productivity of a farm, we often look at yield, i.e. the amount of food
produced divided by the amount of land used (acrage). The amount of land used is known early on 
from the planting data that also includes the timing of planting, the type of seeds planted,
the amount of seeds planted, etc. The optimal format for storage requires flexibility for
different types of data and storage efficiency (e.g. avoiding repeated values), in other words, not
in a tabular format.

On the other hand, analysis would want the acrage on the same row as the production 
number, having a single number that represents planting and another for harvest (often planting
and harvesting can span over multiple days).
Here we optimizing for structure in the data that allows us to perform consistent analyses on the data.

## Common wrangling tasks

Wrangling is often considered something you will learn on the job. The skills required
are a familiarity with different data types, in particular, how to construct, subset, and aggregate values from them.

#### Long to wide data frames

One of the most common tasks is the translation between long and wide data frames, also known as pivoting.

Long and wide datasets are both rectangular data formats but long format data often stores a single
measurement per row where a wide format would store multiple measurements per row that are related
to the same entity. For example

Example long data:

|patient_id|variable|value|units|
|-------|--------|-----|-----|
|1|'height'|178|'cm'|
|2|'height'|166|'cm'|
|1|'weight'|80|'kg'|
|1|'age'|40|'year'|
|2|'age'|30|'year'|

The long data is similar to a "log" where each measurement is written down so it is not
lost while waiting for other variables to be created.

Converting this long data frame to the equivalent form of wide data frame where each row is an individual would look like:

|patient_id|height_cm|weight_kg|age_year|
|1|178|80|40|
|2|166|NaN|30|

To accomplish this task we use the following code:
```python
import pandas as pd

long_df = pd.DataFrame([
  {'patient_id': 1, 'variable': 'height', 'value': 178, 'units': 'cm'},
  {'patient_id': 2, 'variable': 'height', 'value': 166, 'units': 'cm'},
  {'patient_id': 1, 'variable': 'weight', 'value': 80, 'units': 'kg'},
  {'patient_id': 1, 'variable': 'age', 'value': 40, 'units': 'year'},
  {'patient_id': 2, 'variable': 'age', 'value': 30, 'units': 'year'},
])
long_df['var_w_units'] = long_df.apply(lambda x: x['variable'] + '_' + x['units'], axis=1)

wide_df = pd.pivot(long_df,
    index='patient_id', columns='var_w_units', values='value').reset_index()

print(wide_df)
```

- We first created a new column named `var_w_units` so we would have the appropriate
  labeling. This would also allow us to detect issues with different units for the 
  same variable if that exists.
- We'll use the [`pandas.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html) function to perform our pivoting. There are a few different pivot functions. My recommendation is to stick to one of them and be familiar with its behaviors (especially when there is missing values).
- The `index` argument defines the "rows" in the wide data frame, i.e.
  what dimension will constitute a single record. In this case, a single record
  is all the data associated with the same `patient_id` number.
- The `columns` argument defined the "columns" in the wide data frame. Each unique
  value will become a new column. You may think of these as the "features" in your data.
- The `values` argument defines the "entry/elements" in the wide data frame.
- If the same row/column has multiple values associated with it, a `ValueError` will be
  raised. This issue must be resolved using information about the domain + data creation
  process.
- Resetting the index just makes sure that the `patient_id` is stored as a regular column
  rather than an index.

#### Wide to long data frames
Continuing our example from above, we could convert the wide data frame back to its long
format. This can be necessary either because of package requirements (e.g. "tidy data")
or it is easier to convert into a different wide format by first converting it back to
a long format.

Overall, wrangling into the long format (where each row represents one measurement),
so you can imagine we are "melting" the column in the wide format into 2 columns, one
with the column name and the other with the associated value.

```python
id_vars = ['patient_id']
non_id_cols = [col for col in wide_df.columns
                if col not in id_vars]
long_df2 = pd.melt(
    wide_df,
    id_vars=id_vars,
    value_vars=non_id_cols)
long_df2['variable'] = long_df2.var_w_units.apply(lambda x: x.split('_')[0])
long_df2['units'] = long_df2.var_w_units.apply(lambda x: x.split('_')[1])
long_df2.drop(columns='var_w_units', inplace=True)

print(long_df2)
```

- The `id_vars` argument are variables that shall stay 'untouched' and retain their
  function to define unique rows. These tend to be attributes that describe a data point.
- The `value_vars` are the ones that will be melted into a column with the column name
  and a column with the corresponding value.
- We split the column name using string manipulations to obtain our original data frame.


#### Hierarchical data to tabular data

The most common data format on the internet is a hierarchical dataset often in a JSON format. [`nytimes_metadata_example.json`](../../data/nytimes_metadata_example.json) gives an example
of how one could store the metadata about 10 articles. The number of authors will likely be
different so we cannot simply have a column for "author 1", "author2", etc since this will not apply to most records. Having all authors in a single column will defeat the purpose of storing data
in a easy-to-analyze table format.

This is just again the conflict between formats suited for storage is not the same as formats
suitable for analysis. Moreover, this usually results in data loss when we wrangle hierarchical data into tabular formats (not always).

For example, if I wanted to do an analysis on the authors, e.g. how many articles have they
written? This question is easy if interpreted literally. However, likely people would dig into the
articles and maybe request to only analyze non-OptEd articles (these are articles that are mostly
just opinions from certain people and are not generally considered journalistic). To prevent
possible work in the future, it's better to include metadata beyond just the author/article
information. Specifically, we should create a data frame, from 
[`nytimes_metadata_example.json`](../../data/nytimes_metadata_example.json), where each row
was an author/article combination and the columns correspond to
- The author's first name
- The author's middle name
- The author's last name
- The article's main headline
- The article's URL
- The `Section` of the article
- The published time of the article
Please default all values to `""` if a value does not exist. 

The implication of each row being an author/article combination implies that if we have
3 authors for the same article, we would create 3 rows for that article.

Before we wrangle the data, the most important task is the understand the JSON data format
and the specification for the resulting data frame. The final data frame should look something like

|first_name|middle_name|last_name|headline|url|section|published_time|
|Bob|M|Doe|breaking news: ....|https://www.nytimes.com/....|OptEd|2018-05-15T05:23:11|
|Mary||Jane|Hospitals in NYC are...|https://www.nytimes.com/....|New York|2018-05-15T06:13:20|

Now to understand the JSON data we will first do

```python
import json

with open('nytimes_metadata_example.json', 'r', encoding='utf-8') as f:
  meta = json.load(f)

type(meta)  # should be "list"
len(meta)   # should be 10

example_i = 0
article = meta[example_i]

type(article) # dictionary
len(article)  # 20

print(article.keys())
# dict_keys(['abstract', 'web_url', 'snippet', 'lead_paragraph',
#            'print_section', 'print_page', 'source', 'multimedia',
#            'headline', 'keywords', 'pub_date', 'document_type',
#            'news_desk', 'section_name', 'subsection_name', 'byline',
#            'type_of_material', '_id', 'word_count', 'uri'])
```

- It's important to know the data type of `meta` because that informs us how
  to subset an example record from the overall data, e.g. if it was a dictionary
  we wouldn't be able to subset with positional indices.
- We repeat the exploration with our example record, again, because we only
  know how to operate with a piece of data after we know its type. In our case,
  this happens to be a dictionary which allows/requires us to identify its keys.
- It is now important to examine each relevant key because we may assume they are
  strings but they may not be. In general I would still check the `type()` and `len()`
  in the following step but for brevity I'll skip this.

```python
print(article['web_url'])
print(article['section_name'])
print(article['pub_date'])
print(article['headline'])
print(article['byline'])
```

- The first step is to understand cases that seem odd, e.g. `headline` and `byline`. Often this is a good time to ask the data architect for their design choices. For example,
  - the list (instead of a string) mapped to `article['byline']['person']` would 
    help store multiple authors (the second article confirms this).
  - The different `'headline'` values suggest that headlines 
    are not the same across all publications (e.g. `print_headline` vs `main`).
- The second step is to create a single record in our desired data frame

```python
easy_keys = ['web_url', 'section_name', 'pub_date']
record = {k: article[k] for k in easy_keys}

record.update({
  'main_headline': article['headline']['main']
})

name_vars = ['firstname', 'middlename', 'lastname']
person = article['byline']['person'][0]
record.update({key: person[key] if person[key] else ''
               for key in name_vars})
```

- After getting a single record, we can now scale the code for each author!

```python
record_per_author = []
record.update({
  'main_headline': article['headline']['main']
})

name_vars = ['firstname', 'middlename', 'lastname']
# person = article['byline']['person'][0]
for person in article['byline']['person']:
    record_copy = record.copy()
    record_copy.update({key: person[key] if person[key] else ''
                        for key in name_vars})
    record_per_author.append(record_copy)
```

Do you know why we used `dictionary.copy()` in the for-loop?
Try removing it and see what happens :)
Now let's scale it across articles.

```python
records = []
for article in meta:
    record_per_author = []
    record.update({
      'main_headline': article['headline']['main']
    })
    
    name_vars = ['firstname', 'middlename', 'lastname']
    # person = article['byline']['person'][0]
    for person in article['byline']['person']:
        record_copy = record.copy()
        record_copy.update({key: person[key] if person[key] else ''
                            for key in name_vars})
        record_per_author.append(record_copy)
    records.extend(record_per_author)    
```

Finally we create the data frame from the list of dictionaries.

```python
df = pd.DataFrame(records)
```

All these different steps expand on the previous one and should be built
iteratively. One important key is to know that we've actually decided to
create the data frame from a list of dictionaries when we started to construct
a single record.

## General recommendation
The best way to approach data wrangling is to have a clear picture of your data in its
current state and its eventual state. Draw out a plan, and execute them step by step.

For long to wide and wide to long data frames, you should have example code ready
for a function you feel comfortable with.

{% include lib/mathjax.html %}
