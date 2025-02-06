# HW2 - Processing Data before Applying Algorithms

#### Q0 - Simulating dependency

Please show, via math or simulation, that if $$Var(X) = Var(Z) = \sigma^2$$, and $$X$$ is independent from $$Z$$. Then if we define:

$$Y = \alpha X + \sqrt{1 - \alpha^2} Z$$

Then

- The variance remains the same, i.e. $$Var(Y) = \sigma^2$$
- The correlation can be specified $$Corr(X, Y) = \alpha$$

For those using a simulation, using a single "setting" is sufficient.

#### Q1 - The Problem of Collinearity

Below we'll simulate some regression data, where `Y` depends on `H` that is a numeric matrix with 3 columns.

```{r}
n <- 500

beta <- c(0, -1.5, 1)
p <- length(beta)
# H stands for hidden
H <- matrix(rnorm(n * p, mean=5, sd=3), ncol=p)
# Intercept is 0 as well
Y <- H %*% beta + rnorm(n, sd=4)
```

Use the result from Q0 to create a `X` feature matrix that is $$n \times 100$$ where 10 columns depend on $$H_{.,1}$$, i.e. the first column of `H`, 20 columns depend on $$H_{.,2}$$, and 70 columns depend on $$H_{.,3}$$. Please make this dependency such that the correlation between each $$H_{.,i}$$ and each column of `X` is between 0.5 and 0.9. 

- Perform cross validation and visualize the prediction performance (pick a sensible metric) between
  - regress Y on X
  - regress Y on W, where W is the result from PCA and $$k=3$$ (be sure you know why k=2 isn't reasonable even in this cheating mode)
  - regress Y on W, where W is the result from PCA and $$k$$ is chosen that preserves 90% of the variability in `X`
  - Comment on the difference or lack of difference
- Show the pairwise correlation between each column in $$W_{3\times p}$$ and $$H$$

Things to think about: do different normalizing procedures matter in this simulation?

#### Q2 - Weather

The data is from https://www.ncei.noaa.gov/products/land-based-station/us-historical-climatology-network

Use the data in `CourseWorks/Files/Weather/*` 

- The `tmax.csv` contains the monthly average of daily maximum temperatures.
- The columns titled `value{i}` are the temperature values for month `i`
- The `id` are different weather stations
- The year is the year
- The other columns are describe various data quality issues

Please do the following:
- Look at the first few entries of `tmax.csv`, this [readme](https://www.ncei.noaa.gov/pub/data/ushcn/v2.5/readme.txt) might be useful in understanding the data, please convert the data into Celsius and handle MISSING values appropriately.
- Please wrangle the data such that each column is a different weather station and each row is a "year month" combination, let's call this matrix `X`
- Which station has the most number of entries?
- Do PCA on `X`, (recall `prcomp()` in R)
  - For now, aggressively filter the data to avoid NA values
  - Do NOT scale the columns
  - What `k` should we choose if we want to preserve 90% of the variability in X?
  - Do you agree with the result from the heuristic above?
- Examine the first column in the rotation matrix, i.e. first eigenvector, visualize the magnitude of the loadings (with different colors) across the different longitudes/latitudes, what do you notice?
- Repeat the same for the 2nd column
- What would be the interpretation of what is captured by the first vs 2nd column?
- Repeat the same but scale the columns this time, which one do you believe captures more physics?

Thought experiment (no work required for this): if we transposed `X`, what type of relationship would we be trying to understand, i.e. flipping space as measurements and year/months as features.


#### Q3 - citations

In `CourseWorks/Files/Citations/*`, you'll see some citation data.

- `j_cunningham_citation_titles.json` contains the titles for the papers and the references
- `j_cunningham_citation.csv` (WARNING: no header, there should be 15 papers)
  - The rows represent the papers written by Prof Cunningham
  - The columns represent the papers referenced in each of the papers
  - Each entry $$X_{i, j}$$ is how often paper $$j$$ was cited by paper $$i$$
  - The order of the rows and colums are consistent with the order of the titles in `j_cunningham_citation_titles.json`
- Warning: these are old papers and contain several extraction errors!

Please do the following:
- What is the distribution of the number of citations across the 15 papers?
- Let's do PCA on the citation matrix
  - Assuming the total citation count is correlated with paper length, let's divide each row by the number of total citations.
  - Performn PCA by not centering, nor scaling the columns
  - Pick `k`
  - Look at the loadings for the first column in the rotation matrix, i.e. the first eigenvector, with the 0 line plotted. Come up with a method to "threshold" the loadings so you have 0 vs non-0 values.
  - Look at the titles for the references that correspond to the non-0 loadings.
  - Repeat the above for the 2nd eigen vector
  - Repeat the same until `k` (if your `k` was larger than 2)
- Report your findings
- Try to repeat PCA without scaling the rows but normalize the columns (e.g. center and scale), how do the loadings look different in this case?


#### Q4 - Explore voting patterns of senators using PCA

We've collected data from the [senate.gov](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.htm) saved in `CourseWorks/Files/Congress/*`.

In `votes.json`, you will find the Senate voting records from the 105th to 115th Senate. 
The file is organized by senators, each with an id encoded by `S` followed by a digit. For each senator,
their voting record for the last version of the bill is recorded, `1` stands for "Yea", `-1`
stands for "Nay", `0` stands for "Not voting", and `-9999` is used if there were issues during
data collection. The bills are labeled with the congress term (e.g. `106`), the session number (e.g. `1` or `2`),
then the issue ID.

Use PCA to explore the voting pattern. Please at least write down:
- What type of relationship do you want to discover
- How are you deciding what is your column vs row
- How are you filtering your data (warning: some senators get voted out so the data has NAs)
- What normalization choices might you make
- How would you validate (no need to carry this out) your results (there is `voters.json`)
- Carry out at least one attempt, it does not have to be good!

{% include lib/mathjax.html %}
