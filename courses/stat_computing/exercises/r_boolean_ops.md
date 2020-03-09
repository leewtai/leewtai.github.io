#### Exercises

- Try to explain the following lines of code to another peer,
  please explain the data types for each variables and whether
  a vectorized operation is used, then explain the code in
  terms of words.
  ```r
  n <- 10
  coin_tosses <- sample(c(0, 1), n, replace=TRUE)
  is_head <- coin_tosses == 1
  tails <- coin_tosses[!is_head]
  more_or_equal_heads <- length(tails) <= sum(is_head)
  print(more_or_equal_heads)
  ```
- Try to explain the following lines of code the same way:
  ```r
  n <- 20
  coin_tosses1 <- sample(c(1, 0), n, replace=TRUE)
  coin_tosses2 <- sample(c(1, 0), n, replace=TRUE)
  diff_tosses <- coin_tosses1 != coin_tosses2
  head_first <- coin_tosses1 == 1
  diff_tosses & head_first
  diff_tosses | head_first
  ```
