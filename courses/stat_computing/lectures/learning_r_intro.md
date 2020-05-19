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

#### My assumptions
My assumption is that you have been exposed to
- basic statistical concepts like the average, sample standard deviation (vs population variance),
  and histograms.
- Used a calculator

#### Computer setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../../setup/conda_and_navigator_setup.md)
so you could learn R, Python, or Julia in the future.

#### Problems
- [Problem 1, How to simulate Law of Large Numbers?](learning_r_lln.md)
  - Variables
  - Functions, arguments, default values
  - For-loops
- [Problem 2, How to visualize data?](learning_r_data_viz.md)
  - Data types beyond numeric values
  - Subsetting data
  - Plotting
- [Problem 3, Data wrangling](learning_r_data_wrangle.md)
  - JOINs between data tables
  - Wrangling with hierarchical (nested) data into rectangular formats
- [Problem 4, Summarizing segments of data quickly](learning_r_summarize.md)
  - Vectorized functions and alternatives to loops like `apply()` and `tapply()`
- [Problem 5, Working with text data](learning_r_text_manipulation.md)
  - Specifying patterns for computers (regular expression)
  - Handling dates
- [Problem 6, Scraping and calling APIs](learning_r_scraping_and_api.md)
  - Getting data from the internet programmatically
- [Problem 7, Validating math using simulations](learning_r_validating_prob_simulations.md)
  - Hypothesis testing beyond the t-test: permutation tests
- TODO: add lesson that incorporates scope / debugging

#### What we won't cover
What we won't cover that you should learn in other computing courses:
- Data structure which is much deeper than the data types we've been discussing
- Algorithms, recursion, sorting which will deepen your knowledge of computational complexity
- Structuring code or a data pipeline
- Working backwards from a list of specifications. 
- How to wrangle/analyze big data, i.e. where data is stored across multiple machines beyond just your computer.
- ... many many more

{% include lib/mathjax.html %}

