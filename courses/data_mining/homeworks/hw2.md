# HW2 - Simple Data Mining

This homework is to meant for you to do some basic data mining tasks using
statistics from your prior classes.

### Context - US's winner takes all voting system

Most of the voting in the US takes the form of "winner-takes-all" which encourages
the formation of a two party system. We will see if we can identify the party affiliations
simply by looking at the voting patterns.

We've collected data from the [senate.gov](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.htm)

#### Q1 Data wrangling of the Senate Voting
In `votes.json`, you will find the Senate voting records from the 105th to 115th Senate.
The file is organized by senators, each with an id encoded by `S` followed by a digit. For each senator,
their voting record for the last version of the bill is recorded, `1` stands for "Yea", `-1`
stands for "Nay", `0` stands for "Not voting", and `-9999` is used if there were issues during
data collection. The bills are labeled with the congress term (e.g. `106`), the session number (e.g. `1` or `2`),
then the issue ID.

Please wrangle this dataset into a matrix called `voting_matrix` so we can calculate the correlation between the senators'
voting behavior, i.e. we will run `cor(voting_matrix, ...)` in Q3 to identify how senators' vote with one another.

Please report the dimensions of your matrix and what percentage of the matrix does not contain `-1`, `1`, or `0`. For
example, if I only have 2 senators and 2 bills where one out of the four terms is not `-1`, `1`, or `0`, then I would
report `25%`.
- I'm intentionally not telling you what are the columns and what are the rows, this should be implied.

#### Q2 Expectations
Please articulate your expectations for the correlation matrix given the 2 party system.
- What's its dimension?
- How many modes do you expect to see in the distribution of correlation values?
- Where will the correlation values center?

#### Q3 Mining with correlations
Please calculate the correlation value between the senators' voting pattern, please set `use=pairwise.complete.obs`
in the function `cor()`.

- Please explain why R will warn you that some correlations cannot be computed.
- Please plot the histogram of the lower triangular values within the correlation matrix. Hint: `lower.tri`
    - Please comment on this histogram relative to your expectations from Q2. Side comment: make sure this makes sense to you!
- Please re-order the correlataion matrix such that it starts with the highest positive correlation (1) to the strongest
  negative correlation (-1) with respect to Senator McConnell's votes, i.e. the previous Senate majority leader who has
  served since 1985 (id=`S174`, member of the Republican Party). Note that the [majority leader](https://www.senate.gov/artandhistory/history/common/briefing/Majority_Minority_Leaders.htm) is the party's spokesperson for the party's position on issues.
  - It would make sense to filter out senators who do not overlap Senator McConnell.
  - Please try to visualize this re-ordered correlation matrix, hint: `image()`
- Please list the senators, if any, who have a negative correlation with Senator McConnell's votes but an **average** greater than
  0.2 correlation with the "possible Republicans".
  - We will define a 'possible Republican' as someone with a correlation of 0.2 or higher voting record with Senator McConnell.
  - You will need the file `voters.json` to get the names of these senators.
- Why might this group be interesting if they exist? This will **not be graded** by the grader but your projects
  will require you to make this kind of articulation. This should be done in 5 or fewer sentences.

#### Q4 Machine learning intuition with regression
We will compare 2 feature selection methods for regression, with the goal of predicting a senator's voting pattern.
In both methods, for any target senator, we will select 2 other senators to predict their vote on any issue.
- Method 1:
  - Pick the senators with the strongest positive and strongest negative correlation with the chosen senator.
  - Run OLS against both senators simultaneously.
- Method 2:
  - To identify the first senator, simply find the one senator with the strongest correlation.
  - Run OLS of the target senator against the first senator and obtain the residuals.
  - Identify the second senator by identifying the senator whose voting record has the strongest correlation with the residuals from above.
  - Re-run OLS against both senator simultaneously.

Please answer the following:
- Why isn't choosing the 2 senators with the 2 strongest positive correlations a reasonable strategy? This should be 3 or fewer sentences.
- What does `lm()` do when one senator has no voting record for a particular bill? Is the behavior different if the senator is the independent or dependent variable?
- For each senator, please randomly choose 20% of their bills data into a test set, then use the remaining 80% of bills to run both methods above. Please report which method has a better prediction performance according to what you see?
    - Do not impute the missing values
    - You should choose a prediction metric
    - This is not a full cross validation because we are not rotating the test set.
    - Please visualize the prediction performance across senators for both methods.

Side comment: For data mining purposes, one might look into the existence of a popular predictive senator!


{% include lib/mathjax.html %}
