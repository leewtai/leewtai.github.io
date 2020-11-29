# Homework 3: Practice with SLR

#### Q1
True/False, we can always derive the estimates for the regression line slope and intercept with only summary statistics and not the granular data points.

#### For **Q2-Q6**, `X` and `Y` are vectors of data as in the usual regression setup.
#### Q2
If I multiply every `Y` value by a constant `a`, what happens to my estimates for the regression line? Show your derivations.

#### Q3
If I add a constant `b` to every `Y` value, what happens to my estimates for the regression line? Show your derivations.

#### Q4
If I multiply every `X` value by a constant `a`, what happens to my estimates for the regression line? Show your derivations.

#### Q5
If I add a constant `b` to every `X` value, what happens to my estimates for the regression line? Show your derivations.

#### Q6
Show that the sum of the residuals from SLR is always 0.


#### Hooke's Experiment
The famous Hooke's law describes the relationship between a spring's length and the weight it's carrying.

|Weight (kg)|Length (cm)|
|---|---|
|0|439.0|
|2|439.12|
|4|439.21|
|6|439.31|
|8|439.40|
|10|439.50|

#### Q7
What would be considered the response variable here?

#### Q8
Please fit a SLR to the spring data under the linear model below and report the fitted coefficients.

$$y_i = a + b * x_i + epsilon_i$$

#### Q9
What is your best estimate (best in terms of sum of squared error) for the length of the spring when the weight is 9 kg? Please include the units.

#### Q10
Calculate the standard error for the estimate in **Q9**?

#### Q11
Imagine you are working with Hooke, the physicist. He wants you to show, graphically, the relationship between the spring length and the weights along with
different uncertainty values. Please create a graph with the following characteristics:
- The data points from the Hooke's experiment as a scatter plot, weights on the x-axis, length on the y-axis.
- The axis should be labeled, with units
- The simple linear regression (SLR) line, colored as red
- For the uncertainty, we will express this as 2 blue lines (or curves) around the SLR. Choose a reasonable quantity to express the uncertainty at different weight values `x`, let's call this choice `Z(x)`. You should make sure `x` is chosen in a way that covers your graph.
  - One blue line should be the SLR line + 2 * the `Z(x)`
  - One blue line should be the SLR line - 2 * `Z(x)`
- A legend that explains the colored lines


### Wine Reviews
From Kaggle, there's a [dataset on wine ratings from WineEnthusiast](https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4). You can find it on CourseWorks under the file `hw3_filtered_wine_reviews.csv`.

We are going to predict the wine ratings, i.e. the `points`, based on a feature we will generate from the text.

To create our feature, here is a list of some common adjectives for wine: "fruit", "aromas", "acidity", "finish", "tannins", "cherry", "black", "ripe", "red", "rich", "fresh", "oak", "spice", "dry", "berry", "full", "plum", "apple", "soft", "sweet".

#### Q12
Choose 10 adjectives randomly from the list above using a pseudo-random number generator like `sample()` in R and report which adjectives you got. (In real life, this could be a good baseline against expert marketers).

Now process each of the `description` values:
  - Lowercase all characters
  - Replace all non-alphabetical characters with a space (hint: `gsub('[^a-zA-Z]+', ' ', "H0l1o")`)
  - Split the entire string by spaces
You should end up with a single vector of character values for each wine where each element is a word (typos may exist).

Let's create a feature for wine that equals to the total count of the chosen 10 keywords within the description. For example, if my words are `["finish", "fresh"]`, and the description is "This wine has a dry finish with fresh aromas.", Then the feature for this wine would be 2.

#### Q13
Now fit the linear regression by fitting `points` to this new feature. Report the coefficients you get for your regression line.

#### Q14
Your team about to launch some marketing description of their new wine. You, unfortunately, was given the task to predict the `points` of the new wine will receive from WineEnthusiast. What is your prediction if the count is `3`?

#### Q15
Now your boss wants to communicate out your prediction to the marketing team, which uncertainty should you report on your prediction for the new wine? Please report this in terms of an interval.

#### Q16
Please comment on why the uncertainty you chose for **Q11** and **Q15** are the same or different.

{% include lib/mathjax.html %}
