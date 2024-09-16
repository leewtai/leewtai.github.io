# Applied Statistical Methods - Homework 1

### Goals
- Get you familiarized with the trustworthiness data
- Data wrangling exercise
- Exercise mixed models and bayesian models

### Format
Please return a **PDf** file with your solutions on GradeScope.

#### Question 0 - reproducing the S1 results

Here we are following the steps in the code.
- The response data is in the `trustworthiness.zip` file on CourseWorks under `data/S1/decisionTask`. Please combine all of these files into a single data frame.
- Let's first remove those who failed the attention check.
  - In the column named `"Trial Component"`, if the word `"Press"` exists, then this is an attention task for the participant. Participants are asked to press `E` or `I` key, the actual response is in the column called `Response`.
  - Please drop any participants who failed 30 or more percent of their attention checks. Does this match the value from study one?
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

#### Question 3



#### Question 2

Imagine the true model `Y = 2 + 3 * X + error` where X is binary 0 or 1 and the errors are `Normal(0, SD=2)`.

Please use a simulation to justify your answers below:
- Assuming we will have 50/50 split of X values with 0 and 1, roughly how many samples would we need to have the SE for the slope to be less than 0.2?
- Assuming we will have 5/95 split of X values with 0 and 1, roughly how many samples would we need to have the SE for the slope to be less than 0.2?


#### Question 3



