#### Exercises

- Define `coin <- c("head", "Tail")`
    - What is the length of `coin`
    - What is the data type for `coin`
    - Change the first values within `coin` to `"Head"`
- Run the following code
  ```r
  n <- 20
  coin <- c(0, 1)
  coin_tosses <- sample(coin, n, replace=TRUE)
  ```
  - What is the length and data type of `coin_tosses`
  - What is the 3rd element of `coin_tosses`? (notice how this changes from run to run
- What is the class and length of `mix_vec <- c(1, "tail")`
- If I have the vector `dice <- c(6, 5, 4, 3, 2, 1)`, please define a variable named `small_dice`
    using `dice` and subsetting that is equivalent to `c(1, 2, 3)`. Hint: what does `dice[c(4, 3)]` return?
- What is the length and class of an empty vector, `c()`?
