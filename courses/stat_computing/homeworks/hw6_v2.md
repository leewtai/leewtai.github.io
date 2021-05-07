# HW6 - Calling APIs and Text Manipulation

## Q0 Getting USDA Agriculture Data
This problem is focused on using `httr` to call the US Department of Agriculture (USDA) API, QuickStats, to
obtain state level agricultural data. Commodity traders pay attention to this data since they have major
implications about prices, specifically good harvest yields low prices and vice versa.

This problem is broken into 4 steps:
1. Requesting for credentials called the API key
2. Calling one API to understand the options
3. Calling another API to get the records
4. Visualize teh data over time

#### Q0.1 Request for an API key
Please follow the instructions under **"Request API Key"** for USDA's [QuickStat API](https://quickstats.nass.usda.gov/api).
For convenience, please save your credentials on a file called `usda_quickstat_api_key.txt`  following this example: 
```r
library(jsonlite)
cred <- list("usda_quick_stat_api_key" = "MY_API_KEY")
write_json(cred, "usda_quickstat_api_key.txt")
```

Please do **NOT** show your code here to the grader, you will need this file for later.
In general you should never share your credentials with other people. We will take a point off if your credentials are showing anywhere in the assignment.
We will trust that you did this step, i.e. you do not need to print/show anything, given it's necessary to finish the later tasks.

Side comment: this is not the most secure way to store credentials, i.e. storing them in plain text format, but this is not the focus of this class.

#### Understanding the options
The API has many parameters and we do not know the possible values we can set these parameters. To understand the options available to us, we need
to call a specific API endpoint `/api/get_param_values` also listed under ["Usage"](https://quickstats.nass.usda.gov/api).

Specifically, the parameters of the API define different dimensions of the data, e.g. crop type (like corn vs soybeans), sampling method (like census vs surveys), sectors (like crops vs animals). For each parameter, it can take on different values, e.g. "CORN" vs "Corn - Sweet", etc that will specify, within the dimension, what values we want to retrieve.

For the parameters, you should look at the table at the bottom of the **"Usage"** at the API page.
For the second type, we need to leverage the API endpoint `/api/get_param_values` also listed under ["Usage"](https://quickstats.nass.usda.gov/api).

Please use the API to get all possible values under `commodity_desc` that have the word `corn` or `maize` (case-insensitive so CORN or Maize should also be matched if they existed).
Please show all code and print out the possible values.

#### Getting the data
Before we plot the data in the next problem, we need to get the data first. Please grab the data from the API endpoint `/api/api_GET` with the following specifications:

- Fixed Variables
  - `sector_desc="CROPS"`
  - `domain_desc="TOTAL"`
  - `agg_level_desc="STATE"`
- Variables with multiple values
  - `commodity_desc` should vary over the values from the above `commodity_desc` that are NOT "POPCORN"
  - `year`, all years between 1997 to 2018 (inclusive)

- Please wrangle the data into a single data frame such that each record is a row and the different features are the columns. Hint: you can either ask for a CSV from QuickStat or simply use `dplyr::bind_rows()`.
- Please report the number of rows and columns for this final data frame.
- In 2017, what is the ratio between the total production between the "I-states" vs all of the states combined (including I-states so this should be less than 1)? Please do this calculation for each commodity separately.
  - A state is an "I-state" if the first letter of its name begins with an "I". Please do not hardcode the I-states but use regular expression to identify them.
  - The `short_desc` will inform you whether the record is relevant to "production".
  - For corn we're only interested in values related to the grain OR seed (difference is whether it is dried or not).
  - If a state/year combination is missing, we will assume the production was 0 for simplicity.

#### Visualize the data
Please plot the ratio of total production between the I-states vs the entire US over the years. 
- Please make sure the different commodities are plotted on the same graph with different colors.
- Please make sure your axes are labeled and you have a meaningful title that highlights a message in the plot.
- Your plot cannot be a simple scatter plot.


## Q1 Text manipulation
On Canvas, you'll find a file titled `indeed_job_descs_2021_03_18_california.json`, this problem will walk you through how we generated the dataset
for the first practice midterm. Ultimately, we want to know the number of job descriptions that have Python vs R listed.

- Please wrangle the data such that we have a character vector where each value represents one job descriptions.
- Please split each job description such that each job description is now a character vector with length equally
  to its word count rather than one single character value as before.
  - Please answer what is the appropriate data type that can hold multiple job descriptions after we do this transformation?
  - Please split the words by non-alpha-numeric-underscore values (underscore is `_`), you should use
    `strsplit()` and `gsub()` in your solution.
- Please create a data frame where each row is a job description and each column corresponds to a different word, and each
  element within the data frame is the **total occurrence** of the word in the job description specified by the column and row.
  - This should NOT be case sensitive so "hello" and "Hello" should be counted together
  - We will ignore the difficult question of lemmatization so "runs", "run", and "ran" will be counted as **different** words
  - Hints but not required:
    - `table()` can count the frequency of differnt values in a vector.
    - `bind_rows` from the the package `dplyr` can combine different data frames by column names when some columns are missing
- Are some job descriptions repeated across the data? Yes/No, please show the code that demonstrates this. You can assume that
  if the word counts are identical across all words, they are the same job description.
- Please report the number of job description that mention "r" and the number of job descriptions that mention "python"


## Q2 Simulation
- Using the word frequency data frame above, please calculate the correlation between the word "r" and the word "statistics".
- Then please simulate the following 1000 times:
  - permute the values in the column mentioning "r" while keeping values in the column mentining "statistics" intact.
  - re-calculate the correlation between the 2 words.
- Plot the distribution of the simulated correlations vs the actual correlation value on the same plot. Please make sure all
  values are visible.
- Using the plot above, does the correlation between "r" and "statistics" in job descriptions found on Indeed in California seem
  likely or not likely due to chance? Please explain with fewer than 5 sentences.
