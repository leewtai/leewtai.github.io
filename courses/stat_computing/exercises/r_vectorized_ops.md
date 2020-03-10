#### Exercises

- Identify the different vectorized operations in the following
  example that calculates the percentage of outliers using standardized units.
  ```r
  x <- 1:100
  x_avg <- mean(x)
  x_sd <- sd(x)
  x_std_units <- (x - x_avg) / x_sd
  outliers <- abs(x_std_units) > 1.5
  mean(outliers)
  ```
  - Hint: run each line and identify what variables are vectors vs constants.
 
