#### Exercise

Using the [Fisher dataset](data/fisher_1927_grain.csv) to do the following exercises:
- read in the data using `readLines()`
- Use `strsplit()` to separate each line into different values.
- count the length for each character vector from the output above
- Use `do.call()` and `rbind` to form a matrix with all character values.
- Use subsetting to separate the first row, the header information, from the rest, the data.
- Use `as.data.frame()` to convert the matrix into a data frame, then use
  `as.numeric()` to convert the numeric columns into numeric data.
- Overwrite the names of the columns with the header information before.
- Compare your output to `read.csv('fisher_1927_grain.csv', stringsAsFactors=FALSE)`
