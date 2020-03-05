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
data collection, graphics, and reproducability.

To gain a better understanding of programming, we will cover the main
concepts behind statistical computing that
- focuses on data wrangling and simulations
- less on data structures and algorithmic efficiency

For example, we will introduce random numeric vectors relatively early on to reinforce
concepts like the law of large numbers but we will not differentiate between
integers, longs, vs doubles.

#### My assumptions
My assumption is that you have been exposed to
- basic statistical concepts like the average, sample standard deviation (vs population variance),
  and histograms.
- calculators and Excel (Google Spreadsheets)

#### Setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../setup/conda_and_navigator_setup.md)
so you could use R or Python for this in the future.

In the current version, I'll focus on **R programming** for now.

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
  print(demo_num * 3)
  print(demo_num - 4)
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

#### Overwriting variables
What if I want to update a variable? You simply assign a new value to it.

I recommend running these 3 chunks separately but in order:
```
my_name <- 'Wayne Lee'
print(my_name)

my_name <- 'Wayne Tai Lee'
print(my_name)

my_name <- 0
print(my_name)
```

A few things to note:
- The **last** assignment will dictate the value in `my_name` (try playing with the order and find out)
- We were able to assign numbers to something that was a character string before
- One of the biggest source of error in beginner coders is that you forget what order your code was ran in
  and you recycle the same variable name which causes issues in the code later.
- Good naming is considered one of the hardest tasks in programming :)


#### What is a function?
A function in programming is similar to a function in mathematics.
Given inputs, it performs operations and (usually) returns an output.

We've introduced calculator-like functions before like `log()` and `sin()`
but functions can be more complex:
- The inputs can be more complex than a single number
- They can take in multiple inputs
- Functions can have defaults
- Outputs can be more complex than a single number as well

#### Creating data with functions
Besides the usual calculator-like functions, the most basic functions
are those that create a collection of values, this is how we will
represent "data" in programming. 

For example, to make a dice with the 6 sides or a coin with the 2 sides,
we can use the `c()` function to combine the different values into
one variable. This type of data is called a **vector**.
```r
dice <- c(1, 2, 3, 4, 5, 6)
coin <- c("Head", "Tail")
print(dice)
print(coin)
```

A few things to note:
- The inputs can be numbers or characters
- The inputs are separated by `,`
- There are multiple inputs
- `c` is the function name
- Functions that create data tend to be able to take in arbitrary number of inputs

This is not the only way to create vectors. A common alternative is to use the `:` symbol that creates a sequence of numbers, incremented by `1`. For example: `1:4`

[Exercises](exercises/r_vectors_basic.md)

#### Why do we care about vectors in statistical computing?
In statistics, we often talk about a sample of data, $$y_1, \dots, y_n$$ where
$$n$$ is the sample size.

In statistical computing, the corresponding equivalent is a numeric vector of length n where the first element in the vector is $$y_1$$, second element is $$y_2$$, etc.

The most basic random variable is the outcome of $$n$$ coin tosses where heads correspond to 1 and tails correspond to 0.

To generate this kind of data, you could use the following commands:
```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
print(coin_tosses)
```

In the code above:
- We've assigned the value 20 to the variable `n`
- We've created a vector named `coin`, with 2 values, `0` and `1`.
- We've then used the function `sample()` to generate n random numbers (0 or 1)
    - We will talk more about this function later.

#### Properties of vectors
It's important to know the properties of vectors because different types of data
will have different properties and therefore limit how functions can interact with them.

Before continuing below, first define a variable called `dice <- c(1, 2, 3, 4, 5, 6)`
- The number of elements within a vector is called its **length**
    - `length(dice)`
- The type of the elements within a vector is the vector's **type** (implication is that elements within a vector must all share the same type).
    - `class(dice)`
- You can subset different elements within the vector using `[]` (we will cover the idea of subsetting later)
    - `dice[3]` grabs the 3rd element within the vector `dice`
    - `dice[c(2, 3)]` grabs the 2nd and 3rd element within the vector, `dice`
- You can change elements within a vector
    - ```r
      dice[1] <- 6
      print(dice)
      ```
[Exercises](exercises/r_vector_properties.md)

#### Biggest confusion in R
The most confusing thing about R is that most data are vectors, including a single number a vector of length 1.
```r
num_vec <- 1.96
num_vec1 <- c(1.96)
num_vec == num_vec1
class(num_vec) == class(num_vec1)
print(num_vec[1])
```

If you come from a programming background, `num_vec` is a single number where `num_vec1`, should be a vector with single element, the element happens to be a number. 

The metaphor is similar to an individual (`num_vec`) vs talking about a team with only one member `num_vec1`. These are 2 conceptually different things. However, **in R**, these are the same thing because the most basic element in R is a vector.

#### Functions on vectors
A popular operation we perform on data is to take the average.
To do this in R, we can use the `mean()` function

```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
mean(coin_tosses)
```

A few things to note:
- Given each value is a 0 or 1, the averaeg is also the fraction of 1's
in the vector.
- `coin_tosses` is a collection of values that are all passed as **one input** into the function `mean()`. This is different from how `c()` took in multiple inputs that were separated by `,`.

#### Elements of functions (big picture)
```r
coin <- c(0, 1)
coin_tosses <- sample(coin, 10, replace=TRUE)
coin_tosses
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

Same example as before:

```r
n <- 20
coin <- c(0, 1)
coin_tosses <- sample(coin, n, replace=TRUE)
```

If you want to look into the documentation, run the code `?sample`.
You should notice the order and names of the inputs/arguments:

`sample(x, size, replace = FALSE, prob = NULL)`
- Since multiple inputs exist, you can pass inputs into a function by name or by order. 
    If we want to change the order of inputs for the code above, we can simply pass the
    inputs in by name
    ```r
    coin_tosses <- sample(size=n, x=coin, replace=TRUE)
    ```
- Inputs with an `=` within the documentation often mean they have **default values**.
    In other words, if we do not specify those inputs, the defaults will be used.
    ```r
    dice <- 1:6
    # Notice that replace=FALSE guaratees no repeats!
    sample(dice, size=4)
    ```

#### More detailed explanations on sample()
Again from the documentation:
`sample(x, size, replace = FALSE, prob = NULL)`

- `x`: here is either a single number OR a vector with length greater than 1 (notice
    this vector can contain numbers or other values), the function will behave
    differently in these 2 cases.
- `size`: this is the sample size which will determine the length of the
    output (i.e. `coin_tosses` will be length `n` in this example)
- `replace`: this can only take on 2 possible values: `TRUE` or `FALSE`.
    If `TRUE`, the sampling from the vector `x` will be done **with replacement**
    where `FALSE` means the sampling is done **without placement**. The implication
    is that if `replace=FALSE` then `size` cannot be larger than the length of `x`
- `prob`: prob is vector that indicates the probability for each element
    in `x` (in order) to be picked. If `prob` is not specified, each element within
    `x` will have the same probability of being picked.

In general, only very popular functions will have good documentation and explanations.
You should get comfortable "testing" funcrtions out to see what will happen vs not.

{% include lib/mathjax.html %}

