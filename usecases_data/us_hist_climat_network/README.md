# Manipulating Non-Grid Spatial Data

https://www.ncdc.noaa.gov/ushcn/introduction

[US Historical Climatology Network](https://www.ncdc.noaa.gov/ushcn/introduction)
(USHCN) is a network of weather stations
in the US since early 1990s. The variables collected are precipitation,
daily maximum and daily minimum temperatures.

This is a good dataset to explore climate patterns and data manipulation.

Features in the data:
- The data is stored per-station so visualizing an entire map for one
  year requires some manipulation.
- Data quality flags exist for various reasons
- The data is stored in a compact .raw format where the k and k+1
  character in each row represent the state code rather than relying
  on delimiters. This information is stored in a readme.txt file.
- There are missing values since not all stations were operational
  for each year.

[Instructions on getting Climate Data](https://pcmdi.llnl.gov/mips/cmip5/data-access-getting-started.html)

[variable list](https://pcmdi.llnl.gov/mips/cmip3/variableList.html)
