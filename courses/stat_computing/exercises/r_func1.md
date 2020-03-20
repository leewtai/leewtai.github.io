#### Exercises

Using the same function below, please answer the following questions
```r
perc_error <- function(prediction, data){
    err <- prediction - data
    abs_err <- abs(err / data) * 100
    return(abs_err)
}
```

- What happens if you try to run `perc_error(9)`, i.e. missing one of the inputs?
- What happens if you completely delete the line with `return(abs_err)`, what happens
  when you run `perc_error(90, 100)`? What about when you run `outcoe <- perc_error(90, 100)`?
  (This is something weird that R does)
- Is `perc_error(90, 100)` the samer as `perc_error(100, 90)`?
- What is `perc_error(data=100, prediction=90)`? (We are passing the arguments in by name)
- What happens if you try `perc_error(90, "100")` (you should be able to explain this error!)
