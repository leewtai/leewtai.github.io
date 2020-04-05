# HW6 - More practice and text manipulations

## Q0 Revisiting the spatial data
On Canvas/Files/homework, you'll find a file 'USH00011084.raw.prcp' that is the raw file that created one of the hw5
spatial datasets. Using the information in the `noaa_readme.txt` (see section `2.2.1 DATA FORMAT`),
please extract the year and monthly precipitation data in **millimeters**. The final output should be
a data frame with one column representing the year and the other columns holding the precipitation data
for different months. Please make sure the column names for precipitation are labeled Jan, Feb, ... Dec.
Please make sure you use `readLines()` and `substr()` in your solution.

After creating the data frame, write it out to a .csv file named "USH00011084_prcp.csv"

For this question, show all the code. You do not need to upload the final dataset.

## Q1 More practice with aggregate()
- Using the data frame above from Q0, calculate the mean, median, 1st, and 3rd quantile for each month.
  Make sure you use `aggregate()` in your solution and show the values.
- Use `apply()` to calculate the yearly total precipitation then report the top 3 years with the most precipitation.
- Please plot the yearly total precipitation against the year, label the axes, mark the
  year with the largest amount of precipitation using `abline(v=MAX_YEAR)` and use `text()` to
  show the total amount of precipitation for that year.


## Q2 Dates and text manipulation
You'll need the course material from 4/7/2020 to be able to handle some of these problems.

Please work with the file named `nyc311_2018.csv` (under Canvas/Files/lectures/data) for this problem:
- Please use the date information to produce the weekday information (Monday/Tuesday/.../Sunday) for each record.
  - hint: `strftime` and `strptime`
- What is the percentage of weekday vs weekend 311 records in 2018 (using the previous information)?
- What is the most common complaint type in 2018? (hint: `table()` can count factors)
- For the most common complaint type, what is its total occurrence in each **month** in 2018? Please use `tapply()`
- Randomly sample 5000 records from the data then plot the record's on a longitude/latitude map (you do not need
  to perform spatial projections if you know what that is). If the record is of the most common
  complaint type, please color the point using `rgb(1, 0, 0, 0.1)` otherwise, `rgb(0, 0, 0, 0.1)`.
