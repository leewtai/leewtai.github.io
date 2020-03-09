# HW5 - More data cleaning

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
  weird_data <- read.csv('YOUR_PATH/poorly_formatted_data.csv',
                         stringsAsFactors=FALSE)
  ```
  - What is the dimension of this file?
  - Please show the first 5 records.
- You should have noticed 2 issues. The decimal symbol and the symbol used
  to separate different values are not what `read.csv()` expects.
  - What symbol is being used instead of the usual `.` for decimals?
  - What is being used to separate the different columns?
- `csv` is short for "comma separated values", turns out we can change
  the symbol that separates the values and the symbol that acts as the decimal point.
  Find the arguments through the documentation `?read.csv` and try to load the data again with `read.csv()`:
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
  - Please correct this value by overwriting it with an appropriate value. Appropriate here means that if you gave this data to someone else, they would know that this data point was corrupted.
  - Please overwrite the column with the correct numeric data in the original data frame.
  - Please write the data out to a CSV file using `write.csv()` with the name `"better_formated_data.csv"` and make sure the argument `row.names=FALSE`.
  - In 2 sentences, please describe what does `row.names=TRUE` do to the data in `write.csv()`?
  - Pleaes load the clean data using `read.csv('YOURPATH/better_formated_data.csv')`
  - Please plot the scatter plot with the first column on the x-axis and the second column on the y-axis. Please label the axes according to the names of the columns.

Side comment: You should NOT correct the file `poorly_formatted_data.csv` directly because now your code records all the cleaning done to the data.

## Q1 Spatial data
The government has been collecting weather information for quite some years and 
a calibrated version of this data exists through [NOAA](https://www.ncdc.noaa.gov/ushcn/introduction).

In `hw5_spatia.zip` on Canvas, there are 3 station's data that was converted into a CSV file for
you using a similar process to Q0 above. You could download the raw data in the future using
the information under **Data Access** on the NOAA page. We will not work with the raw data yet.

Please download and unzip the file on Canvas (no need to use R to do this).
This contains 2 types of csvs:
- `station_metadata.csv`: this contains metadata for the station like location, state, etc.
- Station measurements data in the format of `STATIONNAME.VARIABLE.csv`
  - We are only using the US data so the station names begin with `USH` followed by 8 digits.
  - The variables can be `prcp`, `tmax`, or `tmin` which stands for precipitation, maximum daily temperature, and minimum daily temperature.

The above description is all for context and nothing needs to be done for them yet. The following questions intentionally gives fewer instructions than the past homeworks.

- What are the different types of metadata within `station_metadata.csv`?
