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
- We've then used the function `sample()` to generate `n` random numbers (each 0 or 1).
  (Not important yet: the `replace=TRUE` statement just means that each random number
  is drawn from `coin` with replacement
  so we can have a sample size that is larger than the total possible numbers.)
  - We will talk more about this function later.
- The key here is to know that vectors are the most basic form of data!

#### Properties of vectors
It's important to know the properties of vectors because these
properties limit how different functions can interact with them.

Before continuing below, first define a variable called `dice <- c(1, 3, 5, 2, 4, 6)`

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
We will use our previous example with `sample()` to elaborate on the elements of a function.
```r
coin <- c(0, 1)
coin_tosses <- sample(coin, 10, replace=TRUE)
coin_tosses
```

`sample()` here is a function that is tossing the coin 10 times, it has a few components that you should be aware of
- **Function name**: `sample`
- **Inputs/arguments**: all inputs are separated by `,` within the `()`. These inputs to the function `sample`
  often have names to help you understand their purpose.
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
- Look at examples: at the bottom of the R documentaiton often has examples.
  Pay attention to what what is entered (vector of what type?), what is outputed. Most functions
  are meant to be simple so a few examples can often help you decipher
  different functions.

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
You should get comfortable "testing" functions to see what will happen vs not.


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

#### Elements of the for-loop
```r
values_to_loop_over <- c(1, 5, 8)
for(i in values_to_loop_over){
    print(i)
}
```

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

First strategy:
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

Second strategy:
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

## Problem 2 - data visualization
The next task we need to learn is how to plot the data. Data visualization
is a powerful technique that often highlights useful patterns in the data.
We will specifically try to plot the different trajectory of
corn production for different states over the years.

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
We show some examples below:
```r
arbitrary_data <- 10:15
names(arbitrary_data) <- c("a", "b", "x", "y", "z")
print(arbitrary_data)

# Subsetting with character vectors
print(arbitrary_data['a'])
print(arbitrary_data[c('b', 'x', 'z')])

# Subsetting with boolean vectors
bool_vec <- c(FALSE, TRUE, TRUE, FALSE, TRUE)
print(arbitrary_data[bool_vec])
```
Things to notice:
- The same "subset" operation could be achieved via different means.
- To subset using character vectors, we had to change the "name"
  for the different elements in the vector.
- To subset using boolean vectors, the boolean vector needs
  to be the same length as the original vector.

#### Quick note on data types
It is important to know data types in programming because
- Many functions behave differently when it interacts with different types of data
- Data types will help you understand many errors. 
  The general philosophy in programming is to trigger errors/warnings early on
  before it's too hard to find the mistake. So operations that are not sensible,
  e.g. `1 + "a"`, will often produce an error to act as an enforcer of writing
  logical code.
- Certain data types are capable of different operations and wrangling
  the data into the most suitable type will increase your efficiency.

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

You can also give names to different elements
```r
num_rolls <- 5
coin_tosses <- sample(c(1, 0), num_rolls, replace=TRUE)
names(coin_tosses) <- paste0('toss', 1:num_rolls)
print(coin_tosses)
print(coin_tosses['toss5'])
```

[Exercises](exercises/r_char_vectors.md)

#### What are boolean vectors?
Boolean values are `TRUE` or `FALSE` values.

These are often created as a result of a logical statements like `1 < 2`

Boolean values can be used to identify outliers, filter data that belongs
to a particular group (e.g. country), or control the flow of code (we'll
explain this later).

When using booleans to subset another vector, only the elements corresponding
to the TRUE values will be kept
```r
nums <- 1:5
nums[c(FALSE, FALSE, TRUE, TRUE, TRUE)]
```

One important feature about boolean values is that they behave like 0 or 1 values
when we perform **arithmetic** with them.
```r
TRUE + FALSE
TRUE * FALSE
FALSE + FALSE
TRUE * 3
sum(c(TRUE, TRUE, FALSE))
```

[Exercises](exercises/r_boolean.md)

#### Vectorized operations with vectors
It is common to operate between a vector and a single value.
For example, checking which numbers are larger than a certain value.
```r
nums <- 1:5
larger_than_3 <- nums > 3
print(larger_than_3)
```
In the code above, `nums` is a vector of length 5. When compared
to `3`, a constant, the comparison was carried out between **each
element** in `nums` and the value `3` as in the following code:
```r
larger_than_3 <- c(1 > 3, 2 > 3, 3 > 3, 4 > 3, 5 > 3)
print(larger_than_3)
```

The distribution of the operation across the vector is a form
of the vectorized operation. This can happen with other operations too:
```r
nums <- 1:5
print(nums - 3)
print(nums * -1)
```

#### Why bother with vectorized operations?
- We can subset specific elements from a vector using the boolean vector created. This is common
  in data cleaning or when you want to analyze a sub-population more closely.
  ```r
  nums <- 1:5
  larger_than_3 <- nums > 3
  print(nums[larger_than_3])
  ```
- We can create transformed data much faster, imagine the task of subtracting the mean from
  a vector of data using a loop vs using vectorized operations:
  ```r
  data <- sample(c(0, 1), 10, replace=TRUE)
  avg <- mean(data)

  # Using vectorized operations (1 line!)
  mean_0_data_vecop <- data - avg

  # Using a for-loop (2-4 lines!)
  mean_0_data_forloop <- c()
  for(i in 1:length(data)){
      mean_0_data_forloop[i] <- data[i] - avg
  }

  print(mean_0_data_vecop)
  print(mean_0_data_forloop)
  ```

[Exercises](exercises/r_vectorized_ops.md)

#### Other Boolean Operators
The most common logical statements are:

Code|Operation|Example
----|---------|-------
`!`|negation of|`!TRUE`
`>`|greater|`vec_demo <- 1:5`<br>`vec_demo > 2`
`==`|equal|`vec_demo <- c("A", "B", "B")`<br>`vec_demo == "A"`
`>=`|greater or equal|`vec_demo <- 1:5`<br>`vec >= 2`
`<=`|less or equal|`vec_demo <- 1:5`<br>`vec <= 2`
`!=`|Not equal|`vec_demo <- c("A", "B", "B")`<br>`vec_demo != "A"`
`&`|and|`vec_demo <- 1:5`<br> `(vec_demo > 2) & (vec_demo >= 2)`
`|`|or|`vec_demo <- 1:5`<br> `(vec_demo > 2) | (vec_demo >= 2)`

For the `&` and `|` operation, it's especially important to understand:
- Order of operations. Notice how we added `()` to ensure that the expressions
  are evaluated into boolean terms between the `&` and `|` operation. Although
  your code would run fine in R, it's best to be explicit in these cases.
- The behavior with with different inputs:
  - For the "and" operation, you'll get TRUE only if all the inputs
    are TRUE, the outcome of `x&y` is:
    `x & y`  | `y=TRUE` | `y=FALSE`
    ---------|----------|----------
    `x=TRUE` |`TRUE`    | `FALSE`
    `x=FALSE`|`FALSE`   | `FALSE`
  - For the "or" operation, you'll get TRUE as long as one input is TRUE,
    the outcome of `x|y` is:
    `x | y`  | `y=TRUE` | `y=FALSE`
    ---------|----------|----------
    `x=TRUE` |`TRUE`    | `TRUE`
    `x=FALSE`|`TRUE`    | `FALSE`

[Exercises](exercises/r_boolean_ops.md)


#### Vectors again!
Recall that vectors are a collection of data with a type and length.
We mentioned that the data within a vector had to all belong to the
same type before. We show that again here
```r
num_demo <- 1
demo_vec <- c(num_demo, 'hello')
class(num_demo) == class(demo_vec[1])
```
- Please examine the class of `demo_vec`
- Why? Intuitively, vectorized operations only make
  sense if we can perform the same operation on each element. Therefore
  restricting each element to be the same in a vector is important for
  us to be able to carry out efficient vectorized operations.

[Exercises](exercises/r_vectors_same_class.md)

#### Special data types - missing values
A very special type of data is the missing data type and data types
that are easily mistaken as missing values.

The missing value data type is `NA` in R. Properties of `NA` include:
- It can be any other data type
  ```r
  na_demo <- NA
  num_vec <- c(na_demo, 1:5)

  print(na_demo + 1)
  print(mean(num_vec))
  ```
- Most operations with NA will propagate the NA downstream
  ```r
  na_demo <- NA
  num_vec <- c(na_demo, 1:5)
  char_vec <- c(na_demo, "hello")
  
  NA values can be any data type
  print(class(na_demo))
  print(class(num_vec[1]))
  print(class(char_vec[1]))
  ```
- To check if a value is `NA`, you need to use the `is.na()` function
  ```r
  na_demo <- NA
  num_vec <- c(na_demo, 1:5)

  # is.na() with NA 
  print(na_demo == NA)
  print(is.na(na_demo))
  
  # is.na() is vectorized!
  print(num_vec == NA)
  print(is.na(num_vec))
  ```

#### What's the point of missing values?
Missing values are **great defaults** because no data can be better than bad data.

For example
- When reporting rain data from weather stations,
  defaulting data to 0 (i.e. no rain) seems sensible at times but then you lose the ability
  to differentiate a confirmed 0 rain event or simply a loss in data.
- When examing surveys with minorities, there can sometimes be missing
  or only one respondent, in either case, "margin or error" calculations
  are not possible and an NA is more appropriate than estimating the data.
- When handling surveys with "non-response", you often want to be notified
  if there are missing values. For example,
  imagine a psychology survey where you have 3 questions asking about
  people's well-being, and some people do not answer your question with
  10% chance. Then you may want to know how many complete surveys you'll have.
  ```r
  sim_num <- 100
  # Let 0 be disagree and 1 be agree to the survey question
  survey_answers <- c(NA, 0, 1)
  sim_avgs <- rep(NA, sim_num)
  for(i in 1:sim_num){
      sim_data <- sample(survey_answers,
                         size=3,
                         replace=TRUE,
                         prob=c(0.1, 0.45, 0.45))
      sim_avgs[i] <- mean(sim_data)
  }
  # Calculate the percentage of cases that are NA
  mean(!is.na(sim_avgs))
  ```

#### Next most common collective data type - Data Frames
Data frames are most often thought of a collection of vectors,
each capable of being a different type.
```r
student_roster <- data.frame(
    student_id = 1:3,
    family_name = c("Doe", "Lee", "Liang"),
    given_name = c("John", "Billy", "Sally"),
    dropped = c(TRUE, FALSE, FALSE),
    stringsAsFactors=FALSE)
print(student_roster)
print(class(student_roster))
print(colnames(student_roster)) # colnames = column names
print(dim(student_roster)) # dim = dimension
print(length(student_roster))
```
Above, we create a data frame named `student_roster` with 4 different
columns, 1 numeric, 2 character, and 1 boolean vector. The argument
`stringsAsFactors=FALSE` was made to ensure character values remained
characters because the default in R is to convert them into factors
a different type of data we will introduce later.

Some things to note:
- Unlike vectors, data frames can hold different types of data which is
  very convenient like Excel Spreadsheets.
- Notice that the `length()` argument corresponds to the number of columns,
  we will learn why this is the case in the future.
- Data frames have 2 dimensions, rows and columns

[Exercises](exercises/r_data_frames.md)

#### Subsetting different columns and rows
Similar to vectors, you can subset data frames using the `[]` 
operator but with some modifications.

As a practice, try walking through the code below, line by line,
to guess what's happening before being told what's happening!
```r
student_roster <- data.frame(
    student_id = 1:3,
    family_name = c("Doe", "Lee", "Liang"),
    given_name = c("John", "Billy", "Sally"),
    dropped = c(TRUE, FALSE, FALSE),
    stringsAsFactors=FALSE)
# To get the 2nd column with integers
student_roster[, 2]
# To get the 2nd row with integers
student_roster[2, ]
# To subset by column with character vectors
student_roster[, c('family_name', 'given_name')]
# To subset using booleans, e.g. those who have NOT dropped the class
dropped_class <- student_roster[, "dropped"]
student_roster[!dropped_class, ]
```
Things to notice:
- Notice that similar rules apply to data frames as vector subsetting
  - you can use different data types to subset, e.g. integers, characters, booleans
  - booleans should share the same length as the number of rows or columns
  - you can subset using a single value or a vector
- To specify subsetting row vs column, you use the `,` within `[]` to differentiate the two cases.

[Exercises](exercises/r_data_frames2.md)

#### Reading data from existing files
The most common way to get a data frame is actually by reading in
an existing file like [fisher_1927_grain.csv](data/fisher_1927_grain.csv) that
contains the data from 1927 harvests with different treatments.

Download the [fisher_1927_grain.csv](data/fisher_1927_grain.csv) file.
The function to read in this data is `read.csv()`
```r
df <- read.csv("~/Downloads/fisher_1927_grain.csv")
```
A few things to know:
- If you get an error, don't worry yet, we'll cover most cases later.
- The code above assigns the data into a variable named `df`.
- The input to `read.csv()` is a character that describes the path and name of the file.
- `csv` stands for "comma separate value" which means each value in the file
  is separated by a comma. If you read the file successfully though, notice
  that you don't see any commas in the data.

#### Common errors when loading data
If you encoutered an issue when you tried to read in the file, here are
some common mistakes that beginners do:

- Typo in function or file name, notice the error produced when the file
  name or function name is misspelled
  ```r
  # Using "_" instead of "." in the function name
  df <- read_csv("fisher_1927_grain.csv")
  
  # Misspelling the name has a different error!
  df <- read.csv("fisher_1927_straw.csv")

  # ODDLY, the filename is NOT case sensitive with R
  df <- read.csv("FISHER_1927_grain.csv")
  ```
- Not knowing "where" the file is stored or R's working directory.
  When you download a file, it is stored in a certain folder on your computer.
  You need to be able to specify how R can find that file from its working folder.
  - If R's working directory is in `"/Users/wayne/Documents/School/Spring2020/UN2102"`
    and the data is under a folder called `"/Users/wayne/Documents/School/Spring2020/data"`
    then in R, you would type out
    - The relative path: `df <- read.csv("../data/fisher_1927_grain.csv")`.
      The relative path is the file's location relative to R's working directory.
      This indicates "go up one folder, then find a folder named data, then find
      a file called fisher_1927_grain.csv"
    - The absolute path: `df <- read.csv("/Users/wayne/Documents/School/Spring2020/data/fisher_1927_grain.csv")`.
      The absolute path is the path from the root of your computer.
  - To know what your current directory is, you can use the following functions:
    - `getwd()`, running this without any arguments will tell you where R's working directory is
      - The working directory is like "the folder" that R is working from
    - `setwd('THE_PATH_YOU_WANT_TO_MOVE_TO')`, running this with the proper string
      will help you move your working directory to the desired "folder"

#### Arguments in read.csv()
You should look at `?read.csv` to see the type of arguments that can change
how the program reads your file. The function relies on the file to be properly
formatted in a certain way to help differentiate different data values,
numbers vs characters, and column headings etc. But if the file is formatted
incorrectly, usually you can change a few settings by changing some arguments.

The most popular arguments are:
- `stringsAsFactors`: should strings be interested as factors? The default is `TRUE` but you
  usually want this to be `FALSE` these days.
- `sep`: the symbol that "separates" the data values, e.g. csv means the values are separated by `","`.
  The common alternative is tab delimited values which would be `"\t"`.
- `na.strings`: all strings that should be interested as missing values, the default is `"NA"`. Popular
  alternatives include `-9999` or `""` (the empty string).
- `header`: should the first line be interested as column names, default is `TRUE`

#### Exploring Larger Data Frames
In general, it's never good practice to "see all the data" as we do in Excel.
With large datasets, I recommend you to use these functions:
- `names(df)` to see the column names
- `head(df)` or `tail(df)` to see the first or last few rows
- `dim(df)` to see the dimension of the data frame
- `class(df[, 1])` to see the class of different columns
These are usually sufficient for you to start plotting for better understanding of the data.

#### Plotting 
Data visualization is a field in itself so we will only cover the basics for histograms and scatter plots.

The first thing about plotting is to realize the number of choices available and how
these choices can affect the interpretation or message of the graph.

We will be working with the file [usda_i_state_corn_yields_cleaned.csv](data/usda_i_state_corn_yields_cleaned.csv)
In the following examples. Download the file and read it in.

#### Legends and axis labels
#### Range of data
#### points()
#### Corn trajectories

#### Saving plots with png()

## Problem 3 - Data Wrangling
#### Joining Data Frames
#### Most flexible data type - list()
#### Subsetting lists
#### do.call()


{% include lib/mathjax.html %}

