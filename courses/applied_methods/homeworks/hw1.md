# Applied Statistical Methods - Homework 1

### Goals
- Get you familiarized with NYTimes comment data
- Data wrangling exercise
- Exercise on generating data from text

### Format
Please return a **PDf** file with your solutions on Canvas.

### Questions
One of the problems in class will look into the comments associated
with various NYTimes articles. In this homework, you'll learn how to
obtain this data yourself.

#### Question 0
Please [create an account with NYTimes for API keys](https://developer.nytimes.com/get-started).
Using these keys, please obtain the [archive file in NYTimes published in March 2020](https://developer.nytimes.com/docs/archive-product/1/overview) and report the following:
- How many articles are there
- For each record, which fields store the author's first and last name?

#### Question 1
There's the comments data in the file `Canvas/Files/Data/nytimes_2020_articles_with_comments.json`.
Load this using `jsonlite::read_json()`. This file was produced by using every article in the archive
above and querying it against the [NYTimes community API](https://developer.nytimes.com/docs/community-api-product/1/overview). This file is quite large even after we've dropped some fields in the data already.
Please make one call to the community API and determine which fields did we drop from the original data?

#### Question 2
What is the main headline of the article with the most comments?

#### Question 3
Please process the comments data into a data frame where each row is a different comment, 
and the columns each contain:
- the numebr of recommendations received
- the displayed name of the commenter on NYTimes
- the update time
- the approved time
- whether the article was selected by the editors
- the number of words in the comment
- the number of unique words in the comment

#### Question 4
Join the data frame in Question 3 with the information from the archive related to
- The author's first name
- The author's last name
- The "news desk" of the article
- The published date of the article

#### Question 5
If our population of interest was all the news articles from NYTimes in March 2020.
What type of sample would you say we have?
