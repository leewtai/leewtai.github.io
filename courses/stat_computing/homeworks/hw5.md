# HW5 - More data wrangling

## Q0 Correcting data format
One of the students have had an issue loading data for a different class into R.
Turns out this dataset has a few good exercises in it. The final result
should be a data frame with 2 numeric columns in it. I have only
changed the name of the file, the rest is real.

For Q0, answers are only necessary for the sub-bullet points where the main bullet
points are for context.

- Please find the data `poorly_formatted_data.csv` on Canvas, and load
  it into R using the following code.
  ```r
  weird_data <- read.delim('YOUR_PATH/poorly_formatted_data.csv',
                           stringsAsFactors=FALSE)
  ```
  - What is the dimension of this file?
  - Please show the first 5 records.
- You should have noticed 2 issues. The decimal symbol and the symbol used
  to separate different values are not what `read.delim()` expects (this just separates values by tab rather than commas)
  - What symbol is being used instead of the usual `.` for decimals?
  - What is being used to separate the different columns?
- `csv` is short for "comma separated values", turns out we can change
  the symbol that separates the values and the symbol that acts as the decimal point.
  Find the arguments through the documentation `?read.delim` and try to load the data again with `read.delim()`:
  - What is the dimension of this file?
  - What are the **names** and **classes** for the 2 different columns? Please use `lapply()` and `class()` to answer this in one line.
- Your previous attempt should have a disappointing outcome. Turns out one value within your data does not follow the same format as other values which is causing the entire column to be interpreted incorrectly. To identify this value, there are many ways but we will take the 2 steps approach for this question: first try to convert the values into numerical values, then identify which value failed the conversion to fix the data.
  - To convert the values into numerical values, we want to use `as.numeric()`. What will `as.numeric()` if we forcefully converting the values as is? (Notice this is working backwards)
  - We know that `as.numeric()` works with characters like "4.2" so we want to convert the data into a similar format. Below is a function that takes in 2 character vectors, one for the character and one the symbol that we want to convert into our usual decimal point. Please use `sapply()` to apply this function to all values to the problematic column.
    ```r
    convert_decimal <- function(text, symbol){
        return(sub(symbol, ".", text))
    }
    # Small demo
    print(convert_decimal('9_01', '_'))
    ```
  - Use the result above along with `as.numeric()` and possibly other functions, please subset out the problematic data point and print out its value.
  - Please correct this value by overwriting it with an appropriate value. Appropriate here means that if you gave this data to someone else, they would know that some data points were corrupted if they calculated any statistics using it.
  - Please overwrite the column with the correct numeric data in the original data frame.
  - Please write the data out to a CSV file using `write.csv()` with the name `"better_formated_data.csv"` and make sure the argument `row.names=FALSE`.
  - In 2 sentences, please describe what does `row.names=TRUE` do to the exported data from `write.csv()`?
  - Pleaes load the clean data using `read.csv('YOURPATH/better_formated_data.csv')`
  - Please plot the scatter plot with the first column on the x-axis and the second column on the y-axis. Please label the axes according to the names of the columns.

Side comment: You should NOT correct the file `poorly_formatted_data.csv` directly because now your code records all the cleaning done to the data and now everyone can replicate your steps.

## Q1 Spatial data
The government has been collecting weather information for quite some years and 
a calibrated version of [this data is maintained by NOAA](https://www.ncdc.noaa.gov/ushcn/introduction).

For this problem, imagine that you are a research intern for a climate scientist
who wants to study the annual precipitation for different locations over time.

In `hw5_spatia.zip` on Canvas, there are `k` station's data that was converted into a CSV file for
you using a similar process to Q0 above. You could download the "raw" data in the future using
the information under **Data Access** on the NOAA page (not CSVs!). We will not work with the raw data yet.

Please download and unzip the file on Canvas (no need to use R to do this).
This contains 2 types of csvs:
- `station_metadata.csv`: this contains metadata for the station like location, state, etc.
- Data on station measurements in the format of `STATIONNAME.VARIABLE.csv`
  - We are only using the US data so the station names begin with `USH` followed by 8 digits.
  - The variables can be `prcp`, `tmax`, or `tmin` which respectively stands for total **monthly** precipitation, monthly average of the daily maximum temperature, and monthly average of the daily minimum temperature.
  - The columns `value0`, ..., `value11` correspond, respectively, to the January-December measurements.
(If you want to understand these, please see the [NOAA website](https://www.ncdc.noaa.gov/ushcn/introduction), under "Data Access", there's a ftp hyperlink which has a readme.txt file with detailed explanations.)

The above description is all for context and nothing needs to be reported for them yet. The following questions intentionally gives fewer instructions than the past homeworks.

- What are the names of the metadata columns within `station_metadata.csv`? 
- What value represents missing values in these files?
- How many stations are there in the zip file?
- Please write the **code** that creates a single data frame that contains the **yearly
  total precipitation** for each station in the zip file. The columns should represent
  different stations, with the exception that the first column should record the "year"
  information. Different rows should represent different years. Please make sure the `colnames()`
  of the data frame are either "year" or the name of the station.
  You should keep all data records, i.e. if an old station has data in the 1890 but no other station does, the final data frame should have a row for 1890. There should not be other pieces data in this data frame. For grading, please report
  - **the dimensions** of your final data frame
  - **the range of the years** covered in your data frame (range = max - min)
  - **the number of missing values** in your data frame
  - Please use `apply()` in your code to get the annual totals.
  - Please treat missing values as 0 when calculating this total (side comment: think about how would you recommend to handle this in real life?)
  - Hints/Warnings/Clarifications:
    - Please first examine the data you have, the data you want, then think backwards.
    - To get all files with a particular naming pattern in your current directory, hint: `list.files(pattern='tmax')`
    - To help with subsetting repetitive names: `paste('hello', 0:3, sep="")` OR recall `grepl('dflag', c('dflag1', 'dflag2', 'value3'))`
    - "total" means to add up the precipitation over different days.
    - To grab the first `m` characters starting at the x'th index in a character value, `substring('hello', 1, 4)`
    - You can overwrite the names of a data frame using the assignment operation `colnames(df) <- c('a', 'b', 'c)`
    - How can you ensure the years are aligned across the different stations


## Q2 tapply() or aggregate() practice
Please summarize the data frame from Q1 to obtain the **decade total** precipitation for the different stations.
- Please separate the years into different decades first, e.g. 1801-1810, 1811-1820, etc, then calculate the total
precipitation.
- Please use `tapply()` OR `aggregate()` to get the decade total precipitations.
- Please treat missing values as 0 again.
Hints:
- To split the years into different factors
  ```r
  rand_nums <- sample(1:30, 5, replace=TRUE)
  cut(rand_nums,
      breaks=seq(0, 30, by=10),
      include.lowest=TRUE)
  ```
  Notice that `(10, 20]` is the notation for an interval that includes 20 but does NOT include 10.
