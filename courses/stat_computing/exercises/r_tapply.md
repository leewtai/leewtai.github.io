#### Exercise

- What's the output of the following?
  ```r
  n <- 5
  demo_df <- data.frame(a = 1:n, b = c(1, 0, 0, 1, 1))
  print(demo_df)

  tapply(demo_df$a, demo_df$b, sum)
  ```
- What's the output of the following?
  ```r
  n <- 5
  demo_df <- data.frame(a = 1:n, b = c(1, 0, 0, 1, 1), d = c("a", "a", "a", "b", "b"))
  print(demo_df)

  tapply(demo_df$a, demo_df[c('b', 'd')], sum)
  ```
