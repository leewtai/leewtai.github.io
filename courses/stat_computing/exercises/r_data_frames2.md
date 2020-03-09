#### Exercises

```r
student_roster <- data.frame(
    student_id = 1:3,
    family_name = c("Doe", "Lee", "Liang"),
    given_name = c("John", "Billy", "Sally"),
    dropped = c(TRUE, FALSE, FALSE)
    )
```
- What happens if I try to subset both the column and rows at the same time, e.g. `student_roster[2, c('family_name', 'given_name')]`
- How can you subset only students with id less than 3 using a boolean?
- How would you subset only columns where the column name has the word "name" in them? hint: `grepl('name', c('name', 'names', 'countries', 'punch'))`
