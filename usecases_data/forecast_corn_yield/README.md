# Predicting corn yields

One of the biggest challenges in agriculture is to forecast the amount of corn that will be harvested in the US (given the decreasing land dedicated to agriculture). 
This also commonly one of the headlines in the [USDA announcements](https://www.nass.usda.gov/Newsroom/2024/) and
[drastically affect commodity prices](https://fred.stlouisfed.org/series/PMAIZMTUSDM).

There are many sources for corn yield data but the most official survey is the US Department of Agriculture (USDA)
National Agricultural Statistics Service (NASS). They [survey farmers](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Agricultural_Yield/index.php) then aggregate the results to create (surprisingly) accurate forecasts for the total production of corn each year. This survey is different from the census, which is calculating from tallying actual yields reported for tax filing purposes. 

To get the data, the [NASS QuickStats API](https://quickstats.nass.usda.gov/api) is recommended. You'll need to register for a key here.

An example code to retrieve the data is shown [here](../usda_quick_stat/pull_usda_qs.R). It is important to know that "yield" is calculated by total production (the mass of corn, US is special in using bushels, a volume measure for this) divided by the land (the acres of land harvested). There are scenarios where land can be planted but not harvested (e.g. puddling causing the roots to rot).

Tasks:
- Run the example code above. Notice the same state, same year, and same variable (e.g. production vs acres harvested) produces multiple records. On what columns do these records differ by? Are there certain ones you would discard?
- Focusing on yield, how good are the NASS surveys in predicting the census values? Please factor in both the "length of forecast"  and "accuracy" in your answer.
- Please correlate the commodity prices with the NASS data.
- If there are any data quality issues, critical to the forecasting task, please state them clearly.
- Does forecasting for the entire US work better than forecasting for each state separately then combining the total?
  - Please define how far ahead your forecast is and what is your evaluation metric.
- Here's some corn trivia, please attempt to verify or disprove one of these. Since they all require some additional data pulling, please describe your new dataset carefully (you are encouraged to limit your analysis below to something smaller than the states):
  - Early planting dates allow farmers to plant hybrids that produce more corn because they have a longer growing season. Planting dates are usually influenced by the time the land is warm enough (e.g. not freezing). Can we verify that earlier warming, leads to earlier planting, which also corresponds to higher yields?
  - Pollination is a critical stage for the corn plant. The belief is that hot days and cool evenings are desirable. Do we see evidence for this?
  - There is a belief that when the corn prices are low, less land is reported for agricultural use (tax reasons), do we see this?
  - Any other agricultural trivia is welcomed but please cite your source :)
- Please produce and justify your best forecast model. 
