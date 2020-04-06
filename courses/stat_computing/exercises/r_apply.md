#### Exercise

```r
mat <- matrix(c(1, 5, 3,
                2, -1, 10,
               -3, -5, -10), ncol=3)
```

Please predict what the following commands would output:
1. `apply(mat, 2, max)`
2. `apply(mat, 1, min)`
3. `apply(mat, 2, function(x) max(abs(x)))`
4. `apply(mat, 1, function(x) sum(x > 0))`

Notice that the last two problems can be rewritten as:
```r
fun1 <- function(x){
    return(max(abs(x)))
    }
apply(mat, 2, fun1)

fun2 <- function(x){
    return(sum(x > 0))
    }
apply(mat, 1, fun2)
```
