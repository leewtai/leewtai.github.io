# Applied Statistical Methods - Homework 0

### Goals
- Refresh and assess your basics from the required courses.
- Encouraging you to setup your jupyter notebook properly.

### Format
Please return a **PDf** file with your solutions on Canvas.

### Questions
Please download the data `Canvas/Files/Data/unemployment_cpi_unempl_2000_2020.json`
This is a dataset from the [Bureau of Labor Statistics](https://www.bls.gov/data/#api)
regarding inflation and unemployment.

In economics, we believe that low unemployment will lead to higher inflation.
The reasoning being that labor is hard to find so employers need to attract
workers with higher salaries. With higher salaries, people are willing to pay
more for goods and therefore leading to inflation. We will validate this theory
at the US national level at a very coarse time scale.

The time series data:
- "LNS14000000" is the [seasonally adjusted national unemployment rate](https://data.bls.gov/timeseries/LNS14000000)
- "CWUS0000SA0" is the [consumer price index based on urban wage earners](https://data.bls.gov/timeseries/CWUS0000SA0)
  - To obtain inflation from this, we simply calculate the percentage change based on
    these values.
  - These values are referenced such that the prices in years 1982-84=100.
  - We will assumed "1st half" = Jan-June and "2nd Half" = July-Dec.


#### Q0 - Standardizing the dataset
Please read in the JSON data and export a CSV file with the following columns:
- year
- period: this should take on values between "1st Half" or "2nd Half"
- unemployment: this should be an average percentage over the appropriate months
- cpi: this shouldn't need much processing

Hint: if you haven't seen a JSON file before, here's some sample code for R:
```
library(jsonlite)
data <- read_json("MYFILE.json")
class(data)
```

#### Q1 - Calculate the inflation
Using your results from Q0, please calculate the inflation rate and add a column to your
data named **inflation**. For example, the inflation rate for 2000, 2nd Half should be 
`(170.2 - 167.6)/167.6 * 100 = 1.55%`. If an inflation cannot be calculated, please
replace the value with NA.

#### Q2 - Visualizing the data
Please plot the scatter plot between the inflation and unemployment rate with the
axes labeled with units. Inflation should be on the y-axis.

#### Q3 - Fit a regression and analyze the output
Fit an OLS to the scatter plot in Q2 and report the fitted slope and its p-value.
Why is the slope relevant to our problem here (at most 3 sentences)?

#### Q4 - Assumptions
Which assumptions were required for your p-value in Q3 to make sense?

#### Q5 - Test whether the inflation is independent of the unemployment rate via permutation test
Please write the code for the following:
- Calculate the correlation between the 2 variables and record this value.
- Repeat the following 1000 times: shuffle the order of one of the variables, then recalculate the correlation.
- Please plot the histogram of these recalculated correlations against the original correlation.
- Please comment on what you can infer from the histogram

#### Q6 (not graded)
- Please setup your Zoom account so your headshot photo will be displayed even when your camera is off.

{% include lib/mathjax.html %}
