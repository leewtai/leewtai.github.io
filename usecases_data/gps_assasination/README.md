# GPS Battleship

[NYTimes wrote a special report about location data privacy](https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html). With only location data, individual identities
could still be inferred and marketers could target you easily.

To showcase this issue, your goal in this project is to use my 2 week location history
then try to "assassinate" me in the 3rd week by estimating the time and location of my personal phone.


### Data
Data is collected on my Android phone using the [GPSLogger](https://play.google.com/store/apps/details?id=com.mendhak.gpslogger&hl=en_US) application which is free but not of high quality.

The data is available on Canvas under `TBD.zip`.

The data is in a GEOJSON format which is similar to a JSON format. Here's some sample code to
help load in the data:

```r
library(jsonlite)

dat <- read_json('data/20200819132607.geojson')
head(dat[['features']], 2)

```

```python
import json

dat = json.load(open('data/20200819132607.geojson', 'r'))
dat['features'][:2]
# [{'type': 'Feature',
#   'properties': {'time': '2020-08-19T19:26:13.000Z',
#    'provider': 'gps',
#    'time_long': 1597865173000,
#    'accuracy': 15.008,
#    'altitude': 1031.24609375,
#    'bearing': 352.6,
#    'speed': 0.94},
#   'geometry': {'type': 'Point', 'coordinates': [-113.99907373, 46.88842983]}},
#  {'type': 'Feature',
#   'properties': {'time': '2020-08-19T19:26:11.540Z',
#    'provider': 'network',
#    'time_long': 1597865171540,
#    'accuracy': 19.681,
#    'altitude': 961.7999877929688},
#   'geometry': {'type': 'Point', 'coordinates': [-113.9991175, 46.8882159]}}]
```

#### Special notes on the data
- The distance unit is meters
- The timestamps did not capture the time zone correctly.
- Each file is a different day
- Data loss is common


### Rules

A correct 
In addition to the 2 week location data, you can place a bomb


### What you need to turn in
(should include rubric)



