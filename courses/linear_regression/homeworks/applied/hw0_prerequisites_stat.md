# Homework 0: Prerequisite - Stat

#### Goals
Homework 0 is meant to give you a concrete understanding of the prerequisites for this class. If you find these challenging, you should reach out to the TA to brush up on these topics.

### Q1 - Data types and graphs

For your grpahs, please make sure to explain what each axis is. You can draw your solution as well.

- Medium is a website for writers and they believe there's an optimal hour to send a notification
  email to get readers onto their website. Someone calculated the "click rate" for each hour, i.e.
  total clicks divided by the total emails sent for each hour. How should they visualize this? 
- Arizona is interested in learning whether the extreme heat has hurt their tourism. Someone has collected
  some data on the daily maximum temperature each time and the number of visitors to the national parks in the
  following week. How should they visualize these?
- Someone wants to understand if the banks prefer schools from NYC (because NYC has a high concentration
  of financial firms). They have some data on whether the candidate's school is from NYC, and also
  whether the candidate was offered an interview. How should they visualize this?
  - For the question above, please draw 2 graphs: one that shows a preference for NYC schools and another
    that does not show a preference.


### Q2 - Data features and statistics

Please provide a one sentence explanation after your answer.

- Rent is well known to have a long right tail. A government employee is sent to understand the "typical
  living cost" for a New Yorker and rent is one of the biggest factors contributing to this number.
  What one statistic is best appropriate for understanding the typical rent for a New Yorker?
- Housing prices is well known to have a long right tail. A real estate agent earns a commission based
  on the selling price of houses, i.e. the higher the price, the more they make. Pretend a real estate
  agent can make roughly 20 deals a year only. If a real estate agent is trying to rank neighborhoods
  based on the housing priecs within each neighborhood. What statistic should they use on the housing
  prices to perform this ranking?
- Pretend a typical Youtube influencer creates content roughly the same length as their previous
  content because consumers like the consistency. When the length of the content starts to fluctuate,
  it's likely that the influencer might stop producing more content. What statistic would be a good
  measure to detect this?

### Q3 - Hypothesis and logic

- If a subscriber does not like their subscription AND if they are short on money, they will cancel
  the subscription. According to that statement, is it logical to assume that anyone who cancels their
  subscription is short on money? Explain with 1 to 2 sentences please.
- Someone wants to test if a one-week "social-media-cleanse" will make someone happier. How should they
  formulate their null hypothesis? Remember to state what can explain the difference, if not the cleanse,
  between the treatment and control group under the null hypothesis.

### Q4 - Collecting data

Please explain your reasoning with 2-4 sentences.

- Past psychology experiments commonly used college students as test subjects, e.g. seeing if reading
  negative content will make someone depressed. What form of bias might occur here given psychology is
  often interested in studying universal traits for the entire adult population?
- Someone wants to understand people's college experiences after graduating and recruited people through
  a post on NYTImes titled ["If You Could Choose Your College Again, What Would You Do Differently?"](https://www.nytimes.com/2023/01/18/opinion/choosing-college-regrets.html), what concerns would you have with this data collection strategy?


### Q5 - Analyzing the data

- What is the smallest sample size necessary for a survey to estimate the
  percentage of households with guns (binary answer: do you currently have a gun or not in the household?)
  with a 95% CI of width at most 2%. You can assume that the target population is a town in the U.S. with 10000 households
  and we would sample households without replacement. You should assume that the Central Limit theorem will kick
  in. Please do this calculation two ways with different assumptions for the Standard Error of a single household.
  - First, use a dated US overall average, i.e. [30% of households](https://www.pewresearch.org/social-trends/2017/06/22/the-demographics-of-gun-ownership/) currently have a gun. The standard error of a binary outcome is linked to the percentage.
  - Second, for binary outcomes, the standard error of a single outcome is always upper-bounded by 0.5.


### Q6 - Decisions

- A researcher is experimenting on a memory-enhancing practice (e.g. memory palace) vs a control. Their p-value
  turned out to be 0.07 and their significance level was the classic 5%. What should they conclude? 
  Can they accept the null hypothesis?
- What is type 1 vs type 2 error?

### Q7 - Hypothesis or not

- [Someone has lost their kids suddenly and is now accused of harming them](https://en.wikipedia.org/wiki/Sally_Clark).
  Why is a hypothesis test with the null hypothesis: "they are innocent" not appropriate?
- Pretend 10% of college essays are automatically generated by Artificial Intelligent (AI) technology. A
  college admissions officer employed an [algorithm](https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00140-5)
  that claims to be able to detect whether the essay was
  written by AI or not with a sensitivity of 90% and specificity of 80%. Now they're reading an essay that the
  algorithm has flagged as being written by AI, what's the probability that it was indeed written by AI?
  - [Sensitivity and specificity are commonly used in medicine](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)

{% include lib/mathjax.html %}
