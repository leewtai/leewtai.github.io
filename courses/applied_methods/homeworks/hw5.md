# Homework5 - Visualizing for Validation

### Goals
The purpose of this homework is to give you a sense of "validating" models.

#### Question 0: Project 2 bombing validation.
On Canvas, you'll find a file called `Data/test_all_gps.zip` that contains all of the data in the third week
for Project 2. 
Please **visualize** your projected 2 predictions next to the actual GPS data on week 3, then report whether your
assassination attempt worked or not, i.e. were they within 5 meters and 10 seconds from the raw GPS values.
Please take note of the 5 minute constraint from the beginning of each data session.

- Your visualization should only plot the data "close" to your predictions.
- Your visualization does not have to include both the spatial and temporal distance (but this is possible!)
  but it should include at least one dimension.
- If your prediction are near the 5 minute beginning, you should label those points differently.


#### Question 1: Final project validation.
Please visualize the data **with** your model. The previous homework was only related to visualizing the data itself.
If you visualized your model with your data already, you should avoid to use the same graphic.
The motivating example here is that "a peer unfamiliar with your project" will rarely believe your
model/analysis is "reasonable" unless you can visually show how your model and data relate to one another.
Please make sure your model and data are clearly labeled and that you include a caption for the graph.

You do not need to explain your model for this assignment.

For example:
- if you have a regression, you could plot the fitted values against the data points.
- if you have a logistic regression, you could plot boxplots for the fitted probabilities for the positive vs negative cases.
- if you have a cluster, you could show the data by coloring the different groups differently.
- if you ran a simulation, what is the true underlying process vs the simulated realizations.
- if you are testing a hypothesis, you could plot the test statistic vs the test statistic under the null distribution.

Thought for curious students: how would your model behave if your data was perturbed, contaminated, or stripped of a feature?
