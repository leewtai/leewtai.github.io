# Statistical Computing for non-programmers

Draft [syllabus](syllabus.md) for the class

#### What is statistical computing?
If you are reading this, I probably do not need to convince you about the
importance of statistics, data, and coding. However, I believe
that statistics is best learned by constantly translating problems
between abstract concepts, mathematical formalism, and programming.
An example is like "health of a nation" is a concept, infant mortality
per 1000 births is one way to formalize a measure for a nation's health,
where automating this report would require us to think about practical
data collection, transfer, and an audience.

To gain a better understanding of programming, we will cover the main
concepts behind statistical computing that focuses on data wrangling and
simulations while focusing less on data structures and algorithmic efficiency.
For example, we will introduce the idea like random numeric vectors to reinforce
ideas like the law of large numbers but we will not differentiate between
integers, longs, vs doubles.

#### My assumptions
My assumption is that you have been exposed to
- basic statistical concepts like the average, sample standard deviation,
  and histograms.
- calculators

#### Setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../setup/conda_and_navigator_setup.md)
so you could use R or Python for this in the future.

In the current version, I'll focus on R programming for now.

#### Using programming as a calculator
I'm assuming you've used a calculator before. Try out a few of the following
calculations in the Jupyter Notebook. To run the code, highlight the cell,
then hit "Shift+Enter" or there's a "Run |>" button in the tab area as well.
- `1`
- `2*3`
- `3 +4`
- `3 + 4 * -1`
- `(3 + 4) * -1`
- `3 + 4 * -    1`
- `log(1)`

[Exercises](exercises/r_calculators.md)

#### Intentinoally making mistakes
Please make mistakes early on!

I highly encourage you to make mistakes. The more you do so, and learn,
the better at coding you will become. In general, when you are intentionally
trying to break the code, it is important that you
- read the code
- anticipate the error/warning (or lack of error/warning)
- run the code
- read the error message or lack of error message
- make sense of the error message

For example:
If I were to run the following code:

```r
1  1
```

- read the code
    - I see two `1`s are separated by a few white spaces
- anticipate the error/warning (or lack of error/warning)
    - I expect R to not return a warning and just print out two 1's separated by the same number of white spaces
- run the code
    - copy/paste the `1  1` into the Notebook and run it
- read the error message
    - `Error: unexpected numeric constant in "1  1"`
- make sense of the error message
    - This is not obvious! Ask the instructor/TA for an explanation.
    - Instructor's attempt at explaining:
        When R is interpreting that command, the error is referring to the second 1  being unexpected. After typing in the first 1 followed by spaces, R is anticipating you to operate with it like + , *, /, etc. However, it encounters the second 1 instead of what it was anticipating. R decided it could not interpret the intent of the command so it throws an error and does not run the command. You can verify by running `1  "a"` and see how the error message changes.

[Exercises](exercises/r_make_mistakes.md)

#### Calculator-like functions
Just like your algebra class where $y=f(x)$, R has functions.

Similar to our mathematical notation, the most common method
to refer to functions are used by typing out their "name" followed
by the parentheses `()`, e.g. `log(1)`
