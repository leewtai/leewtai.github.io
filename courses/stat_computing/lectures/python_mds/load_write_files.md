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

Here's an example of how to read a JSON file.
```python
import json

demo_handle = open('demo.json', 'r')
demo_json = json.load(demo_handle)
```

Here's an example of how to read a CSV file.
```python
import pandas as pd

demo_df = pd.read_csv("demo.csv")
```
{% include lib/mathjax.html %}
