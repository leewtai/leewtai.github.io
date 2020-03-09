#### Exercises

Using the same data set, please answer the following questions.
```r
student_roster <- data.frame(
    student_id = 1:3,
    family_name = c("Doe", "Lee", "Liang"),
    given_name = c("John", "Billy", "Sally"),
    dropped = c(TRUE, FALSE, FALSE)
    )
```
- What happens if one of the vectors do not have 3 elements?
- What happens if you do not define the column name (e.g. delete `student_id =` but keep the data part)
- What is the data type of `dim(student_roster)`
