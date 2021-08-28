## Introduction

One of the key metrics airlines track is their turn-around time at airports.
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


