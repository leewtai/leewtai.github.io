# Prerequisites - Introductory Statistics

You should understand the role statistics plays in the scientific method.
- **Observing** the world through summary statistics
- Formulating a **hypothesis** that explains the problem
- Collecting the relevant **data** for the question at hand (sampling and experiments)
- **Analyzing** the relevant data with respect to randomness (hypothesis testing)
- **Decide** to reject or fail to reject our null hypothesis according to the context (understand type 1 vs type 2 errors; practical vs statistical significance)

The overall logic is "similar" to proof by contradiction, we assume a statement is true, then we collect data. If the data (reality) is really unlikely under the assumption, we reject the assumption instead. We do this because it's easier to disprove things but very hard to prove anything is correct in practice.

#### Observations via summary statistics or graphs

When observing data, we often visualize different types
of data differently, e.g. histograms for quantitative vs bar charts for qualitative data.
But ultimately we care about the **distribution** of the data, i.e. the different
possible values and the respective relative frequencies (we care about the absolute frequency
if the least popular category is small).

An example of **distributions** are:
- The distribution of grades in a class could be 35% A's, 50% B's, 13% C's, and 2% F's.
- The distribution of male vs female in your city could be 49% to 51%.
- The distribution of number of children could be 0, 1, 2, 3, and 4+.

|Feature | Significance of feature | common statistics used to quantify the feature| 
|-------|--------|---------|
|Uni-modal vs multi-modal distribution| multi-modal distributions could imply multiple populations, e.g. children and adults, in the same dataset. Most summary statistics below often assume the distribution is uni-modal.| This is often eye-balled from graphs of the data.|
|Location| Where is data, e.g. are regrets with college majors around 10% (not bad) or 50% (yikes!)| mean, median, mode|
|Spread| Relative to the location statistic, how spread-out/variable is the data? e.g. 50% regret $$\pm$$ 30% is very different from 50% $$\pm$$ 5%| standard deviation, inter-quartile range (IQR), range|
|Skew|Are data values symmetrically distributed about the location statistic? Long tails imply a small fraction of values are vastly different from the majority|This is often eye-balled in introductory statistics|

How can there be multiple values that serve the same purpose, i.e. different quantities that
reflect the same feature in a distribution? This is because different statistics have different
properties, these properties result from the different calculations, and for different problems
we desire different properties.

The most popular property is the **sensitivity to extreme values** in the distribution. Means are
sensitive to values in the tail where medians are less so. An example is income where adding a
billionaire to your neighborhood would increase the mean income a lot but not impact the median income of your neighborhood.

This **sensitivity is not always bad**, different problems may want to be sensitive to the tail.
For example, housing prices are similar to income data where there
is a long right tail (this is a feature in the data). 
A policy maker would be interested in the median housing price
to understand the typical cost of living (i.e. they wouldn't want their location statistic to be sensitive to outliers) where a realtor would be interested in the
mean housing price because they earn commission as a fraction of the selling price and one
big sale could suffice for one's annual income (i.e. they want to be sensitive to the presence of rich buyers).

The spread statistics allow us to know how much data is within a certain range. For example, the fraction of data that is $$k$$ SD's away from the average is upper-bounded by $$\frac{1}{k^2}$$ . So there can be at most $$\frac{1}{2^2}$$ , i.e. 25% of the data that is away from the average beyond 2 SDs (see Chebyshev's inequality). The amount of data within one IQR from the median is at least 50%. In some sense, it allows us to know the quality of the location statistic. 

Overall, these statistics are helpful because they give us a picture of the distribution of the data without plotting and later provide a concrete number that we can measure change. 

#### Formulating a hypothesis

A hypothesis is an explanation of the observed data that can be challenged/falsified.

For example, if we observe 2 modes in the measured weights of Americans, several explanations could explain the outcome:
- Was there an error in recording the data, e.g. some in kilograms and some in pounds
	- We could challenge this by looking at the documentation
- Are children and adults both in the data?
	- We could challenge this by looking at the age distribution
- Could men and women's weights form 2 modes?
	- We could challenge this by looking at the weights separately by sex

The typical textbook hypothesis surrounds a causal question like "does vitamin C work?" This often is phrased into hypothesis like:
"Providing daily dosage of X mg of Vitamin C does not decrease the average number of sick days taken for the common cold for people in the age between 18 and 65. Any difference observed is due to individual differences and the random assignment."

This statement has several elements:
- Define "work", i.e. the outcome.
  We didn't just say "lessens the severity of the common cold" because this has many ways to measure, e.g. highest fever, number of sick-leaves taken, etc. In addition to the individual values, we summarize the values from the groups with an average. 
- Define "using" the drug, i.e. the treatment
  The ability to follow a drug regiment is difficult. Most experiments compromise with the "intent to treat", i.e. did we intend to treat you, rather than focusing on those who actually use the drug properly. 
- Who are we treating? i.e. the target population
  Some drugs are meant for people with a severe illness, some advertisements are meant for children, different populations may react differently to different treatments. It's important to know that fewer descriptors often imply more general populations.
- Provide alternative explanations (hypothesis) for the outcome differences.
  Even if the drug truly did not work, it is very unlikely for the two averages to be exactly the same. To explain this observation, we provide an alternative, other than the drug, that explains this difference. A typical hypothesis test often uses the random assignment of different individuals to explain outcome differences. 
- Is the alternative testable or falsifiable?
  The typical hypothesis testing procedure of looking at the z test statistic and p-values is how we falsify/challenge the differences due to random assignment. 

It's important to know that random assignment is only one possible explanation.

These considerations are helping us to formalize our intuition. Specifically, we define "work" by choosing one measurable outcomes for health (a simplification). We also provide an alternative explanation for the difference using random assignment (another simplification that ignores other possibilities).

#### Collecting the relevant data

There are two main questions in introductory statistics:
- How to estimate population parameters with statistics from a sample? The main worry is with sampling bias, i.e. is our sample representative of our population? This is addressed via random sampling.
- How to estimate the impact of a treatment? The main worry is confounding, i.e. are there other factors beyond our treatment that could have explained the outcome? This is addressed via random assignments and matching.
To address these biases, statisticians propose random sampling and random assignment (for treatment vs control) to turn the biases into chance-like error.

The framework to think about sampling bias is through the example of a political poll. 

|Terminology | Definition | Example via Political Polling|
|---|---|---|
|population|who you want to study|Anyone who can vote in the next election|
|the sampling frame|who you could **possibly** contact|Those with a phone number from your country|
|the sample (who responded)|who you actually contacted and responded|Those who you sampled and answered your questions|
|non-response|who you contacted but did not respond|Those who you sampled but did not respond to your phone call or answer your questions|
|illegible|who you sampled, answered your questions, but not who you want to study|Foreigners with a domestic phone number who answered the poll|
|Outside the sampling frame|who you want to study but are cannot contact|Voters without a phone number|

An example of a sampling bias is if we contacted the top 1000 phone numbers in our sampling frame, since the numbers are likely ordered in a particular fashion (e.g. Alabama first), and states have strong political leanings, our sample would not be representative. Sampling the phone numbers turns this possible bias into a chance-like error (notice that it's still possible to sample the first 1000 phone numbers in the sampling frame).

To think about confounding, we must understand the domain and alternative factors that contribute to the outcome differences. The common issue studying diets is whether life style is a confounding factor for the outcome, i.e. is life style (e.g. exercise vs not) instead of diet causing the differences we see in the data.

In other words, the reason we cannot simply study people who are on a diet today vs not and measure their outcomes is that confounding variables could explain someone's behavior and their health outcome rather than the diet having an impact on someone's health. People with healthy life styles tend to diet (e.g. no sugary drinks) and also have better health outcomes. Attributing the outcomes to the diet is ignoring the alternative explanation from the life style. 

There are two ways to address this confounding issue, random assignment and matching. Random assignment places people into the treated vs control group randomly, regardless of their confounding variable (e.g. healthy or non-healthy life styles). Matching on the other hand, tries to match people with similar life styles then assign one to treatment and the other to control.

In practice, matching is difficult because it's difficult to know and list the confounding factors upfront. In practice, we want to make sure we have no known confounders and the random assignment addresses the unknown confounders like genetics by turning the bias into a chance-like event.

A nice framework is to think about 3 sources of variability that contribute to data:
- Systematic and planned
  These are consistent and intended effects like the treatment itself.
- Systematic and unplanned (biases)
  These are consistent but unintended effects like confounders or sampling bias. 
- Chance-like error
  These are chance-like and undesirable, e.g. the difference we see between two control groups. The effect from random sampling and random assignment are under this category.

##### After converting bias to chance-like error, then what?
In the ideal world, the data would only have the influence from the treatment and nothing else. In this case we would only need one sample from the treatment and control group!

This, however, isn't realistic because there are always individual differences with the subjects, random measurement error, etc. Even genetically identical mice can have different outcomes.

To deal with chance-like error in the data, we rely on aggregate statistics on large samples where the statistics behave more like constants relative to the individual data points.
In other words, a statistic on a collection of people is more predictable than a measurement from an individual. Intuitively you may think that the individual differences will be mostly averaged out and only the treatment difference is the only thing consistently different between the treated and control group.

In classic introductory textbooks, how to calculate the necessary sample size is an important question (especially for grant writing since recruiting subjects is often a major source for cost).
The question then becomes, what sample size will make the statistic "predictable enough", i.e. its standard error (SE) is small enough.

Small enough is often defined half of your expected treatment effect, i.e. if you believe a new drug will make your smarter by 3 points, you want your SE to be around 1.5 points. Since introductory statistics only deals with averages, we only have two formulas:

- If $$X_i$$ are independent from each other, then $$SE(\frac{1}{n}\sum_i X_i) = \frac{1}{n}\sqrt{\sum_i SE(X_i)}=\frac{\sigma}{\sqrt{n}}$$
- If $$X_i$$ are draw without replacement from a population, then $$SE(\frac{1}{n}\sum_i X_i) =\sqrt{\frac{N-n}{N-1}}\frac{\sigma}{\sqrt{n}}$$
Notice that both of these decrease as $$n$$ increases.

In the formulas above, $$n$$ is the variable we need to solve, half of the treatment effect (e.g. our 1.5 points) should come from understanding the domain, and $$\sigma$$ should come from some pilot study that understands the general variability and reliability in the measurements.

The calculation above, however, does not factor in statistical power, this is a concept we'll cover below. In practice, statistical power is often what sets the sample size.

Where does this "half" come from? It'll come from the fact that the average follows a Normal distribution, this is true because something called the Central Limit Theorem, which states that averages, with a sufficient sample size, will follow a Normal distribution. What is a sufficient sample size depends on the data and is not the same.

A distribution is, again, the possible values and their respective frequency. A Normal distribution has the property:

|$$k$$| $$P(-k SD\leq$$Normal Random Variable$$- Avg \leq k SD)$$|
|---|---|
|1|$$\leq 0.68$$|
|2|$$\leq 0.95$$|
|3|$$\leq0.997$$|

This $$k=2$$ case is where the "half" above came from because we set "Effect Size = 2 * SE", so "SE = Effect Size / 2".


#### Analyzing the data

Hopefully you suspected that the work for analyzing the data has already been done in the previous step. You've determined the data to collect, how much to collect, and how you will make a decision. This part is mostly about executing those plans and some verification.

In introductory statistics, we rarely talk about the verifications needed to be done but a simple one is whether the data is what you expected? For example, if your psychology experiment has a lot more women than men, you might question the sampling procedure. Failing these verifications often means you should re-assess your data collection and delay any decision making.

But assuming the verification goes by smoothly, the analysis steps often just involve calculating the summary statistics: averages, SD, then calculating the z-test-statistic, i.e. the effect normalized by the variability in the data:
- For a population parameter this would be  $$\frac{\bar{Y} - CONSTANT}{SE_{\bar{Y}}}$$
- For an experiment this might be $$\frac{(\bar{Y}-\bar{X}) - CONSTANT}{SE_{\bar{Y}-\bar{X}}}$$
The constant depends on what your null hypothesis states, e.g. "the drug has no effect" would imply the constant is 0.

With our large samples, the z-test-statistic should follow a Normal(0, 1), i.e. Normal distribution with mean=0 and SD=1. Therefore, if the z-test-statistic is beyond 2, we would find that to be surprising under the null hypothesis, specifically, we've encountered an event, where seeing our data or something more extreme, only happens less than 5% of the time. The specific probability here is called the p-value.

#### Decision

The p-value can be thought as a surprise level (the smaller the more surprised), to make a decision, we need your risk tolerance for being wrong. There are 2 ways of being wrong:
- Type 1 error, false positive, calling something useful that is in fact not useful
- Type 2 error, false negative, calling something not useful that is in fact useful

It turns out that following the hypothesis testing procedure, i.e. rejecting the null when the p-value is less than 5% will ensure your type 1 error is at most 5%. So the p-value is compared to your Type 1 error tolerance, i.e. your significance level $$\alpha$$. If the p-value is lower than $$\alpha$$, we reject the null hypothesis, otherwise we fail to reject the null hypothesis.

However, most tests fail to reject the null hypothesis. This phrasing instead of "accepting the null" is to encourage us to think about the other reasons we might fail to reject: 
- The null is true, e.g. the drug had no effect for this measurement
- The chance-like error is too large relative to the treatment effect, e.g. small sample sizes, image 1 sample, will always fail to reject.
- Some error occurred in the analysis
- We should be tracking some other metric instead

To control for type 2 error, we often rely on something called statistical power. This is the probability of correctly rejecting the null when the alternative hypothesis is correct, P(Seeing our z-test-statistic or more extreme \| Alternative Hypothesis is True). Calculating this requires us to create a minimum detectable effect (MDE) from the domain science, this is often the same or slightly smaller than the expected treatment effect. We then calculate what's the chance of rejecting the null when the alternative is true.

It's important to note that the Type 1 and Type 2 errors here are referring to errors over many experiments, not the individual experiment being conducted. So the hypothesis testing framework is only appropriate for decisions that will happen many many times.

## Other topics
Introductory statistic courses often also teach:
- Basic logic
- Probability / Counting
- ....

In regression we won't talk much about sampling but you should know that the absolute sample size (not the sample size relative to the population) and proper randomization are keys to a quality sample.

{% include lib/mathjax.html %}
