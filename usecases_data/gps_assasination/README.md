# Assasination Classroom

<img src="assassinate_classroom.png" alt="Assassination Classroom" width='600'>

[Assassination classroom by Yusei Matsui](https://en.wikipedia.org/wiki/Assassination_Classroom) is the inspiration for the project! In this comic, a teacher is training students to assassinate himself. Why? Find out yourself :)

Similarly, your challenge is to use 2 weeks of my phone GPS data to "bomb" me on my usual path in the 3rd week. You'll have one attempt only!

### Project deliverables
At the end of the project, you need to submit:
- A bomb plan, which is an algorithm that will produce:
  - The day of the week
  - The time of explosion (see rules below)
  - The longitude and latitude of my location (see rules below).
- Your code on GitHub. A classmate will be using your code to validate your attempts on the 3rd week. Make sure your code can run and has enough comments for someone to install the necessary dependencies.
- A written report on how you solved the problem. This should be written for a classmate who is not enrolled in this course. This report should include
  - An introduction
  - A description of the data with visualizations
  - A description of your final approach/model
  - A description of your level of confidence, i.e. model validation
  - A conclusion (at most one paragraph)


### Data
Data is collected on my Android phone using the [GPSLogger](https://play.google.com/store/apps/details?id=com.mendhak.gpslogger&hl=en_US) application which is free but lacking in precision.

The data is available on Canvas under `TBD.zip`.

The data is in a GEOJSON format which is similar to a JSON format. Here's some sample code to
help load in the data. If you are unfamiliar with JSON data, just ask for help!

```r
library(jsonlite)

dat <- read_json('data/20200819132607.geojson')
head(dat[['features']], 1)
```

```python
import json

dat = json.load(open('data/20200819132607.geojson', 'r'))
dat['features'][:2]
```

A single record from the GPS looks like this
```
{"type": "Feature",
 "properties": {"time": "2020-08-20T21:13:09.831Z",
                "provider": "gps",
                "time_long": 1597957989831,
                "accuracy": 19.296001,
                "altitude": 965.132568359375,
                "bearing": 208.8,
                "speed": 2.02},
 "geometry": {"type": "Point",
              "coordinates": [-114.00013904, 46.88713864]}
}
```
If you plot the data over time across different days, you'll see my path:
<img src="initial_gps_glimps.png" alt="sample path over days" width='600'>


#### Special notes on the data
- The distances are in meters and times are in seconds
- The timestamps did not capture the time zone correctly.
- Each file is a different day
- Data loss is common with GPSLogger (it's free!)
- The data was cleaned so you cannot actually infer my dwellings over summer :)
- To get distances in meters from longitude and latitude data, you can
  use the great circle distance or UTM projections (zone=12)

### Rules
To succeed, your bomb must be placed within 5 meters and 10 seconds to my position in the 3rd week.

Since my summer schedule was irregular, my departure time each day varied wildly.
To fix this issue, you'll also be given the timestamps when I start moving.

For the 3rd week, GPSLogger values will be taken as "truth". If there is data
loss, it will be treated as if I disappeared from the planet during those times, i.e.
I cannot be bombed.

I look forward to your assassination attempts!
