# Homework 5

The goal of this homework is to give you some practice with text data.

Warren Buffet is considered one of the most successful investors and he writes
an [annual letter](https://www.berkshirehathaway.com/letters/letters.html) for
his clients that is widely read by most people. The Gates Foundation, one of the
largest non-profits, on the otherhand has an [annual letter](https://www.gatesfoundation.org/ideas/annual-letters)
from Bill and Melinda Gates that touches on a variety of topics.

Both letters are in the files `buffet_letters.json` and `gates_letters.json`
on Canvas respectively. Any consecutive non-alphanumeric values have been replaced
by a single space character, e.g. "Hello, today I'll teach." will become "Hello today I'll teach."

### Q0: Pre-process the data

At the end of this section, we want a term frequency matrix, i.e. a data frame where each
row corresponds to a letter and each column corresponds to a lemmatized token. Here are a few steps we would like you
to include:

- Lowercase all of the words
- Replace anything that satisfies the following regular expressions with the corresponding word:
  - `"([^0-9])(19|20)[0-9]{2}([^0-9])"` -> `"YEAR"`
  - `"\\$?[0-9]+[,\\/\\.]?[0-9]*"` -> `"NUMBERS"`
- Use the [`udpipe` package](https://bnosac.github.io/udpipe/docs/doc2.html) to lemmatize and tokenize the sentences in the letter.
  You can get sentences simply by separating the letters by `\n` before using `udpipe_annotate()`
  - If you have memory issues here, try the [package `textstem`](https://cran.r-project.org/web/packages/textstem/index.html) instead.
    You may choose your own tokenization package as well if you choose this route.
- (optional) You may perform other processes if you believe your computer is hitting some memory issues
  e.g. dropping any word with 2 or fewer characters, handling links like we handled years, etc
- Count the occurrences of each lemmatized token within each letter

Please report the dimension of your data frame at the end and print out the histogram that
shows the distribution of word presence across all words, e.g. "be" likely appears in 100% of the letters,
"GEICO" may appear in 10% of the letters, ... the histogram should show us these percentages (or counts) across all words.


### Q1: Calculating TF-IDF

Please calculate the TF-IDF matrix using the definition of term frequency as "the occurrence of a token
normalized by the occurrence of the most frequently used token in the letter". Please use $log(\frac{N}{n_t})$ as
your inverse document frequency where $N$ is the number of letters and $n_t$ is the number of letters that contain the
term $t$.

Please calculate, for each token, its maximum TF-IDF value across all letters and assign this to a variable named `mtfidf`.

Please plot the histogram of `mtfidf` along with a vertical red line.
The red line should be largest value within `mtfidf` that corresponds to a word listed under the [stopwords package](https://www.rdocumentation.org/packages/stopwords/versions/2.3).

Please also report the number the stopwords you used to calculate the red line value above and the number of tokens
within `mtfidf` values less than or equal to the red line value. 

Please write 1 or 2 paragraphs on how we should handle the tokens that have `mtfidf` values below the red line value yet
are not considered "stopwords" by the package.

### Q2: Clustering text

Please choose at least the top 60 tokens based on your TF-IDF matrix above. This is left intentionally open for you to explore different options.

Using your TF-IDF matrix, please cluster the letters using k-means clustering and hierarchical clustering
using the "ward.D" linkage method. Please pick one method and try to **explain** the resulting clustering either visually,
algorithmically, or using simple statistics. You can quote news articles or wikipedia pages to support your findings as well.

### Q3: Final Project

This section is mostly graded on completion with coherent sentences.

- Please summarize the goal of your data mining final project using 3 or fewer sentences.
- Please list one or more individuals or entities who would, under ideal circumstances, change their behavior or be willing
  to pay for the results of your data mining efforts.
- Please produce one visualization using one of the datasets for your final project.
- Please articulate one **obvious** pattern you expect to see in your data, i.e. something that would not be considered
  an insight.


{% include lib/mathjax.html %}
