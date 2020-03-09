#### Exercises

- Try to articulate the final outcome of the following code
  ```r
  n <- 10
  coin_tosses <- sample(c(0, 1), n, replace=TRUE)
  is_head <- coin_tosses == 1
  tails <- coin_tosses[!is_head]
  more_or_equal_heads <- length(tails) <= sum(is_head)
  print(more_or_equal_heads)
  ```
