# Learning R through Examples and Errors (for Non-programmers)

#### What do you mean by teaching R via examples and errors?
The biggest challenge and annoyance for many non-programmers who want to learn R is:
- The overwhelming amount of details that create a steep learning curve yet seems useless for early programming
- The shallow amount of details when learning via copy/pasting code because you
  don't have the confidence how things would change in practice

This is written to hopefully strike a balance for people who feel both problems.
To achieve this, we will introduce the programming concepts while performing some
data analysis. We will also introduce examples and errors that will help correct
your misconceptions of the code. We will constantly ask you to predict/guess
what would happen under a different scenario to deepen your understanding of basic R programming.

Overall, we will **focus** on data wrangling and simulations (e.g. working with non-rectangular
data, joins, for-loops) but will **not focus** on data structures and algorithms
efficiencies (e.g. sorting, recursion, difference between long vs double).


#### Problems
- [Problem 1, How to simulate Law of Large Numbers?](lectures/learning_r_lln.md)
- [Problem 2, How to visualize data?](lectures/learning_r_data_viz.md)
- [Problem 3, Data wrangling](lectures/learning_r_data_wrangle.md)
- [Problem 4, Summarizing segments of data quickly](lectures/learning_r_summarize.md)
- [Problem 5, Working with text data](lectures/learning_r_text_manipulation.md)
- [Problem 6, Scraping and calling APIs](lectures/learning_r_scraping_and_api.md)
- [Problem 7, Validating math using simulations](lectures/learning_r_validating_prob_simulations.md)


## What we didn't cover
If you've read through the entire document to this point. You should feel relatively comfortable with
basic data analysis:
- Getting data from the internet programmatically
- Dealing with different data formats
- Wrangling data from a non-rectangular format to a rectangular format that is easy to analyze
  (and understand why people choose one over another)
- Applying calculations across different segments of the data
- Visualizing the data
But more importantly, to not take operations done by the computer for granted! A lot of
details are necessary to enable automation and this is just the beginning.

What we haven't covered that you'll learn in other computing courses:
- Data structure which is much deeper than the data types we've been discussing
- Algorithms like recursion and sorting which will deepen your knowledge of computational complexity
- Structuring code or a data pipeline
- Working backwards from a list of specifications. 
- How to wrangle/analyze big data, i.e. where data can exist across multiple machines and files beyond just your computer.
- ... many many more

#### My assumptions
My assumption is that you have been exposed to
- basic statistical concepts like the average, sample standard deviation (vs population variance),
  and histograms.
- Used a calculator

#### Computer setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../../setup/conda_and_navigator_setup.md)
so you could learn R, Python, or Julia in the future.


{% include lib/mathjax.html %}

