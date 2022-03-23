# HW4 - Clustering Basics

This homework is meant for you to practice basic clustering with COVID data over different counties.

You **must** submit both your HTML (or PDF) + .Rmd file on CourseWorks.

Context: How did different counties experience COVID? Rather than tackling a county at a time, we will calculate some characteristics, cluster, then diagnose the different types of counties in the US.

### Question 0 - Explore the data

The [NYTimes has a GitHub repository with COVID data per counties](https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv)

- Please convert the cases into a wide format data frame, called `cases`, where each row is a county and the different columns are the `county`, `state`, `fips`, and the different dates, e.g. 2020-01-20, 2020-01-21, .... The cells under the dates should have the cases for that county on that day.
- Please write some code that can verify that your dates are ordered AND we do not have any missing dates. Explain your code and logic with at most 2 sentences.
- Please print out how many rows you have after converting the data into the wide format.
- For each county, calculate the maximum cases over all days. How many records have their maximum cases over time to less than or equal to 0? Please print out the corresponding `county` and `state` values for these records.
- Please filter the data such that we only have counties with known names. Then print out the dimension of your data frame.
- Please create a new data frame, called `avg_cases`, that insteads has the 7-day moving averge of cases in the cell rather than the cases themselves. Given our goal is in clustering and not prediction, your 7-day average should be averaging values starting 3 days before to 3 days after.
  - Pick one county then plot the cases vs the 7-day average cases on the same plot. The x-axis should be time and y-axis should be cases. Label your axes.

### Question 1 - aligning the data:

- If we tried to use the built-in `kmeans` function on `cases`, what error do we get? For this to not crash your notebook, use the function `try()` around your function call.
- We will align the "start of COVID" across counties before clustering using a crude method - finding the first day that had 200 or more cases (in the 7-day average), then get the following 365 days after that, store this in a variable called `df`.
  - Please remove any county that satisfies any of the following:
    - does not have 365 days worth of data
    - does not ever reach 200 or more cases
  - Please list the top 6 states or special districts that have their records removed this way.
- Now use `kmeans()` on `df` trying out 2, 3, ... 20 clusters. Please plot the ratio between the `betweenss` and `tot.withinss`for each of these different choices.
- How many clusters would you choose? For each cluster, average across the counties for each of the 365 days, we will call these the `avg_ts`, plot the different `avg_ts` on the same plot that highlight their temporal patterns.
- Using at most 3 sentences, how would you describe the clustering algorithm is grouping our counties?


### Question 2 - aligning the data, differently

- Please normalize the values in `df` by the county's maximum value observed in `avg_cases`.
- Please repeat the same steps with the clustering as above, i.e. identifying the optimal number of clusters. Warning, the clusters will not be as obvious as before, and repeated runs will likely result in different outcomes (i.e. you should run this multiple times and evaluate the clusters). Try your best at choosing a reasonable number of clusters, remember that our goal is to produce "useful" clusters!
- Please plot the average curve for each cluster, with a different color, then plot 5 randomly sampled curves from the cluster to show the uncertainty within each cluster. Please label your plots.
- Please write at most 5 sentences why normalizing by the maximum vs normalizing by the county's population can possibly yield different results.

### Question 3 - Giving clusters meaning

- Depending on the number of clusters you chose, you may get a different answer. For each state (e.g. California, Texas, etc), please calculate the distribution into different clusters.
- For each state, please perform a hypothesis test whether the counties are distributed proportional to the size of the cluster. Then sort (small to large) and plot the p-values from these tests against the line that has slope `1/num_states` and a 0 intercept. Please conclude whether you believe counties are distributed randomly across the clusters or not, i.e. do certain clusters have a preference for certain states.
- Depending on your answer above, what does a random or non-random distribution across the clusters mean about the clusters?
- Side comment: You have the representative curve for each cluster, the distribution of the states into different clusters. Often these could start giving people ideas for the meaning for different clusters.

### Question 4 - Final Project

Please articulate what the minimal dataset means for your project. Make sure you talk about
- minimal time range(s) or spatial coverage
- features that you expect to have
- the unit of record, i.e. a row in your data frame (people, cars, documents, etc)
- why this is related to your final project
