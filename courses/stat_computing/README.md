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

## Problem 1, How to simulate Law of Large Numbers?
We will use the law of large numbers to motivate the following content
in statistical computing.

The law of large numbers says that sample averages based on a larger
sample size will have a smaller standard error than a sample average
based on a smaller sample size. Standard error here means the expected
error of the sample average as an estimate for the population average.

To accomlish this, you'll need to be able to
- Create a collection of random data from a population
- Assign the data to variables
- Apply the average function over the data
- Simulate the sample average multiple times
- Collect the outcome from each simulation

The following steps should lead you to that final step.

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
Given inputs, it performs some operations and (usually) returns an output.

We've introduced calculator-like functions before like `log()` and `sin()`
but functions can be more complex:
- The inputs can be more complex than a single number (e.g. a matrix!)
- They can take in multiple inputs
- Functions can have defaults, i.e. if you do not specify a significance level,
  we often default to 5%.
- Outputs can be more complex than a single number as well

#### Creating data with functions
Besides the usual calculator-like functions, the most basic functions
are those that create a **collection of values**, this is how we will
represent "data" in programming. 

For example, to make a dice with the 6 sides or a coin with the 2 sides,
we can use the `c()` function to combine the different values into
one variable. This type of data is called a **vector**.
```r
dice <- c(1, 2, 3, 4, 5, 6)
coin <- c("Head", "Tail")
empty_vec <- c()
print(dice)
print(coin)
print(empty_vec)
```

A few things to note:
- The inputs can be numbers or characters
- The inputs are separated by `,`
- There are multiple inputs
- `c` is the function name
- Functions that create data tend to be able to take in arbitrary number of inputs

This is not the only way to create vectors. There are two other common alternatives:
- Creating a sequence of numbers, incremented by `1` using the `:` example
  ```r
  1:4
  ```
- Creating a vector by repeating another vector.
  ```r
  rep(1, 5)
  ```

[Exercises](exercises/r_vectors_basic.md)

#### Why do we care about vectors in statistical computing?
In statistics, we often talk about a sample of data, $$y_1, \dots, y_n$$ where
$$n$$ is the sample size.

In statistical computing, the corresponding equivalent is a numeric vector
of length n where the first element in the vector is $$y_1$$, second element is $$y_2$$, etc.

The most basic random variable is the outcome of $$n$$ coin tosses where
heads correspond to 1 and tails correspond to 0.

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
- We've then used the function `sample()` to generate `n` random numbers (each 0 or 1)
  - We will talk more about this function later.
- The key here is to know that vectors are the most basic form of data!

#### Properties of vectors
It's important to know the properties of vectors because these
properties limit how different functions can interact with them.

Before continuing below, first define a variable called `dice <- c(1, 2, 3, 4, 5, 6)`

- The number of elements within a vector is called its **length**
  - Try running the code: `length(dice)`
- The type of the elements within a vector is the vector's **type** (implication
  of this statement is that elements within a vector must all share the same type).
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
The most confusing thing about R is that a single value (e.g. a single number) is a vector of length 1.
```r
num_vec <- 1.96
num_vec1 <- c(1.96)
num_vec == num_vec1
class(num_vec) == class(num_vec1)
print(num_vec[1])
print(num_vec1[1])
```

If you come from a classic programming background, `num_vec` is a single number (scalar),
where `num_vec1` should be a vector with single element, the element being a scalar. 

The analogy is similar to an individual (`num_vec`) vs a team with only one member (`num_vec1`).
These are 2 conceptually different things.

However, **in R**, given its focus on data, the most basic element is a vector
which can cause some unintuitive behaviors sometimes.


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
- Given each value is a 0 or 1, the average is also the fraction of 1's
  in the vector.
- `coin_tosses` is a collection of values that are all passed as **one input**
  into the function `mean()`. This is different from how `c()` took in multiple
  inputs that were separated by `,`.

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

#### How to read documentation in R
Documentation is often not well written but here are a few tips:
- Pay attention to the variable names. Most functions are written
  so the meaning of the variables can help you understand the function.
- Look at examples: what is entered, what is outputed. Most functions
  are meant to be simple so a few examples can often help you decipher
  different functions. R commonly has examples at the bttom of its documentation.

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

#### Avoiding repetitive tasks: for-loops
In statistics, we often talk about probability as something happening over repeated trials.
To emulate that, we can use **for-loops**.

First, run a simple for-loop example in R:
```r
values_to_loop_over <- c(1, 5, 8)
for(i in values_to_loop_over){
    print(i)
}
```

At this level, it's fine to think about the for-loop above as condensing this code:
```r
values_to_loop_over <- c(1, 5, 8)
i <- values_to_loop_over[1]
print(i)
i <- values_to_loop_over[2]
print(i)
i <- values_to_loop_over[3]
print(i)
```
Notice how the repeated code is `print(i)`. This repeated piece will often
become the body of the for-loop. On the otherhand, `i` is simply taking on
the next value within `values_to_loop_over` for each loop/iteration. This
slight change is controlled by whatever you provide in `values_to_loop_over`.

[Exercise](exercises/r_forloop1.md)

#### Elements to the for-loop
```r
values_to_loop_over <- c(1, 5, 8)
for(i in values_to_loop_over){
    print(i)
}

The above loop has a few elements to consider:
- First, the "body" of the loop are enclosed in `{}`
- The `i` will be a the varaible that changes from loop to loop
- The `values_to_loop_over` will control which values
  `i` can take from loop to loop.
- `for(? in ?){???}` is the basic structure that clarifies
  the different roles within the code.


#### Common for-loops mistake - overwriting your variables
For example, if we wanted to simulate 3 coin tosses but
you were restricted to only using `sample(c(0, 1), 1)`, i.e.
your function could only toss one coin at a time.

A natural instinct is to write a loop like the following:
```r
arbitrary_vec <- 1:3
for(i in arbitrary_vec){
    coin_toss <- sample(c(0, 1), 1)
}
```

The issue with this loop is that `coin_toss` is over-written from
loop to loop because you can re-imagine the code as:
```r
arbitrary_vec <- 1:3
i <- arbitrary_vec[1]
coin_toss <- sample(c(0, 1), 1)
i <- arbitrary_vec[2]
coin_toss <- sample(c(0, 1), 1)
i <- arbitrary_vec[3]
coin_toss <- sample(c(0, 1), 1)
```
- Notice that `coin_toss` will only take on the final result for
  `sample(c(0, 1), 1)` and the 2 previous coin_toss values are
  essentially discarded.
- Notice also that `i` in this case does not serve any purpose
  but is simply a side effect from the for-loop.

#### Collecting outputs over each loop
The issue above was that any variable **defined within the
loop** will get overwritten in each loop.

There are 2 strategies to overcome this issue (recall our goal is to
create 3 coin tosses using a for-loop).
- When overwriting a variable, the variable will do so by including
  the output from the loop AND the variable itself.
- Update a variable that was defined outside the loop.

Below are examples for the 2 strategies using the same example before.
At the end of the loop, notice how a variable `coin_tosses` will be
created that will contain the results from the coin_tosses across
each loop.

Here's an example for the first strategy:
```r
arbitrary_vec <- 1:3
coin_tosses <- c()
for(i in arbitrary_vec){
    coin_toss <- sample(c(0, 1), 1)
    coin_tosses <- c(coin_tosses, coin_toss)
}
```
- Notice in this case, we are leveraging `c()` to combine
  the results from previous `coin_tosses` (notice plural!)
  with the newest `coin_toss`
- Notice how `coin_tosses` is being overwritten in each loop
- Notice that we needed to define `coin_tosses` before the loop
- Notice how `i` still serves no purpose here!

Here's an example for the second strategy:
```r
sequential_integers <- 1:3
coin_tosses <- c()
for(i in sequential_integers){
    coin_toss <- sample(c(0, 1), 1)
    coin_tosses[i] <- coin_toss
}
```
- Notice in this case, we are leveraging the "subset" operation
  to update `coin_tosses` in each loop. 
- Notice we needed to define `coin_tosses` before the loop!
- Notice that, in R, you can subset for an index that is longer than the length of the vector. 
  This is observable from the fact that `coin_tosses` start with length 0 then we update
  the first element by **assigning** the output from `coin_toss` to the empty vector. Subsequence
  updates are also subsetting indices longer than the vector to extend the vector.
- To do this, we had to make sure that `i` is no longer looping
  over arbitrary values but should be sequential integers to
  update different values within `coin_tosses`
- Notice how `i` now serves a purpose!

[Exercises](exercises/r_forloop2.md)

#### Special note on `c()`
Above, we used the fact that given two vectors, `c()` will
combine the inputs into a single vector. 

This is logically consistent with how `c(1, 2, 6)` behaves
because each number is also considered a vector of length 1.

Given this, you need to think about `c()` as a function that
combines multiple vectors into a single vector.

#### First Statistical Simulation!
We've learned:
- How to create vectors that represents data, e.g. `sample()`
- How to write a for-loop
- How to apply functions on vectors, e.g. `mean()`

Now we can run simulations for the Law of Large Numbers!

The Law of Large Numbers says that sample averages with larger sample
sizes will be "closer" to the population average. Instead of the standard
error, however, we will use the mean absolute error for simplicity.

To demonstrate this, we will use the following template. I encourage you to
- Read the comments, code, variable names to get an overall understanding of the code
- Update `sample_size` to 100 see the impact on the final result, this should align with
  your understanding of the law of large numbers.
- THEN go back and make sure you understand each line
  - What operation is being done:
    - assigning a new variable?
    - subsetting?
    - applying a function to a vector?
    - is the output a vector of length 1 (single number) or more?

```r
# Creating the unknown population mean
fair_coin <- c(0, 1)
biased_coin <- sample(fair_coin, 7, replace=TRUE)
population_avg <- mean(biased_coin)

# We will change the sample size to see the impact on the final result
sample_size <- 10

# The loop contains the repeated process of calculating different samples,
# calculating their corresponding sample averages, then calculating the
# the absolute error from the true population average.
abs_errors <- c()
num_simulation <- 1000
for(i in 1:num_simulation){
    sim_sample <- sample(biased_coin, sample_size, replace=TRUE)
    sample_avg <- mean(sim_sample)
    abs_error <- abs(sample_avg - population_avg)
    abs_errors[i] <- abs_error
}

# Finall, to evaluate "closeness" we will simply take the average
# across all absolute errors, a smaller value here would indicate
# "closer"
mean(abs_errors)
```

Comment on the code: the code above is intentionally written in a very
verbose fashion. 

[Exercise](exercises/r_law_large_num.md)

#### Best practices on writing for-loops for beginners
In general, when you are about to write a for-loop, the **last thing**
you want to write is the `for(){}` statement. 

Given the law of large number example, the first things that should be
written is the final result, the mean absolute error.
```r
mean_abs_error <- mean(abs_errors)
```

This line won't run because `abs_errors` is not defined yet. `abs_errors`,
however, is a collection of different values of `abs_error`, otherwise
the average operation wouldn't make sense.
```r
abs_errors <- c()
i <- 1

abs_errors[i] <- abs_error
mean_abs_error <- mean(abs_errors)
```

Following the same logic, `abs_error` has not been defined yet.
```r
abs_errors <- c()
i <- 1

abs_error <- abs(sample_avg - population_avg)
abs_errors[i] <- abs_error
mean_abs_error <- mean(abs_errors)
```

Now `sample_avg` and `population_avg` are not defined.
But both of these require us to define a population. This would
normally be provided to you or defined by the problem context:
```r
fair_coin <- c(0, 1)
biased_coin <- sample(fair_coin, 7, replace=TRUE)
population_avg <- mean(biased_coin)

sample_size <- 10

abs_errors <- c()
i <- 1

sample_data <- sample(biased_coin, sample_size, replace=TRUE)
sample_avg <- mean(sample_data)
abs_error <- abs(sample_avg - population_avg)
abs_errors[i] <- abs_error
mean_abs_error <- mean(abs_errors)
```

Now we need to repeat the calculation with a for-loop.
This requires us to replace the `i=1` since that will
be defined by the for-loop instead.
```r
fair_coin <- c(0, 1)
biased_coin <- sample(fair_coin, 7, replace=TRUE)
population_avg <- mean(biased_coin)

sample_size <- 10

abs_errors <- c()
for(i in 1:1000){
    sample_data <- sample(biased_coin, sample_size, replace=TRUE)
    sample_avg <- mean(sample_data)
    abs_error <- abs(sample_avg - population_avg)
    abs_errors[i] <- abs_error
}
mean_abs_error <- mean(abs_errors)
```

By fixing the naming afterwards, the code is finished!

#### Problem 2 - data visualization
The next task we need to learn is how to plot the data.
Specifically, plotting the different trajectory of
corn production for different states.

To do this, we will need to learn about
- Boolean vectors
- Character vectors
- Vectorized operations
- Subsetting
- Data frames
- Plotting functions

#### Subsetting
Before, we taught about subsetting vectors using numerical vectors, e.g.
```r
arbitrary_data <- 10:15
print(arbitrary_data[2])
print(arbitrary_data[2:4])
```

But turns out you can subset using boolean vectors and character vectors.
```r
arbitrary_data <- 10:15
names(arbitrary_data) <- c("a", "b", "x", "y", "z")
print(arbitrary_data)
print(arbitrary_data['a'])
print(arbitrary_data[c('b', 'x', 'z')])

bool_vec <- c(TRUE, TRUE, FALSE, FALSE, FALSE)
print(arbitrary_data[bool_vec])
```
Things to notice:
- To subset using character vectors, we had to change the "name"
  for the different elements in the vector.
- To subset using boolean vectors, the boolean vector needs
  to be the same length as the original vector.

#### What are character vectors?
Character vectors are composed of character strings like `"a"`,
`"hello"`, `c("statistical", "computing")`, etc

Characters values can be used to change axis labels, create file
names dynamically, or find keywords in job descriptions.

A common function we'll use with characters is `paste0()` that
combines different characters together.
```r
alphas <- c('a', 'b', 'c')
paste0('file_', alphas, '.csv')
```

[Exercises](exercises/r_char_vectors.md)

#### What are boolean vectors?
Boolean values are `TRUE` or `FALSE` values.

These are often created as a result of a conditional statement like `1 < 2`


{% include lib/mathjax.html %}

