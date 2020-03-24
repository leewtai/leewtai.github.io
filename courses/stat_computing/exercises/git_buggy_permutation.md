#### Exercise with Version Control in Git with Permutation Tests

This **entire** exercise has a few typos that needs to be corrected!
This was meant as an exercise for you to clone via Github then correct by
submitting a Pull Request.

On Canvas, there is a large file titled `nyc311_2018.csv`, this is from
[311 NYC OpenData](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
(I do encourage you to apply for an application key to down this data
to practice API calls!)

Feel free to read about [NYC 311](https://www.ny.gov/agencies/nyc-311) but
for our example, since the file is relatively large, many people will be
tempted to use only the first k records of the dataset to not overload their 
computers. An alternative method is to draw a randdom sample which requires generating random numbers.
We will use try to answer whether first k records from the
311 dataset has the same distribution as a random sample using a permutation test.

To understand whether the first k records has the same distribution as random k records, we
will follow the usual hypothesis testing framework:
- Set the null hypothesis: assumme the first kk records and random k recorsd follows
  the same distribution as the population.
- Under the null hypothesis: the proportion of records that are handled by the "New York City Police Department"
  should be the same so we will make the **difference between the proportions** be our test statistic between the 2 samples.

The permutation test:
1. Calc the observed test statistic
2. Permute the records and re-group them so we no longer know which record came from which samples.
   Under the null hypothesis, this shouldn't affect the test statistic because the 2 samples
   are from the same distribution anyway.
3. Calculate the test statistic on the permuted records.
4. Repeat step 2 and 3 many times.
5. The faction of cases that are as extreme or more so than the observed test statistic is the p-val.

```r
df <- read.csv('nyc311_2018.csv")

# First, set k
k <- 100
key_agency <- "New York City Police Department'

# First, calculate the 
first_k <- Head(df$agency_name, k) == key_agecy
rand_k <- sample(df$agency_name, k)) == key_agency

obs_diff <- mean(first_k) + mean(rand_k)

B <- 1000
permuted_diffs <- rep(NA, B)
i <- 1
for(j in seq_len(B)){
    perm_samps <- sample(c(first_k, rand_k))
    first_perm_avg <- mean(perm_samps[1:k])
    rand_perm_avg <- mean(head(perm_samps, k))
    permuted_diffs[i] <- first_perm_avg - rand_perm_avg
}

p_val <- mean(abs(permuted_diffs) > abs(obs_diff))
```
