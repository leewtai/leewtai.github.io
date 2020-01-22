# HW1 - practice

Please return all the code used to do the calculations. If the question asks you to report
anything, please follow this example:
```r
# (EXAMPLE QUESITON) Please create a vector called "blocks" that has the integer from 1 to 121 and report the average of that vector.
blocks <- 1:121
mean(blocks)
# The average is 61 
```
Note that the `#` is how we write comments into R.

#### Q1
On Canvas, there's a data set `anony_grades.csv`, please write out **the code**
that will read the data into your console and creates two variables `n_row` and `n_col`
the respectively store the number of rows and columns in this dataset.

#### Q2
Please report the number of rows and columns in this dataset?

#### Q3
What error message will be returned if I misspell the file name?

#### Q4
What error message will be returned if I misspell the function that reads in the data?

#### Q5
The student with no section (`sec=NA`) is actually the row that records the total possible
points for each item and not a real student. Please write **the code** that extracts the fake student
data using boolean vectors (this will be used in the future homeworks when we need to convert the grades
into percentages). Hint: `is.na()` can detect whether a value is an `NA` value in a vector.

#### Q6
Since the homework has a different weight from the other items, we often need to process it separately.
Please write **the code** that can extract the columns that correspond to the homework columns.

#### Q7
Please write **the code** that can subset the data for students in the first section, i.e.
`sec=1` and **report** the number of students and the average for the final.
To calculate the average here, please limit yourself to using only the function `sum()`, `dim()`, subsetting,
and division instead of using the built-in function `mean()`.

#### Q8
Please try to compute the average final grade for the students in the second section using
the `mean()` function. Please report the value you get if you keep the defaults and the value
you get if you change one optional argument to `na.rm=TRUE`.

#### Q9
Please loop over the 2 sections to compute their respective median final grades and report the result.
