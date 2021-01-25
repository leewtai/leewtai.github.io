# HW1 - Basic data manipulation

Before we calculate the final grades, we often normalize different categories like homework, exams,
participation, etc. This requires subsetting and aggregating data that is common across most data
analytics jobs which we will do in this homework.

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
points for each assignment and is not a real student. Please write **the code** that extracts the fake student
data using boolean vectors (this will be used in the future homeworks when we need to convert the grades
into percentages). In other words, we want a variable with only the data from the fake student.
Hint: `is.na()` can detect whether a value is an `NA` value in a vector.

#### Q6
Since the homework has a different weight from the other assignments, we often need to process it separately.
Please write **the code** that can extract the columns that correspond to the homework columns, i.e. create
a subset of data that only contains the homework scores. Please name your variable sensibly.

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
You should write your code here as if you do not know how many sections (e.g. there could be 100 sections)
there are in the data but need to infer it from one of the columns. Hint: there are multiple
approaches but `unique()` could be useful.
