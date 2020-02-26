# Overall

# Summary

In early 2020, coronavirus is becoming an issue and one could ask which airports
in the US are 1 degree (direct flight) vs 2 degrees away from Wuhan (the epicenter of the epidemic). 

To accomplish this, a simple joining exercise between flights between any
US airport and an international airport along with 


## Intent
- Joining data from 2 different files.
- Probability reasoning of 2nd degree nodes on a graph (simple elementary)

## Skills required
- Joins
- Reading in .csv files
- Ability to think about connecting flights

# Data source

## Website
https://www.transtats.bts.gov/Tables.asp?DB_ID=111&DB_Name=Air%20Carrier%20Statistics%20(Form%2041%20Traffic)-%20All%20Carriers&DB_Short_Name=Air%20Carriers

## Details
Data is downloaded from the above website for the following tables
- T-100 International Market (All Carriers)
- T-100 Domestic Market (All Carriers)
- Wuhan Tianhe International Airport has a code of WUH.

### Lookouts
- The airport code IST has 2 airport IDs in 2019
- To get the complete 2nd degree data, we are missing the 1st degree airports
  from WUH to non-US airports, that then lead into the US.
