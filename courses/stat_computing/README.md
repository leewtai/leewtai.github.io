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
Just like your algebra class where $$y=f(x)$$, R has functions.

Similar to our mathematical notation, the most common method
to refer to functions are used by typing out their "name" followed
by the parentheses `()`, e.g. `log(1)`

The simplest example are functions that manipulate a single number. 
- `log(1)`
- `sin( 90 / 180 * pi)`
- `2^3`

Notice how the third example does not follow the convention for calling functions
yet its similarity to the mathematical notation makes it easy to understand. 

[Exercises](exercises/r_calc_functions.md)

#### Variables in programming
In R, you can assign values to variables so you can refer to them later and increase readability of your code
(very important!).

To do assign a value to a variable name, you can use the `<-` or `=` symbol with the variable name on the left and the value on the right.

- ```r
  demo_num <- 2
  demo_num * 3
  ```
- `demo.char <- "hello"`
- ```r
  demo_num2 = -0.2
  abs(demo_num2)
  ```

This allows you to refer to them later when you have repeated use of the same variable (e.g. think about the sample size **n** in intro statistics that appears in the mean and sample variance calculation).

Later, if you forget what's assigned to the variable, usually you can use the `print()` function or simply type in the variable name at the end of the cell to get the value returned.

```r
print(demo_num)
demo.char
```

[Exercises](exercises/r_variables.md)

#### In R, the most basic element is a vector
In general, a vector is a collection of values where each value has the same data type.

Here are some examples of creating vectors:
- `dice <- c(1, 2, 3, 4, 5, 6)`
- `hello_letters <- c("h", "e", "l", "l", "o")`

To group multiple values into a single vectors, we use the `c()` function. Notice how a vector can contain numbers or characters and the different values are separated by `,`.

This is not the only way to create vectors. The most common alternative is using the `:` symbol that creates a sequence of numbers, incremented by `1`. For example: `1:4`

[Exercises](exercises/r_vectors_basic.md)

#### Why do we care about vectors?
In statistics, we often talk about a sample of data, $$y_1, \dots, y_n$$ where
$$n$$ is the sample size.

In statistical computing, the corresponding equivalent is a numeric vector of length n where the first element in the vector is $$y_1$$, second element is $$y_2$$, etc.

The most basic random variable is the outcome of $$n$$ coin tosses where heads correspond to 1 and tails correspond to 0.

To generate this kind of data:

```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
print(coin_tosses)
```

- We've assigned the value 20 to the variable `n`
- We've created a vector named `coin`, with 2 values, `0` and `1`.
- We've then used the function `sample()` to generate n random numbers (0 or 1)
    - We will talk more about this function later.


#### Biggest misunderstanding of R
Again, the most confusing thing about R is that everything is a vector

```r
num_vec <- 1.96
num_vec1 <- c(1.96)
num_vec == num_vec1
class(num_vec) == class(num_vec1)
```

`num_vec`, from a traditional programming sense, is a single number.

`num_vec1`, from a traditional programming sense, is a vector with single element, the element happens to be a number. 

The metaphor is similar to an individual (`num_vec`) vs talking about a team with only one member `num_vec1`. These are 2 conceptually different things.

However, in R, these are the same thing because the most basic element in R is a vector.

#### Elements of functions (big picture)
We said before that data we've taught in intro stat $$y_1,…,y_n$$ can be thought as vectors in R like coin tosses.

```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
print(coin_tosses)
```

`sample()` here is a function that is tossing the coin n times, it has a few components that you should be aware of
- **Function name**: `sample`
- **Inputs/arguments**: all values separated by `,` within the `()` are inputs to the function `sample`
    - The first 2 values are passed in "by order" where the third value is passed in "by name". The function has a default order of how inputs are entered which is why the first 2 inputs do not need to be given a name explicitly. To know the order or the names, you would **need** to read the documentation for the function by running the code `?sample` in R.
- **How inputs are passed to the function**: this is done via the `()` and the different inputs are separated by `,`.
- The **consequence and/or output** of the function:
    - In the example above, an output is generated and assigned into `coin_tosses`, by examining `coin_tosses`, you'll see that the output is a numeric vector of 0 and 1 values.
    - Some functions do not produce "output" but have a consequence on the environment. For example, deleting a variable, changing your working directory (we will explain this more later), etc. 

[Exercise](exercises/r_function_elements.md)

#### Inputs/arguments to functions
Same example as before

```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
```

If you look into the documentation `?sample`. You should notice the order and names
of the inputs/arguments:

`sample(x, size, replace = FALSE, prob = NULL)`

Here, arguments without an equal sign behind them do not have defaults.


{% include lib/mathjax.html %}

