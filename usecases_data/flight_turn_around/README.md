## Introduction

One of the key metrics airlines and airports track is the turn-around time for each
plane at airports.
Shorter turn-around time are valuable because they can lead to higher usage
for planes and also because long turn-around times can often highlight issues
early on with the machines or operations.

## Intent

The intent is to have one major project split into 3 portions that will cover different
topics in the applied statistics course.

- Explore the turn-around time for different airports
- Predict the turn-around times for future flights
- Augment the dataset with

## Skills required

- Computing
- Regression and regularized regressions
- Time series

## Data source

We're specifically using the dataset labeled as [On-Time : Reporting Carrier On-Time Performance (1987-present)](https://www.transtats.bts.gov/tables.asp?gnoyr_VQ=FGJ&flf_gnoyr_anzr=g_bagVZR_eRcbegVaT).


## Guidance

#### Exploratory data analysis

- Please visit the website and find the **Download** hyperlink associated with the dataset: [On-Time : Reporting Carrier On-Time Performance (1987-present)](https://www.transtats.bts.gov/tables.asp?gnoyr_VQ=FGJ&flf_gnoyr_anzr=g_bagVZR_eRcbegVaT). Please download all of the data corresponding to 2019 Jan-Dec with the following variables (this is somewhat manual)
  - FlightDate (yyyymmdd)
  - Unique Carrier Code
  - Tail Number
  - Flight Number
  - Origin Airport
  - Destination Airport
  - Actual Departure Time (local time: hhmm)
  - Difference in minutes between scheduled and actual departure time. Early departures show negative numbers.
  - Wheels Off Time (local time: hhmm)
  - Wheels On Time (local time: hhmm)
  - Actual Arrival Time (local time: hhmm)
  - Difference in minutes between scheduled and actual arrival time. Early arrivals show negative numbers.
  - Cancelled Flight Indicator (1=Yes)
  - Specifies The Reason For Cancellation
  - Diverted Flight Indicator (1=Yes)
  - Distance between airports (miles)
  - Flight Time, in Minutes
- Please filter the data so we only have the data that **departs** from PDX or SEA.
- Please report how many flights are in the year 2019 after filtering?
- How would you summarize the "utilization rate" for the different airports?
- What data quality issues have you noticed? What results will be impacted by these issues?
- Are turn-around times independent of the destination airport? How would you test this idea?
- Is there a cyclical pattern to the turn-around time? Please use a graph and a paragraph to justify your answer.
- Are turn-around times the same across airlines (i.e. carriers)?


#### Some modeling and prediction

#### Expanding the dataset
