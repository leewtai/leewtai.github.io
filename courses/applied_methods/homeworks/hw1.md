# Applied Statistical Methods - Homework 1

### Goals
- Get you familiarized with the trustworthiness data
- Data wrangling exercise
- Exercise mixed models and bayesian models

### Format
Please return a **PDf** file with your solutions on GradeScope.

#### Question 0 - reproducing the S1 results from Trustworthiness paper

Here we are following the steps in the code.
- The response data is in the `trustworthiness.zip` file on CourseWorks under `data/S1/decisionTask`. Please combine all of these files into a single data frame.
- Let's first remove those who failed the attention check.
  - In the column named `"Trial Component"`, if the word `"Press"` exists, then this is an attention task for the participant. Participants are asked to press `E` or `I` key, the actual response is in the column called `Response`.
  - Please drop any participants who failed more than 30 percent of their attention checks. Does this match the value from study one?
- Using the data under `data/S1/demo`, please make sure the demographic information matches those mentioned in the paper.
- We want to get the trust level information for each "face"
  - Single face trust levels are in `stim_descriptives/S1_single_faces.csv`.
  - Ensemble trust levels are be calculated by averaging the `trust_level` for images that share an `ensemble_id` in the file `stim_descriptives/S1_ensembles.csv`.
  - To join the trust levels to the participant's responses, the `file_name` (from the single face data) and `ensemble_id` appended with `".jpg"` (from the ensemble data) can be joined to different parts of in the `Trial_Component` column from before (look at the data!).
- If the response is `e`, it indicates that the participant believes the single face is more trustworthy than the ensemble mean. Please calculate the percentage of correct guesses for each participant (i.e. each subjID).
- Please perform a hypothesis test, for each participant, with the null hypothesis being that participants are guessing whether the single faces are higher than the ensemble mean.
- Please create a visualization that attempts to answer "are guesses easier when the probe face is extremely trustworthy or extremely untrustworthy?" For example, if a face has a trust level of 1, then guessing the mean is higher than 1 should be easy, i.e. not just 50%.
- Please explain your visualization.

#### Question 1

In the file `stim_descriptives/S1_attractiveness_ratings.csv` contains the average attractiveness rating for each single face.
How would you model the relationship between attractiveness vs the trustworthiness according to the paper? Be sure to articulate:

- What are the expected ranges of attractiveness? What ranges are we observing in the data? Are these expected?
- What is Y vs X in your model
- What can we conclude about the relationship between attractiveness and trustworthiness if we fitted a linear regression model according to your specification? Please show your model.

#### Question 2 - simulation

Given the in-class simulation that simulated multiple measurements from the same individual, 

```
uniq_n <- 100
reps <- 5
n <- uniq_n * reps  # Sample Size
p <- 5    # number of features

p <- p + 1 # this allows for the intercept

X <- rnorm(n * p, 0, 2)
X_matrix <- matrix(X, ncol=p, nrow=n)
X_matrix[, 1] <- 1 # this is the intercept

beta <- runif(p, min=1, 2)
noise <- rnorm(n, 0, sd=1)

# This is how we think about Y being modeled by X and noise
Y <- X_matrix %*% beta + noise

# adding in the individual effect
individual_intercepts <- rnorm(uniq_n, 0, sd=5)
Y <- Y + rep(individual_intercepts, each=reps)

df <- as.data.frame(cbind(Y, X_matrix[, -1]))
names(df) <- c("Y", paste0("X", 1:(p - 1)))

df["subj_id"] <- as.character(rep(1:uniq_n, each=reps))

head(df, 4)
```

- How would you evaluate how well the random intercepts are estimated with the `lme4` package?
  - Please visualize the relationship between different values for `reps` and how well your random intercepts are estimated.
- Please visualize the relationship between different values for `reps` and how well your fixed effects are estimated.
- Please visualize the relationship between different values for `uniq_n` and how well your fixed effects are estimated (fixing reps at 5).
- If the distribution for the random effects did not have mean 0, what happens?
- Modify the simulation where there is no random effects but instead there is a binary feature, `X6`, that a subject has a 0 or 1 label (e.g. the subject speaks another language or not). The corresponding beta value will be 1. When fitting the model, however, still fit `X1` through `X5` with fixed effects and allow random intercepts for each subject. We will pretend that `X6` is unobserved. 
  - What would you expect to happen with this simulation?
  - Do things follow your intuition when the 0 to 1 labels are evenly split?
  - Do things follow your intuition when the 0 to 1 labels are not evenly split?


#### Question 3 - Posterior

We want to understand how fast different estimates converge to the truth given additional data points. Please visualize your answer.
- Let `p=0.2274` but pretend we do not know this.
- We will toss `n` coins with chance `p` to land Heads. (You should explore sample sizes start with 1 and increment slowly).
- Here are the competing estimates for `p`:
  - The proportion of Heads is the estimate for `p`
  - Using the conjugate posterior mean for `p`
    - please choose a prior that treats all possible `p` values equally
    - please choose a prior that gives more weight to `p` values closer to 0.5
- Please answer, are the competing estimates all unbiased for all values of `n`? Use a simulation to answer this.
