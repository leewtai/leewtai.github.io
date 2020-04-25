#### Exercise

- There are multiple ways to encode CSVs.
  - Read in the [Fisher dataset](data/fisher_1927_grain.csv) using `read.csv()`
    then write the data to a separate file using `write.csv()`. Call the file
    `fisher_rewrite.csv`.
  - Read in both `fisher_1927_grain.csv` and `fisher_rewrite.csv` using `readLines()`
    then compare them.
  - How is data formatted by `write.csv()`:
    - There is an extra column created, what is its column name?
    - What symbol was used to decorate the string values in the data.
