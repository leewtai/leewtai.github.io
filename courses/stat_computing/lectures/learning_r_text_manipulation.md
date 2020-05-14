# Problem 5 Analyzing Text Data
This chapter will focus on programmatically identifying key words in job descriptions.
Job descriptions often introduce the company, the role they're hiring
for, then follow up with basic and preferred qualifications. As students,
it would be nice to understand what qualifications are common across different
employers.

To understand and analyze text, we need to learn how to read, parse,
search through text data. Specifically:
- How to read in files in raw text form with `readLines()`
- How to parse text in a specific format with `strsplit()`
- How to extract subsections of text using their position with `substr()`
- How to parse text in complex formats with regular expression
- ...

#### Terminology string, text, and character
- A character is a single letter, number, or symbol (e.g. space `" "`, underscore `"_"`,
semicolon `";"`, etc) that is stored as a character value. 
- A string is a collection of 0 or more characters, stored as a character value. A
  length 0 string is often called the empty string, `""`

Both characters and strings will be stored as character values in R.
```r
empty_string <- ""
demo_string <- "random string!"
nchar(empty_string)
nchar(demo_string)
class(empty_string)
class(demo_string)
```

#### Recognizing patterns in text data
For our first example, we'll try to work with birthdays of UFC fighters
in [raw_fighter_details.csv on Kaggle](https://www.kaggle.com/rajeevw/ufcdata).

The data is still in a csv format so we can leverage the old functions we learned.
```r
fighters <- read.csv("YOUR_PATH/raw_fighter_details.csv",
                     stringsAsFactors = FALSE)
head(fighters$DOB)
# [1] ""             ""             ""            
# [4] ""             ""             "Nov 12, 1974"
# [7] "Mar 18, 1989" "Nov 14, 1992" "Aug 26, 1986"
#[10] ""             "Aug 05, 1989"
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
to extract the birth month by subsetting specific indices in the character string
(indices are like locations on the string).

To get the months, we'll write a function that can be applied to each record.
This means that the function needs to handle the case when the date is missing.
To capture the empty string case and potentially other cases, we'll
check if the string has 12 characters before subsetting. Specifically, in the event that
there are not 12 characters, we will return the original string so we can 
analyze these cases later.

```r
grab_month <- function(date_str){
    if(nchar(date_str) != 12){
        return(date_str)
    }
    month <- substr(date_str, 1, 3)
    return(month)
}
months <- sapply(fighters$DOB, grab_month)
table(months)
# months
#     Apr Aug Dec Feb Jan Jul Jun Mar May Nov Oct Sep 
# 740 199 267 184 197 180 262 202 216 225 199 226 216
```
What to notice?
- The only exception to the months were empty strings in the data
- We used `sapply()` to apply the function on each record. Given
  the simple output (each length 1 and a character value),
  the output from `sapply()` is likely a vector.
- Another way to write the function would have been to do
  ```r
  grab_month <- function(date_str){
      if(nchar(date_str) != 12){
        out <- date_str
      } else {
        out <- substr(date_str, 1, 3)
      }
      return(out)
  }
  ```
  from a readability standpoint, there are more lines, more indentation,
  and the variable names are less clear in this way.

[Exercise](../exercises/r_substring.md)

#### Reading in the data as character strings
Recall the [Fisher dataset](../data/fisher_1927_grain.csv) that 
`read.csv()` nicely parsed into a data frame. We can also read the data
in as character strings to see the format of the data using `readLines()`

Please run the following code and compare it against the data frame version.
```r
grain_csv <- read.csv('fisher_1927_grain.csv')
grain <- readLines('fisher_1927_grain.csv')
class(grain)
length(grain)
head(grain, 2)
head(grain_csv, 2)
```
What to notice?
- Each line in the raw data corresponds to a different row
- The different column values in each row are separated from one another using the comma `,`
  - Each line therefore will have the same number of `,`'s
  - Notice that the commas do not exist when we used `read.csv()`, because
    these are not part of the data but simply used to delineate the data.

[Exercise](../exercises/r_readlines.md)

#### Why should I bother with `readLines()` given `read.csv()` exists?
- Turns out that the file extension `.csv` does not guarantee that the data is formatted
  properly. Here is an example [CSV file from the World Bank](../data/world_bank_total_population.csv)
  that is not properly formatted. How to read it?
  - First use `readLines()` and notice the first `K` rows are not in the CSV format.
  - Turns out there's an argument in `read.csv()` that can skip the first few rows
    before reading in the data. Read the documentation to find out!
- Having the ability to read in arbitrarily formatted data as text can be very powerful
  once we learn how to manipulate text. When a file cannot be read properly, you can
  always fall back on readLines() if the file is encoded as text.


#### Separating strings based on a special symbol
`.csv` stands for **c**omma **s**eparated **v**alues, i.e. commas are dedicated to 
separate one value from another.

To split character strings by a particular symbol, we could use the function
`strsplit()` to parse the data.

The bahvior of `strplsit()` is slightly more complicated so it's best to start with a demo.
```r
demo_str <- c("2020/04/01", "2019/12/11")
strsplit(demo_str, split="/")
strsplit(demo_str[1], split="/")
```
What to notice:
- Each element in the list is a character vector
- The output from `strsplit()` is a list, even if there was only one character input.
  - The reason list is a reasonable data type for the output is because each value
    can be split into character vectors with different lengths.
- After splitting, the symbol used was erased.

[Exercise with the Fisher dataset](../exercises/r_parse_data.md)

#### Parsing strings with more complicated patterns 
Notice how `strsplit()` depended on the data to be formatted in a certain fashion.
Natural text, however, is rarely formatted in such a uniform fashion.

Imagine trying to extract each word from the following sentence from
a product manager job scription.
```r
demo <- "Experience with Google Analytics and Google Optimize\nKnowledge of project management tools (JIRA, Trello, Asana)\n"
strsplit(demo, split=" ")
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
The first common operation is the substitute function, `sub()`, that
can replace the specified patterns with a specified output. For example:
```r
demo <- "x = 1"
sub("=", "<-", demo)
```
The code replaced `=` with `<-` for the character assigned in the variable `demo`.

#### Specifying the frequency in regular expression
For the following example, we will use the demo string `demo <- ''`
with the `r` as the character to be replaced.

Here are a few common frequencies, you should TYPE out each example to see the impact

|Frequency|Regular Expression|Example|
|---|---|---|
|Exactly once|``|`sub("r", "_", demo)`|
|Exactly 2 times (notice 2<br>can be replaced with any integer)|`{2}`|`sub("r{2}", "_", demo)`|
|Exactly 2 to 4 times (notice 2 and<br>4 can be replaced with any integer)|`{2,4}`|`sub("r{2,4}", "_", demo)`|
|Zero or one occurrence|`?`|`sub("r?", "_", demo)`|
|One or more occurrence|`+`|`sub("r+", "_", demo)`|
|Zero or more occurrence|`*`|`sub("r*", "_", demo)`|

[Exercise](../exercises/r_frequency_reg_expression.md)

#### Specifying the character in regular expression
For the following example, we will use the demo string with a diverse
set of characters `demo <- 'wtl_2109@COLUMBIA.EDU'`

|Character|Regular Expression|Example|
|---|---|---|
|a word as a character|`(edu|education)`|`sub("(EDU|EDUCATION)", "?", demo)`|
|Any character between t, 0, OR 1|`(t|0|1)` or `[t01]`|`sub("(t|0|1)", "?", demo)`<br>`sub("[t01]", "?", demo)`|
|Any digit between 0 to 9|`\\d` or `[0-9]` or `[5498732160]`|`sub("\\d", "?", demo)`<br>`sub("[0-9]", "?", demo)`|
|Any lowercased alphabet|`[a-z]`|`sub("[a-z]", "?", demo)`|
|Any capital alphabet|`[A-Z]`|`sub("[A-Z]", "?", demo)`|
|alphanumeric or the underscore "_"|`\\w` or `[a-zA-Z0-9_]`|`sub("\\w", "?", demo)`|
|Any character (wild card)|`.`|`sub(".", "?", demo)`|
|NOT lower case alphabets|`[^a-z]`|`sub("[^a-z]", "?", demo)`|

What to notice?
- Any character placed inside `[]` would be treated as a possible character for matching
- `[^ ]` is the only "negation" type of pattern, i.e. anything character except those specified
  within the brackets will be matched.
- Common character patterns have abbreviations that often start with `\`, e.g. `\w` or `\d`

[Exercise](../exercises/r_character_reg_expression.md)


#### Combining characters and frequencies to form patterns
Returning to our original problem of parsing a sentence in the job description.
```r
demo <- "Experience with Google Analytics and Google Optimize\nKnowledge of project management tools (JIRA, Trello, Asana)\n"
strsplit(demo, split=" ")
```
A simple solution is to substitute every occurrence of one or more (frequency) non-letters (characters) into a single space.
Then separate the string by the space symbol.
```r
demo_subbed <- sub("[^a-zA-Z]+", " ", demo)
demo_subbed == demo
```
The output is likely identical to demo because the first non-letter symbol is a single space character, which was replaced with a space.
The key we're misssing is that we wanted this substitution to happen for "every occurrence".
To do this, we should use the function `gsub()` instead.
```r
demo_subbed <- gsub("[^a-zA-Z]+", " ", demo)
strsplit(demo_subbed, split=" ")
```
It turns out that you can enter regular expression into `strsplit()` directly for the `split` argument.
```r
strsplit(demo_subbed, split="[^a-zA-Z]+")
```

[Exercise](../exercises/r_reg_expression.md)

#### Getting a sub-pattern within multiple patterns
We can also combine multiple patterns into a single pattern. Imagine trying to get the website names
from the following demo:
```r
demo <- c("www.google.com", "www.r-project.org", "www.linkedin.com", "xkcd.com")
proper_demo <- paste0('https://', demo)
```
As humans, we recognize the "www" and the different endings (.org and .com) as not part of the name.

To specify the patterns we're seeing, you most likely will come up with something like
```r
pattern <- "https://(www\\.)?[^\\.]+\\.(com|org)"
sub(pattern, "caught ya!", proper_demo)
```
What to notice:
- Since `www.` was optional, we used `?` to say its appearance is optional.
- To specify a literal period, we had to type `\\.` otherwise it would be confused with the wild card symbol.
- Since the website names can contain weird symbols, e.g. `-`, we know the only character people would avoid is
  likely the period, so the website name was anything BUT the period.
- Notice how we used `()` to specify different sub-patterns in the overall pattern. Try removing the `()`
  and see which websites will not be captured.
- For website endings, we chose to limit ourselves to the finite endings that we know (you could add .gov, .io, etc)
  instead of matching arbitrary endings. This is generally good practice to avoid mistakes.

The above example, however, did not extract the website name. To do so, there's another
specific idea in regular expression substitution that you should know.
```r
pattern <- "https://(www\\.)?([^\\.]+)\\.(com|org)"
sub(pattern, "\\1 AND \\2 AND \\3", proper_demo)
sub(pattern, "\\2", proper_demo)
sub(pattern, "\\1SOMETHING.\\3", proper_demo)
```
What to notice:
- Each sub-pattern, enclosed by `()`, corresponds to an index, i.e. the first pattern can be referred
  with `\\1`, the second can be referred as `\\2`, etc. Again, the `\\` is being used to separate from
  a literal `1` in this case.
- This can be useful to obtain different 

[Exercise](../exercises/r_reg_exp_sub_pattern.md)

#### Other functions with regular expression
Besides substitution, there are a few other important functions that rely on regular expression.
- Is the pattern in the string or not? (Outcome TRUE/FALSE)
  ```r
  demo <- c("state", "statistics", "stat101", "no game", "probability")
  grepl("stat", demo)
  ```
  - Notice the output `matches` is the same length as the character vector you passed in,
- Identify the first character to ending characrter of the pattern in the string
  ```r
  demo <- c("state capital", "statistics textbook", "stat101", "no game", "probability")
  matches <- regexpr("stat[a-z]+", demo)
  attributes(matches)
  match_lens <- attr(matches, 'match.length')
  substr(demo, matches, matches + match_lens)
  ```
  - Notice how `regexpr()` returned data that had "attributes" that could be extracted
    using the `attr()` function. To find the list of attributes you can use `attributes()`
    This gets into a topic called objective oriented programming which we will not cover.
    You should consider the output from `regexpr()` to have multiple values associated with it,
    but instead of storing the output in a list with multiple values, it has the main output
    and associated attributes.
  - We're using `substr()` in a vecrtorized fashion where each string is subsetted using
    a different start and ending position.

#### Regular expression in practice
One thing to know about regular expression is that it is a very heavy trial and error process.
You should always double check your results and you should always Google for a solution since
someone else has likely encountered the same question.

Most software systems are designed such that "free text" is changed to drop-down menus so the input
is more predictable. Problems that require regular expression are
likely natural text which has many edge cases that rarely can be 100% captured by regular
expression.

The best way to learn is to keep trying :)

{% include lib/mathjax.html %}
