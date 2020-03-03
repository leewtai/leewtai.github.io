# HW4 - Data Cleaning

CHANGE IN FORMAT:

For ease of grading, we're switching to **html** or **pdf** files from RMarkdown OR Jupyter Notebooks.
You can research this online for how or follow these [instructions](../../setup/math_and_code.md)

#### Q0 Practice with JOINS
When evaluating where to build your future startup headquarters, you may want to know whether JFK is "more connected" than ATL (fictional story, this will not be your top concern). One way to quantify "connectedness" is to see the total number of domestic airports that are reachable within a single vs double flight if we depart from JFK or ATL.

We could achieve this using the `unique_domestic_us_flights_2019.csv` and `unique_international_us_flights_2019.csv` on Canvas (same files as in class). These files contain all the domestic and international flights where the origin or destination is a US airport. We are going to restrict ourselves to use IATA airport codes for this assignment (e.g. JFK, SFO, etc).

Please show the code for the following:
- Read in the domestic and international file using `read.csv()` and make sure to use the argument `stringsAsFactors=FALSE`
- Please subset the data so you only have the columns "ORIGIN" and "DEST"
- Assign a variable called `origin_airport` that has the value `"JFK"`
- For the domestic and international data, please filter out only the data departing from your `origin_airport`
- Please report how many unique domestic airports are reachable within a single flight if you depart from `origin_airport`?
- From your filtered data, please print out the data that have destination in IST, then remove the duplicate record
    Hint: understand the following example to help you "remove" duplicate records (there are multiple-ways to do this):
    ```r
    demo_df <- data.frame(a=c(1, 1, 3), b=c(2, 2, 2))
    dup_records <- duplicated(demo_df)
    print(dup_records)
    demo_df[dup_records,]
    print(unique(demo_df))
    print(demo_df[!dup_records,])
    ```
- Please use `rbind()` to create a single data frame with both domestic and international flights starting from your `origin_airport`
- Please use `merge()` along with another data frame (you need to figure what this data frame is) to infer the number of unique domestic airports that are reachable within 2 flights. 
    - Clarification: going international, then returning to a domestic airport is one way to reach a domestic airport via 2 flights.
    - Hint: you may want to use `unique()` to filter out only the unique airports.
        ```r
        demo_char <- c("hello", "hello", "hello", "this", "is", "a", "telemarketing", "call")
        unique(demo_char)
        ```
    - Warning: Notice that if an airport is reachable by a single flight, it is reachable within 2 flights. Make sure your code reflects this piece of logic.
    - Reminder hint: `c()` combines vectors into vectors
- Please clean up the code above (but do not overwrite the code above) into a single function that takes in the inputs `origin_airport` that should be a character like "JFK" and a single data frame that has both the international and domestic flights. The function should output a `list` with the following structure:
    ```r
    list(
        origin_airport=????
        single_flight=list(count=????, uniq_airports=????),
        double_flight=list(count=????, uniq_airports=????)
    )
    ```
    Clarification: `count` should be an integer, `uniq_airports` should be a character vector with length equally to `count`, `origin_airport` should be the `origin_airport` passed to the function originally. 
- Please use your function to answer the number of unique domestic airports reachable within one or two flights if we start from "MSO" vs "ATL"

Side comment: please take a moment and see how much you could figure out if I simply asked you to "write a function that can answer: how many unique domestic airports are reachable within 2 flights starting from JFK vs ATL?". This is not easy but where we want to be!


#### Q1 Exploring data from Twitter
Tech companies often have ways for people to interact with their data to speed up innovation
and discourage unwanted activities. [Twitter](https://twitter.com/home) is one such company where researchers like to
use to analyze "popular sentiment". Twitter users can share their thoughts/findings via short messages, known as tweets, that can be viewed by the public and people who subscribe to their twitter feed (a.k.a. followers).

In `twitter_standard_api_results.json`, you'll find data collected from using the [Twitter Standard Search API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets).
This contains tweets and additional information related to the tweets known as metadata.

This problem is meant to give you practice on exploring hierarchical data types. Use the following code
to read in the data then answer the following questions.

```r
library(jsonlite)
twitter_output <- read_json("data/twitter_standard_api_results.json")
```
- What is the data type of `twitter_output` in R?
- What are all of the tags/names associated with `twitter_output`? (one line code)
- To use the Standard Search API, you have to enter a search query, what query did we use to collect this data? Please read the tags/names throughout `twitter_output` to find this out. (can be one line code)
- Navigate through the `twitter_output` object, what tag/namne is associated with the actual tweet (no code)
  - hint1: the 10th tweet starts with "White House requesting"
  - hint2: you could also look at the [Example Response](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets) in the documentation.
- How many different tweets are in this file? (Try navigating `twitter_output`, there are multiple ways of inferring this, can be a one line code)


#### Q2 Data wrangling
Subsetting and summarizing data is much easier on rectangular data types like data frames so data wrangling often involves getting hierarchical data into a rectangular format that is Excel friendly.

Use the same data from Q1, please use 2 methods to create a data frame where the rows correspond to the different
tweets and the columns correspond (in order) to different features: the tweet, the `retweet_count`, the `retweeted` flag (TRUE/FALSE), 
the user's `screen_name`, the user's `friends_count`, the user's `followers_count`, and the user's `location` (notice
how Twitter handles this when the information is not available!). 

The 2 methods should produce the same data frame but one should use a for-loop where the other should utitlize a combination of `lapply()` and `do.call()`.

Requirements for both methods:
- The column names of the data frame should correpsond to the tag/name from the `twitter_output` object for consistency (the "tweet" will not be titled tweet but should correspond to your answer in Q1)
- Please make sure `screen_name` and `location` are characters and not factors, the others should all be numeric values or logic (boolean) values.
- (restriction on the for-loop) Please make sure you only have a single loop, i.e. you cannot have a different loop for the different variables.

What you need to show for this problem:
- The code for both methods to construct the data frames
- The code that shows that all the column names and data types agree between your two data frames (hint: `all()`)
- The code that checks the dimensions are the same between the two data frames
- The output from the 2 checks above.

Hints:
- "Working backwards" might be helpful here.
- For `lapply()` it might be easier to write a function called `q2_extraction` that extracts the desired information given data at the appropriate level in `twitter_output`. This function should output a data frame with only one row of information if you take this strategy.
- Use `?data.frame` to see which argument can control the behavior of turning characters into factors
- For the for-loop, there are many approaches, but the easiest start might be to define a data frame ahead of the loop:
    ```r
    var_names <- c("Q1_TWEET_NAME", "retweet_count",
                   "retweeted", "screen_name",
                   "friends_count", "followers_count",
                   "location")
    outcome <- as.data.frame(matrix(NA, ncol=length(var_names), nrow=1))
    names(outcome) <- var_names
    for(i in seq_along(?????????)){
        ???????????
        outcome[i, "retweet_count"] <- ???????
        outcome[i, "screen_name"] <- ???????
    }
    ```

#### Q3 Why we bother with data wrangling
Please use one of the data frames from Q2
- Between `followers_count` and `friends_count`, which variable has a higher correlation with `retweet_count`?
- Please plot the scatter plot between `retweer_count` and your answer from above (`retweet_count` should be on the y-axis). Please make sure the axis labels are correct and do not mention the data frame itself. Please have the correlation number (rounded to 2 decimals) displayed in the plot title (hint: `paste("Correlation: ", round(cor(?, ?)))`). This plot will NOT be pretty!
- You should notice 4 large values in the x-axis. Please recreate the plot above if we removed these 4 large values. Hints:
    - Notice that manipulating the `xlim` attribute will not update the correlation value so this is not sufficient.
    - You can use the fact that these 4 values are beyond 1 SD from the mean.
- Anomalies can be interesting case studies, please report the content of the tweet and the screen_name of the tweet with the highest `retweet_count` (hint: `which.max()`)

Side comment: notice how much easier/cleaner the plotting/subsetting is with the data frame rather than writing for-loops over the dataset multiple times

{% include lib/mathjax.html %}

