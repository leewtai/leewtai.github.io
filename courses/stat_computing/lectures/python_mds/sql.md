# SQL and analytics

Analytics is a key skill to learn in data science. "Analytics courses" are often
taught as an introductory statistics course or an SQL class.
The reason is that to answer most analytics questions, the concepts of
metrics, uncertainty, or the scientific method are necessary. On the
other hand, the data is stored in an existing database so accessing the
data often requires some familiarity with SQL.

We will use the built-in package `squlite3` in Python3 to interface with SQL
databases.

## What are databases?

At this point, you should be familiar with individual files with data.
A database can be thought as a collection of files that is optimized for
certain operations, e.g. searching for a record in a particular "file",
ensuring consistency across different users reading the data at different times,
ensuring transactions between files are tolerant to machine failures.

There are reasons that corporate data is stored in databases but we will
not dive too deep into these reasons.

#### Some terminology

- Table: objects **similar** to data frames in databases,
  where rows correspond to different records and columns correspond
  to different features. There is often one or more special columns
  that will be designated as the **primary key**, which is how databases 
  are able to search for records so quickly.
  - You'll sometimes hear the primary key as the column that is the index
    of the table.
- Database: a collection of tables and possibly other data types.

## Creating a toy database

To create a somewhat realistic database, we will leverage an e-commerce dataset
on [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and convert
all of the CSV files into "tables" in a database. This section is less important
because this is often done by a data engineer and not data scientists.
There are many considerations about "usecases for the data" that will determine
different choices for the databases.

To create a naive relational database, we will
- Establish a database with `sqlite3.connect()`
- Create an empty table for each CSV with `CREATE TABLE ...`
  - `CREATE TABLE` is an SQL command which will be passed
    to the database via `sqlite3.connection.cursor.execute()`
    as a string. This allows us to write SQL queries composing
    strings via string manipulation.
    - We specify the column name followed by its
      data type, leveraging the data types inferred by pandas when
      we read in the data using `pandas.read_csv`
  - This is often where one would constrain particular columns like
    allowing missing values, designating one or more primary keys,
    create a default value, specifying the data type etc.
- Insert records into the table with `INSERT INTO {table} ... VALUES ...`

We will relay the SQL queries to the database in Python. 
Place the CSV files in the same directory as the
following script. The script will perform the steps we describe above.
Try to analyze the code in pieces and analyze each bit before moving forward.

```python
import sqlite3
import re
from glob import glob

import pandas as pd

csvs = glob('*.csv')
connection = sqlite3.connect('olist.db')
cursor = connection.cursor()

for csv in csvs:
    df = pd.read_csv(csv)
    if re.search('^olist', csv):
        table = re.sub('olist_([a-z_]+)_dataset.csv', r'\1', csv)
    else:
        table = 'product_cat_trans'

    # Converting pandas data types to SQL data types
    col_dts = []
    for col, dt in zip(df.columns, df.dtypes):
        if dt == 'object':
            dt = 'text'
        elif dt == 'int64':
            dt = 'int'
        else:
            dt = 'double precision'
        col_dts.append(f'{col} {dt}')

    column_dtype = ', '.join(col_dts)

    # Create empty table
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({column_dtype})')

    # Insert records into the empty table
    cols = ','.join(df.columns)
    qs = ','.join(['?' for _ in range(df.shape[1])])
    for _, row in df.iterrows():
        cursor.execute(f'INSERT INTO {table} ({cols}) VALUES ({qs})', row)

    # Think this as a "save" step
    connection.commit()

connection.close()
```

After running the query above, you should have a database called `olist.db`
that contains the data from the CSV files.

## Querying data using SQL

In general, the databases will be maintained by a data engineering team
that so the analysts can focus on querying the appropriate datasets to answer
different business questions. So the key skill with SQL often surrounds learning
all the various `SELECT` statements.

In the examples below, we will skip the part where we pass the SQL command
as a string to `sqlite3.cursor.execute(SQL_QUERY).fetchall()` but only focus
on the SQL syntax only. For example, all SQL queries below should be inserted
into `SQL_QUERY` to run properly in your Python environment.

```python
import sqlite3

connection = sqlite3.connect('olist.db')
cursor = connection.cursor()

SQL_QUERY = "{YOUR_SQL_CODE}"

output = cursor.execute(SQL_QUERY).fetchall()
```

#### Examining what tables are available

```SQL
SELECT name FROM sqlite_master WHERE type='table'
```

This reads as select from the table `sqlite_master` where the records have the value `'table'` in the column `type` then return the value in the column `name` for those records.

Note although we did not define `sqlite_master`, it is created by default to
locate all of the other tables created.

#### To get the schema and columns names for a table

```sql
PRAGMA table_info('order_payments')
```

This will return, for the table `order_payments`, in order, 
- the id for each variable,
- the name of each variable
- the SQL data type of each variable
- whether the respective variable has "IS NOT NULL" enforced
- Default value for each variable
- whether the respective variable a primary key or not


#### Examining sample records of a table

This query says: "from table `order_payments`, please return all variables associated with
the first 5 records."

```sql
SELECT
  *
FROM
  order_payments
LIMIT
  5
```

#### Examining sample records of specific columns in a table

This query says: "from table `order_payments`, please return the variables `order_id` and `payment_value` associated with the first 5 records."

```sql
SELECT
  order_id,
  payment_value
FROM
  order_payments
LIMIT
  5
```

#### Calculating summary statistics

This query says: "from table `order_payments`, group the records by `order_id`; then calculate the maximum `payment_value` across those records, we will refer this result as `max_pay`; then calculate the number of records used to produce this summary statistic, referring this as `cnt`; then please return the variables `order_id`, `max_pay`, and `cnt`.

```sql
SELECT
  order_id,
  MAX(payment_value) as max_pay,
  COUNT(*) as cnt
FROM
  order_payments
GROUP BY
  order_id
```

Other popular functions are:
- the average or sum: `AVG({VARIABLE})` or `SUM({VARIABLE})`
- the minimum: `MIN({VARIABLE})`
- the unique count: `COUNT(DISTINCT({VARIABLE}))`
- count the number of rows being aggregated: `COUNT(*)`

#### Filtering based on summary statistics

Sometimes we want to look at summary statistics that satisfy a certain criterion.
For example, if the maximum is taking over a single value, that may be indicative
of users that are relatively new on the platform and we may want to filter those out
from our calculations.

Since the `WHERE` keyword is reserved to filter records before aggregation, there's
another keyword `HAVING` that can filter records after the aggregation.

```sql
SELECT
  order_id,
  MAX(payment_value) as max_pay,
  COUNT(*) as cnt
FROM
  order_payments
GROUP BY
  order_id
HAVING
  COUNT(*) > 1
```

It's important to know that both `WHERE` and `HAVING` can co-exist, for example, we want
want to limit the maxmimum to be applied on non-zero payment values only then only keep
the maximums that had 2 or more non-zero payment.

```sql
SELECT
  order_id,
  MAX(payment_value) as max_pay,
  COUNT(*) as cnt
FROM
  order_payments
WHERE
  payment_value > 0
GROUP BY
  order_id
HAVING
  COUNT(*) > 1
``` 

#### Nesting tables

Below we calculate the standard deviation in `payment_value`,
notice to achieve this,
we will calculate the average in a nested call.

```sql
SELECT
  SQRT(AVG((a.payment_value - agg.avg) * (a.payment_value - agg.avg))) as std,
  agg.avg,
  COUNT()
FROM
  order_payments as a,
  (SELECT AVG(payment_value) as avg FROM order_payments) as agg

```

#### JOINing two tables

Identical to the concept behind `pandas.DataFrame.merge`, SQL has
a functionality called "JOIN".

Below we calculate, for each customer, their largest purchase and
the number of orders.

Notice that the default `JOIN` is an inner join.

```sql
SELECT
  orders.customer_id,
  MAX(b.total) as max_purchase,
  COUNT() as order_count
FROM
    orders
  LEFT JOIN
    (SELECT
       order_id,
       SUM(payment_value) total
     FROM
       order_payments
     GROUP BY
       order_id) as b
  ON
    orders.order_id = b.order_id
GROUP BY
  orders.customer_id
```

