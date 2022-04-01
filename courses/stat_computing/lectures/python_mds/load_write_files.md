# Loading and writing data from and to files

Data is often stored in different file formats and you need different parsers
to load these.

Sometimes the data may not be properly formatted and it'll need to be read
in like text.

## Reading and writing files

The most important thing is to understand what format is best for your data.

Common plain text formats are:
- **CSV**, stands for Comma Separated Values, this is the classic tabular format
  data where rows often refer to different records and the columns refer to
  different features. The tabular format implies that each record has the same
  number of features (if missing, a missing or default value must be assigned)
  and each feature has the same number of records. The convention is that the
  first row describes the features (e.g. `First_Name`, `Last_Name`, etc). For
  example:
  ```python
  "First_Name","Last_Name","Age","Sex"
  "Wayne","Lee",21,"M"
  "Sharmodeep","Bhattacharyya",20,"M"
  "Michelle","Martinez",20,"F"
  ```
- **JSON**, is like the dictionary in Python where it can have keys and it can
  nest data to have a hierarchical structure. For example:
  ```python
  {"students": [
      {"name": "Wayne Lee",
       "age": 21,
       "sex": "M"},
      {"name": "Sharmodeep Bhattacharyya",
       "age": 20,
       "sex": "M"},
      {"name": "Michell Martinez",
       "age": 20,
       "sex": "F"}],
   "course": {
       "name": "stat comp & intro to data sci",
       "code": ["GR5206", "UN4206"]}
   "enrollment_cap": 10
   }
   ```

Some fields have created standards around data and therefore their own
data format. Shape files for geospatial data is such an example.

Some places, for efficiency and privacy, may have their own format that
may not be stored in plain text. [Protobuf](https://developers.google.com/protocol-buffers/)
from Google is a popular version of this where one needs a separate
file to parse (deserialize) the data stream.
  
#### A package will likely exist

To read any data, you'll likely need a package to help you read it.

With lower level functions, it's important to know that reading from and
writing to data often involves 2 steps.
1. Creating a handle to accessing a file in a read or write mode
2. Parsing the data stream from the file (read) or serializing the data
   into the file's format (write).

Serialization just means to store the data in the file's format, e.g.
characters are surrounded by `""`, values are separated by `,`, etc.
There are more complicated versions when the data is not stored in
plain text.

Here's an example of how to read/write a JSON file.
```python
import json

demo_handle = open('demo.json', 'r')
demo_json = json.load(demo_handle)
json.dump(demo_json, open('demo_copy.json', 'w'))
```

Here's an example of how to read/write a CSV file.
```python
import pandas as pd

demo_df = pd.read_csv("demo.csv")
demo_df.to_csv("demo_copy1.csv")
```

Another approach is using `numpy` which we will discuss in more detail soon.
```python
import numpy as np

demo_array = np.loadtxt(fname="demo.csv", delimiter=",")
np.savetxt("demo_copy.csv", demo_array, delimiter=",")
```

#### Reading in plain text data that may be poorly formatted

Every now and then, we'll have data that is poorly formatted. For example,
the [CSV file from the World Bank](https://data.worldbank.org/topic/health)
will lead to a parsing error for most programs.

```python
import pandas as pd
df = pd.read_csv("API_8_DS2_EN_csv_v2_3471645.csv")
# ParserError: Error tokenizing data. C error: Expected 3 fields in line 5, saw 66
```

To debug the problem, we could open the file with a text editor (e.g. Note Pad on
Windows) or let Python read the file line by line to debug the issue.

```python
with open("API_8_DS2_EN_csv_v2_3471645.csv", "r") as f:
    txt = f.readlines()

txt[:5]
```
Reading the first 5 lines reveals that the first 4 lines contain metadata (data
title and last updated date), breaking the usual CSV format. Knowing this error,
we can tell our usual functions to skip the first 4 lines.

```python
df = pd.read_csv("API_8_DS2_EN_csv_v2_3471645.csv", skiprows=4)
```

In worst cases, we would need to parse the data line by line.
 
{% include lib/mathjax.html %}
