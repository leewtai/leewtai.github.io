# Teaching confidence intervals as the set of non-rejected parameter values

Confidence interval is one of the most popular yet also most misunderstood concepts in
statistics. Most practictioners confuse confidence intervals with credible intervals.
Even Statisticians confuse these interpretations sometimes (CITATION). This paper
argues that rebranding and teaching the confidence interval differently can alleviate
this misunderstanding.

The first proposal is to rebrand the confidence interval as not-rejected intervals (NRI).
The first reason for this rebranding is a simple word association for students. The word
"confidence" only appears in reference to confidence intervals (or confidence levels)
where "fail to reject" and rejecting hypotheses are common place and rarely confusing.
Although "compatibility intervals" were proposed in (CITATION), I believe introducing new
vocabulary is likely to create more confusion than not.
The second reason is precision about the interval's meaning.
Practictioners commonly "accept" the null hypothesis when the confidence interval fails
to reject the null.

The standard language of "fail to reject" is intentinoally chosen such that when practictioners
understand that a non-significant result can be due to an under-powered study, the null hypothesis is
true, or an incorrectly specified model.

(Citation) has detailed the common misunderstanding between NRIs and credible intervals.
These inlcude: ....

The second proposal is to teach confidence intervals as the set of all possible parameter
values that does not disagree with the data at hand too widely.
The error rate is capped by the significance level.

### Starting with the special case
Imagine playing hide and seek with a real number, $$p$$ hidden on the unit interval. 
For the most extreme case, imagine that out data $$X \sim Bernoulli(p)$$ has only $$n=1$$.
What is a confidence interval in this case?

This seemingly simple question is not obvious to most students (???). In introductory courses,
we often construct confidence intervals using the Normal approximation to the binomial distribution
when $$n$$ is large but rarely talk about the small sample scenario.

A practical researcher might simply state $$[0, 1)$$ if $$X = 0$$ and $$(0, 1]$$ if $$X = 1$$,
noticing that one data point is not entirely uninformative yet the data is small enough that
we should not dwell on the precise confidence interval.
However, given the tolerance of a $$\alpha$$% error rate, we should soon realize that the confidence
interval could be tightened to $$[0, 1-\alpha]$$ and $$[\alpha, 1]$$ respectively.

Common misunderstandings between confidence intervals and credible intervals.

Constructing confidence intervals for the mean of a population is one of the most classic
examples (CITATION). The instructional materials often follow the steps of
- generating $$B$$ realizations of data from the population with mean $$\mu$$
- calculating the sample average $$\bar{X}_i$$ for $$i \in 1, \dots, B$$.
-
Traditionally, people teach confidence intervals using the


Things to read:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742490/

http://www.stat.columbia.edu/~gelman/research/published/uncertainty_intervals.pdf
https://www.tandfonline.com/doi/epub/10.1080/00031305.2018.1527253?needAccess=true


Common Mistakes:
credit: https://www.thoughtco.com/confidence-interval-mistakes-3126405
- Percentile method in bootstrap
- What is the chance that your confidence interval contains the mean?
- What percent of the data falls within the interval?
- What percent of sample means fall within the interval?
- Does this interval capture all sources of error?
Credit: https://www.tandfonline.com/doi/epub/10.1080/00031305.2018.1527253?needAccess=true
- Rejection of null = acceptance of alternative
- Ignores subordinate factors
- stat sig = practical sig
Robust misinterpretations of confidence intervals:
https://pubmed.ncbi.nlm.nih.gov/24420726/
- non-significant outcome is proof for absence of effect
- significant outcome as proof for the existance of an effect


Study design:
https://files.eric.ed.gov/fulltext/ED502272.pdf

{% include lib/mathjax.html %}
