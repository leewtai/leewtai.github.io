#### Exercises

- What will the output be from the code below? Try to answer it without running code.
  ```r
  demo_list <- list(1:3, 2:4, 3:5)
  do.call(data.frame, demo_list)
  ```
- Why is the class of each of the "elements" from the different `out` variable after each `do.call()` function call, i.e. `class(out[[i]])` where `i` goes through the length of `out`?
  ```r
  dat <- list(1:3, c('a', 'b', 'c'))
  out <- do.call(rbind, dat)
  out <- do.call(cbind, dat)
  out <- do.call(c, dat)
  ```
