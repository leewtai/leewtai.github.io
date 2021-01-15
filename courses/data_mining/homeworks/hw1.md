# HW1 - Review

This homework is to meant for you to brush up some prerequisites.
If some of these topics are new to you, feel free to ask on Piazza how to approach these.

### Context - Is gold price inversely related to the market?

There's a belief that the money from the stock market will escape to gold
when the stock market is not doing well. The demand for gold and the expectations
for the market are often reflected in the pricing of the assets, i.e. high demand yields
high gold prices and upward expectations also lead to higher stock prices.

#### Q1 
Please use the 'TIME_SERIES_WEEKLY' API listed on [Alpha Vantage](https://www.alphavantage.co/documentation/)
to get the weekly time series data for
- 'VOO': an arbitrarily chosen ETF that tracks the market
- 'GDXJ': an arbitrarily chosen ETF for gold

For this problem, simply show the code for your query and print out the number of weeks of data for each time series.
Your API key should NOT appear in your solutions but the URL you're using and the query should be shown.

Hint:
- You will need to [claim a free API key](https://www.alphavantage.co/support/#api-key) before you can query data
- The functions in `httr` should be helpful, here is [some sample code](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_scraping_and_api.html) if you have not done so before.


#### Q2
Please plot the `close` price for VOO against the different weeks and overlay the regression line for this scatter plot.
- You do not need to label your week index but the prices should be labeled.


#### Q3
Please plot the residuals from the regression in Q2 against the `close` price of GDXJ.
- label your axes with units.
- Your title should include the correlation value, rounded to the nearest hundredth.
- Please show the code that demonstrates your decision on merging the 2 time series.

#### Q4
Relying only on the scatter plot, would you say the belief between gold and the market
is supported or rejected? Please explain.

{% include lib/mathjax.html %}
