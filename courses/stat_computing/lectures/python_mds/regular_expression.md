# Regular expression

When dealing with text data, often we encounter patterns in text but exact
matches are difficult to specify, e.g. we want all the "numbers" mentioned
in a particular piece of text. This is when regular expression comes in handy.

#### Terminology string vs character
- A character is a single letter, number, or symbol (e.g. space `" "`, underscore `"_"`,
semicolon `";"`, etc) that is stored as a character value. 
- A string is a collection of 0 or more characters, stored as a character value. A
  length 0 string is often called the empty string, `""`

#### Recognizing patterns in text data
For our first example, we'll try to work with birthdays of UFC fighters
in [raw_fighter_details.csv on Kaggle](https://www.kaggle.com/rajeevw/ufcdata).

The data is still in a csv format so we can leverage the old functions we learned.
```python
import pandas as pd

fighters = pd.read_csv("raw_fighter_details.csv")
fighters.DOB.head(20)
```
What to notice?
- Some birthdays are recorded as empty strings
- When the birthdays are not missing, the first few records suggest a format:
  - the first 3 characters correspond to the month in abbreviated letters, the
    first being capitalized and the others lowercased.
  - the 5th to 6th character correspond to the day (notice the 11th record used
    `05` instead of `5` to indicate the day)
  - the 9th to 12th character correspond to the year
- We have not seen the other records so the format may not hold, e.g. we could see
  `"12 18, 1983"` in other records.

This format suggests that we could subset different characters to obtain the
different pieces of information.

#### Getting a substring, subsections of a string
When the data follows a strict pattern as we have seen, it's possible
to extract the birth month by subsetting specific positions in the string
using `[]`.

To get the months, we'll write a function that can be applied to each record.
This means that the function needs to handle the case when the date is missing.
To capture the empty string case and potentially other cases, we'll
check if the string has 12 characters before subsetting. Specifically, in the event that
there are not 12 characters, we will return the original string so we can 
analyze these cases later.

```python
def grab_month(date_str):
    if len(date_str) != 12:
        return date_str
    return date_str[:3]


months = fighters.apply(lambda x: grab_month(str(x.DOB)), 1)
months.value_counts()
```

What to notice?
- The only exception to the months were empty strings in the data
- We used `pandas.DataFrame.apply()` to apply the function on each record.
- Another way to write the function would have been to use if/else
  ```python
  def grab_month(date_str):
      if len(date_str) != 12:
          month = date_str
      else:
          month = date_str[:3]
      return month
  ```
  from a readability standpoint, there are more lines and more indentation.


#### Parsing strings with more complicated patterns 
Natural text, however, is rarely formatted in such a uniform fashion.

Imagine trying to extract each word from the following sentence from
a job scription.
```python
demo = "Experience with Google Analytics and Google Optimize\nKnowledge of project management tools (JIRA, Trello, Asana)\n"
demo.split(" ")
```

Notice how we normally would not consider "(" and "," as part of the word.
This means we need a more flexible way to manipulate text programmatically,
this is where regular expression comes in.

#### Regular expression: specifying complex text patterns
Regular expression is a common syntax for specifying complex text patterns
for programs.

The general syntax for the pattern is to specify
1. The type of character
2. Immediately followed by the frequency for the character

These patterns are then used as an inputs to various functions. 
The first common operation is the substitute function from the built-in package `re`, `re.sub()`.
This function can replace the specified patterns with a specified output.

```python
import re
re.sub("!", "_", "Hello! IN PERSON CLASSES!!!")
```

Below we explain how regular expression works in more detail.

#### Specifying the frequency in regular expression
For the following example, we will use the demo string `demo = 'rawr rawrr rawrrr!'`
with the `r` as the character to be replaced.

Here are a few common frequencies, you should TYPE out each example to see the impact

|Frequency|Regular Expression|Example|
|---|---|---|
|Exactly once|``|`re.sub("r", "_", demo)`|
|Exactly 2 times (notice 2<br>can be replaced with any integer)|`{2}`|`re.sub("r{2}", "_", demo)`|
|Exactly 2 to 4 times (notice 2 and<br>4 can be replaced with any integer)|`{2,4}`|`re.sub("r{2,4}", "_", demo)`|
|Zero or one occurrence|`?`|`re.sub("r?", "_", demo)`|
|One or more occurrence|`+`|`re.sub("r+", "_", demo)`|
|Zero or more occurrence|`*`|`re.sub("r*", "_", demo)`|

Notice that there are "empty strings" between each character by default, causing frequencies that catch
"zero" occurrences to add an additional `_` to the examples above.

#### Specifying the character in regular expression
For the following example, we will use the demo string with a diverse
set of characters `demo = 'wtl_2109@COLUMBIA.EDU'`

|Character|Regular Expression|Example|
|---|---|---|
|a word as a character|`(edu|education)`|`re.sub("(EDU|EDUCATION)", "?", demo)`|
|Any character between t, 0, OR 1|`(t|0|1)` or `[t01]`|`re.sub("(t|0|1)", "?", demo)`<br>`re.sub("[t01]", "?", demo)`|
|Any digit between 0 to 9|`\d` or `[0-9]` or `[5498732160]`|`re.sub("\d", "?", demo)`<br>`re.sub("[0-9]", "?", demo)`|
|Any lowercased alphabet|`[a-z]`|`re.sub("[a-z]", "?", demo)`|
|Any capital alphabet|`[A-Z]`|`re.sub("[A-Z]", "?", demo)`|
|alphanumeric or the underscore "_"|`\w` or `[a-zA-Z0-9_]`|`re.sub("\w", "?", demo)`|
|Any character (wild card)|`.`|`re.sub(".", "?", demo)`|
|NOT lower case alphabets|`[^a-z]`|`re.sub("[^a-z]", "?", demo)`|

What to notice?
- Any character placed inside `[]` would be treated as a possible character for matching
- `[^ ]` is the only "negation" type of pattern, i.e. anything character except those specified
  within the brackets will be matched.
- Common character patterns have abbreviations that often start with `\`, e.g. `\w` or `\d`
  You can find the list of these online


#### Combining characters and frequencies to form patterns

Returning to our original problem of parsing a sentence in the job description.
```r
import re

demo = "Experience with Google Analytics and Google Optimize\nKnowledge of project management tools (JIRA, Trello, Asana)\n"
re.sub("[^a-zA-Z]+", " ", demo).split(" ")
```
The code replaced "one or more non-letter character" with `" "`, allowing us to use `str.split()` to split out the words.
- `[^a-zA-Z]` is how we specify a character that satisfies "anything but the character a through z and A through Z"
- `+` is how we specify the frequency as "one or more occurrences", handling cases like `")\n"` into one single white space.

#### Limiting the substitution frequencies
Sometimes we only wish for the substitution to happen a limited number of times, that can be achieved
with the argument `count` in `re.sub()`. This is defaulted to 0 which starts for no limits on the
number of substitutions.

```python
demo = "rawr, rawrr, rwarrr"
re.sub("r{2}", "_", demo, count=1)
```

#### Getting a sub-pattern within multiple patterns
We can also combine multiple patterns into a single pattern. Imagine trying to get the website names
from the following demo:
```python
demo = ["www.google.com", "www.r-project.org", "www.linkedin.com", "xkcd.com"]
proper_demo = ['https://' + s for s in demo]
```
As humans, we recognize the "www" and the different endings (.org and .com) as not part of the name.

To specify the patterns we're seeing, you most likely will come up with something like
```python
pattern = "https://(www\.)?[^\.]+\.(com|org)"
[re.sub(pattern, "caught ya!", s) for s in proper_demo]
```

What to notice:
- Since `www.` was optional, we used `?` to say its appearance is optional.
- To specify a literal period, we had to type `\.` otherwise it would be confused with the wild card symbol.
- Since the website names can contain weird symbols, e.g. `-`, we know the only character people would avoid is
  likely the period, so the website name was anything BUT the period.
- Notice how we used `()` to specify different sub-patterns in the overall pattern. Try removing the `()`
  and see which websites will not be captured.
- For website endings, we chose to limit ourselves to the finite endings that we know (you could add .gov, .io, etc)
  instead of matching arbitrary endings. This is generally good practice to avoid mistakes.

The above example, however, did not extract the website name. To do so, there's another
specific idea in regular expression substitution that you should know. We'll add an additional
`()` for the subpattern that should match the website name.
```r
pattern = "https://(www\.)?([^\.]+)\.(com|org)"
[re.sub(pattern, "\\1 AND \\2 AND \\3", s) for s in proper_demo]
[re.sub(pattern, "\\2", s) for s in proper_demo]
[re.sub(pattern, "\\1SOMETHING.\\3", s) for s in proper_demo]
```
What to notice:
- Each sub-pattern, enclosed by `()`, corresponds to an index, i.e. the first pattern can be referred
  with `\\1`, the second can be referred as `\\2`, etc. Again, the `\\` is being used to separate from
  a literal `1` in this case.
- This can be useful to obtain different substrings from more complicated text pattern.


#### Other functions with regular expression
Besides substitution, there are a few other important functions that rely on regular expression.
- We can use the behavior where `None` evaluates to `False` to determine if a pattern is in the
  string or not?
  ```python
  import re

  demo = ["state", "statistics", "stat101", "no game", "probability"]
  stat_pattern = re.compile('stat')
  stat_matches = [stat_pattern.search(s) for s in demo]
  # print(stat_matches)
  # [<re.Match object; span=(0, 4), match='stat'>,
  #  <re.Match object; span=(0, 4), match='stat'>,
  #  <re.Match object; span=(0, 4), match='stat'>,
  #  None,
  #  None]
  ```

#### Regular expression in practice

One thing to know/embrace/accept about regular expression is that it is a very heavy trial
and error process. It is hard to know all the possible ways free form text may appear.
You should always double check your results and you should always Google for a solution since
someone else has likely encountered the same question.

Most software systems are designed such that "free text" is changed to drop-down menus so the input
is more predictable. Problems that require regular expression are
likely natural text which has many edge cases that rarely can be 100% captured by regular
expression.

The best way to learn is to keep trying :)

{% include lib/mathjax.html %}
