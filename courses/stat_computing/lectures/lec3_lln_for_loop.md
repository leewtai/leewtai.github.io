## Applied Statistical Computing - Law of Large Numbers and For-loops

#### Last lesson review

In R, we introduced:
- Variable names
- Vectors
- functions that apply to vectors

```{r}
coin <- c(0, 1)
sample_size <- 5
pop_avg <- mean(coin)

sample_pop_avg_diffs <- c()

tosses <- sample(
  coin,
  sample_size,
  replace=TRUE)
sample_avg <- mean(tosses)
sample_pop_avg_diff <- sample_avg - pop_avg
sample_pop_avg_diffs <- c(
  sample_pop_avg_diffs,
  sample_pop_avg_diff)
```

Now we need to repeat the bottom part many times to get "sample_pop_avg_diffs" (note the plurality).

#### Basic structure of for-loop

- Body of the loop
- The different iterations of the loop
- Placeholder across different iterations

How can we avoid typing out the repetitive `+` signs?
```r

1 + 2 + 3 + 4

```

#### How to store the values separately?

Turns out that `c()` applies to vectors!
```{r}
coin <- c(1, 0)
biased_coin <- c(1, coin)
```


#### Tying the for-loops back to LLN

- The for-loop will repeat, whatever is in the body, equally to the length of the vector it is looping over.
```{r}


```



{% include lib/mathjax.html %}
