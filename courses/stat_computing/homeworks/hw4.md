# HW4 - Data Cleaning

Please make sure your R is at least version 4 or higher. If you have an older version of R, just know that
you may encounter factors when you construct data frames when others will not. This won't impact your code
significantly.

#### Q0 Practice with JOINS
When evaluating where to live after college, you may want to know whether JFK is "more connected" than ATL. One way to quantify "connectedness" is to see the total number of domestic airports that are reachable with a direct or connected flight.

We could achieve this using the `unique_domestic_us_flights_2019.csv` on CourseWorks. These files contain all the domestic flights where the origin and destination are US airports in 2019. We are going to restrict ourselves to use IATA airport codes for this assignment (e.g. JFK, SFO, etc).

Please show the code for the following:
- Read in the domestic file using `read.csv()`, please confirm the airport codes have class `character`.
- Please subset the data so you only have the columns `"ORIGIN"` and `"DEST"`
- Please use `unique()` to confirm that there are no duplicate flights, e.g. two records from the same `ORIGIN` to the same `DEST` would be considered a duplicate but a flight from SFO to JFK is a different flight from JFK to SFO. Hint: what does `unique()` behave with a data frame?
- Assign a variable called `init_airport` with the value `"JFK"`
- Please subset only the flights departing from your `init_airport`
- Please report how many unique domestic airports are reachable within a single flight if you depart from `init_airport`?
- Please use `merge()` to infer the number of unique domestic airports that are reachable within 2 flights (i.e. a direct or connected flight) from `init_airport`.
- Please clean up the code above (but do not overwrite the code above) into a single function that takes in the inputs `init_airport` that should be a character like "JFK" and a single data frame has the domestic flights. The function should output a `list` with the following structure:
    ```r
    list(
        init_airport=????
        single_flight=list(count=????, uniq_airports=????),
        double_flight=list(count=????, uniq_airports=????)
    )
    ```
    Clarification: `count` should be an integer, `uniq_airports` should be a character vector with length equally to `count`, `origin_airport` should be the `init_airport` passed to the function originally. 
- Please use your function to answer the number of unique domestic airports reachable within one or two flights if we start from "MSO" vs "ATL"


#### Q1 Exploring data from Twitter
Tech companies often have ways for people to interact with their data to speed up innovation
and discourage unwanted activities. [Twitter](https://twitter.com/home) is one such company where researchers like to
use to analyze "popular sentiment". Twitter users can share their thoughts/findings via short messages, known as tweets, that can be viewed by the public and people who subscribe to their twitter feed (a.k.a. followers).

In `hw4_twitter.json`, you'll find data collected using the [recent search API from Twitter](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction).
This contains tweets and additional information known as metadata.

This problem is meant to give you practice on exploring hierarchical data types. Use the following code
to read in the data then answer the following questions.

```r
library(jsonlite)
twitter_output <- read_json("hw4_twitter.json")
```
- What is the data type of `twitter_output` in R?
- Navigate through the `twitter_output` object, what tag/namne is associated with the actual content of the tweets.
- How many different tweets are in this file? (Try navigating `twitter_output`, there are multiple ways of inferring this, can be a one line code)
- What range of dates are covered within this dataset? Your code should not assume that the data is in temporal order.


#### Q2 Data wrangling
Subsetting and summarizing data is much easier on rectangular data types like data frames so data wrangling often involves getting hierarchical data **into** a rectangular format that is Excel friendly.

Use the same data from Q1, please use 2 methods to create a data frame where the rows correspond to the different
tweets and the columns correspond (in order) to different features:
- the `retweet_count`
- the `like_count`, 
- the date of the tweet (please discard finer details about the time if it exists)
- the author's id
- A feature called `used_hashtag` that contains a TRUE/FALSE value depending if Twitter has determined that a hashtag was used in the tweet. Hint: look for the name/tag `hashtags` in the second tweet.

The 2 methods should produce the same data frame but one should use a for-loop where the other should utitlize a combination of `lapply()` and `do.call()`.

What you need to show for this problem:
- The code for both methods to construct the data frames
- The code that shows that all the column names and data types agree between your two data frames (hint: `all()`)
- The code that checks the dimensions are the same between the two data frames
- The output from the 2 checks above.

Hints:
- "Working backwards" might be helpful here.
- For `lapply()` it might be easier to write a function called `q2_extraction` that extracts the desired information given data at the appropriate level in `twitter_output`. This function should output a data frame with only one row of data if you take this strategy.
- For the for-loop, there are many approaches, but the easiest start might be to define a data frame ahead of the loop, hint:
    ```r
    var_names <- c("retweet_count", "like_count", "date")
    outcome <- as.data.frame(matrix(NA, ncol=length(var_names), nrow=?????))
    names(outcome) <- var_names
    for(i in seq_along(?????????)){
        ???????????
        outcome[i, "retweet_count"] <- ???????
        outcome[i, "date"] <- ???????
    }
    ```

#### Q3 Why we bother with data wrangling
Please use one of the data frames from Q2
Please plot the scatter plot of the retweet count vs the like count while coloring different points according to whether a hashtag was used or not.
- Make sure you label your axes.
- Please make sure your y-axis corresponds to the retweet count
- Please make sure you have a legend for your plot, hint: `legend()`
- You can hardcode this problem at certain points but you should think about how to make this only depend on the data.
- You can either sample your data or play with transparency for the plot to show up better.
- You may want to transform the axes so outliers do not dominate the pattern in the graph.
- Please make sure your title descriptive of the key message the readers should notice.

{% include lib/mathjax.html %}
