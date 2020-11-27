# Final Project

The goal of the final project gives you an opportunity to demonstrate your learnings from regression!

- (2 pts) Email your question and dataset choice to Owen and Wayne by 05/01/2020 so we know you're on track.
- (65 pts) Final Report due **05/08/2020**, this should be a pdf file submitted on Canvas. The report should be between 5 to 10 pages (double or single space). You should not print out raw data. Code will be submitted separately and do not count towards your page limit.

## Dataset
Normally, a statistics class would have you start with a question, then collect the necessary data related
to the problem. Due to the limited topics we've covered so far, we will instead start with existing datasets
then ask you to explore/analyze it. This is closer to a data mining exercise. 

You are expected to choose 1 dataset only out of the following options. Please read the requirements below before you choose your dataset.

- US Accidents at \url{https://smoosavi.org/datasets/us_accidents}
- World Bank Indicators for Countries at \url{https://data.worldbank.org/indicator}
- UC Irvine Data Repository for Machine Learning at \url{http://archive.ics.uci.edu/ml/datasets.php}
  - You must find a dataset with at least 200 data points and 4 features if you choose something from here.
- Choose your own dataset! This needs approval but feel free to use a dataset if you're working on a project in a different class.

## Report

#### A real problem/question (15 pts)
From the dataset, please identify a question that could potentially could be answered by the dataset. 

An example of a bad (but popular) question is to predict Amazon reviews based on the written review. This is a bad question because it's not clear why Amazon would want to infer a rating from the written review given all written reviews come with a star rating already.
People who fit this model often do so because the Amazon rating is the only numerical variable available.

On the other hand, a real problem/question does not need to be difficult. A real question could be how much does the base salary
of a public servant in NYC scale with their tenure? Estimating the coefficient is a real question especially if you can compare 
people who started in different years.

One way to evaluate whether a question is interesting is to see if a certain population would change their behavior based on the outcome.

For this segment, please 
- Clearly state your "problem/question" your analysis aims to answer
- Answer how would linear regression (or logistic regression) would help you address the question. For example, do the parameters, the ability to predict new records, or uncertainties from the model address your question?
- Draw a DAG for the data generation process of the dependent variable. 
  - This just needs to be reasonable, not necessarily correct
  - This DAG can refer to variables that are not available to you
  - This goal is for you to think about the data generation process vs what is available to you.

Note that your analysis can be inconclusive! Sometimes a negative result (i.e. not finding a pattern) is valuable information! Feel free to study external sources of information (e.g. Urban Planning or Economics textbooks) to support your question but this is not necessary.

#### A description of the data (5 pts)
Given your question/problem, please perform some exploratory analysis on the dataset. For example, if I'm analyzing payroll
information between genders, I should look at the boxplot between salary distribution split by gender. I should check the percentage
of male vs female payees I have in the dataset and I should see if any outliers exist in the data. One visualization is expected in this section. 

#### Multiple solutions and a choice (20 pts)
In your analysis, there needs to be at least 2 different models that answer the problem. There are many ways to create different models:
- different subsets of features in your model
- different transformations of the data (e.g. $$\sqrt{salary}$$ vs $$\log(salary)$$
- methods for estimating missing values
- different procedures that clean the training data (NOT the testing!)
- ...
Any single or multiple choices from above would result in a different "model".

For this section, please show
- the different solutions
- how you chose one solution over the other solution(s), there needs to be at least one visual evidence for this.

#### Uncertainty and validation (15 pts)
This section can be embedded into the section above.

- Your report should address how does uncertainty from the data affect your choice of model or your answer
to the original problem. Classic examples of this is creating confidence intervals for the coefficients rather than using the regression estimate alone. Showing the volatility of the cross validation results is another classic method for prediction problems. 
- Your report should validate your assumptions. These could be the classic linear regression assumptions or questions about the generalizability of the dataset. Please demonstrate you understand what assumptions exist and which ones may be addressed with your data and which may not be addressable by data (when appropriate). 
- (optional) A simulation may be appropriate depending on your question (e.g. censoring an entire state/country's data to see how your model changes).

We do not expect you to validate all assumptions or address all sources of uncertainty but you need to demonstrate you understand these concepts and how they affect your regression/conclusion, e.g. why does cross validation demonstrate how uncertainty from the data can affect our conclusion.

#### Conclusion (5pts)
What did you conclude from your analysis? This may or may not be conclusive e.g. if you were doing inference and could not
conclude the parameter of interest is significantly different from 0, that's a perfectly fine outcome! We are looking for no more than a paragraph for this.

#### Code (5pts)
Please submit your code separately from your report.

{% include lib/mathjax.html %}
