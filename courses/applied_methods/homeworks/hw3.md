# Homework3 - Practice with Kalman Filters

### Goals
The purpose of this homework is to give you some exercise with applying
Kalman Filters on the spatio-temporal data used in project 2.

Some basics on [GPS](https://en.wikipedia.org/wiki/Global_Positioning_System):
- GPS coordinates depend on satellites orbiting in space. The time
  delay from passing signals to your phone from the satellite will inform
  us the distance between the satellite and your phone. Once you have this distance
  across multiple satellites, we may infer your position on the planet.
- These coordinates are noisy since the measurements are not perfect.

Please show ALL code for this assignment.

#### Question 0 Familiarizing yourself with the data
On Canvas, you can find the dataset `gps.zip` but we will focus on a single file for this assignment.
Please load the file `20200826131614.geojson` which should be read like a usual JSON file.

- Please create a data frame with the longitude, latitude, and the human-readable time stamp in 3 columns. Please
  make sure the order of the rows respect the order of the original file.
- How many longitude/latitude records are in the file?
- Are the data points in chronological order according to the human-readable time stamps, yes/no, please articulate your logic?
- Plot the first 10 records in the file according to their longitude/latitude. Next to each point, please indicate their order (1, 2, ... etc).
  - You should notice an anomaly with the first 10 records, please articulate this anomaly.
- Leveraging the anomaly you observed above, please remove data points that have this feature.
  - Please state how many points have you removed. This is an ad hoc/naive data processing method, you
    should not feel obligated to do the same in Project 2.
- Please summarize the time differences between records to answer the following questions:
  - What seems like the intended data collection frequency (temporal), i.e. one record per X seconds or X records per second?
  - A session is often defined as times of activity broken up by periods of non-activity. If we use 60 seconds of non-activity to separate different sessions, how many sessions do you observe in the dataset? Note that the application does not record data when it believes the phone is stationary (i.e. no activity is detected).


#### Question 1: The Dynamic Linear Model
Recall the generic dynmaic linear model which describes the relatinoship between the observed data and the underlying state:
$$Y_t = F_t \theta_t + v_t$$
and the relationship between the states at different times:
$$\theta_t = G_t \theta_{t-1} + w_t$$

For this assignment, you should treat $$Y_t$$ as your noisy measured position at time $$t$$ where $$\theta_t$$
is your true position **and** speed at time $$t$$, i.e. $\theta_t$ would be a 4 dimension vector with your
2 dimension true position information along with your 2 dimensional velocity. This description already imposes
restrictions on what $$F_t$$ and $$G_t$$ can be. Let $$Y_t=\begin{bmatrix} X_t \\ Z_t \end{bmatrix}$$ be a 2 by 1 vector
with the noisy position data in 2 dimensions. If $$\theta_t = \begin{bmatrix} \mu_{x, t} \\ \mu_{z, t} \\ \nu_{x, t} \\ \nu_{z, t}\end{bmatrix}$$
is a 4 by 1 vector with the true position and velocity.
- Please write out the matrix for $$F_t$$, hint: what is the relationship between the "truth" and a noisy measurement of it?
- What is the dimension of $$G_t$$, i.e. how many rows and columns does this matrix have?
- $$V = Cov(v_t)$$, if we assume the noise between the 2 dimensions in your noisy position are independent, what does this imply about the matrix $$V$$.
- We are ignoring the impact of "acceleration" in our current setup. Please articulate intuitively how you would introduce acceleration into this model.
  - Between $$\theta_t$$, $$v_t$$, $$w_t$$, and $$Y_t$$, which term(s) would "capture" the error from ignoring effects from acceleration? For example, when we ignore
    a regressor in regression that are not confounders, the $$\epsilon$$ term captures the effect of these missed values.

#### Question 2: Computing DLMs with Projections

Unfortunately, degrees in longitude and latitude do not translate into distances properly, e.g. 1 degree in latitude is different from 1 degree
in longitude in terms of absolute distance.
To remedy this, we will project the data into [UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
coordinates where the distances between UTM coordinates are meters.

To do so, we need the libraries `sp` and `rgdal`. Please install these in a special environment isolated from your other classes.
The spatial library `gdal` (necessary dependency for `rgdal`) is notorious for breaking people's computing environments if you're not careful.
The following code should help you convert longitude/latitude coordinates into UTM coordinates. Sadly, we will not go into details of projections
for this class.
```r
library(sp)
library(rgdal)
# This following step is similar to transforming time stamps like "2020-01-25" into a time object
spat_df <- SpatialPointsDataFrame(coords=df[, c("longitude", "latitude")],
                                  data=df['time_stamp'],   # This needs to be a data frame
                                  proj4string=CRS("+proj=lonlat +datum=WGS84"))
# This step converts the longitude/latitude -> UTM
utm_df <- spTransform(spat_df, CRSobj = "+proj=utm +zone=12 +datum=WGS84")
utm_coords <- coordinates(utm_df)
```
- According to your answers in Question 0 and 1, please complete the following code. Hint: `dt` should be a representative number for the time between records
  ```r
  gps_variance <- 20^2
  v_mat <- SOME_MATRIX_BASED_ON_GPS_VARIANCE
  dt <- SOME_NUMBER
  g_mat <- matrix(c(1, 0, dt, 0,
                    0, 1, 0, dt,
                    0, 0, 1, 0,
                    0, 0, 0, 1), byrow=TRUE, ncol=4)
  avg_walk_speed_m_per_sec <- 1.4  # https://en.wikipedia.org/wiki/Walking
  dlm_spec <- dlm(
    FF= SOME_MATRIX
    GG= g_mat,
    V = v_mat,
    W = diag(c(5, 5, 1, 1)^2),
    m0 = matrix(c(utm_coords[1, ], rep(avg_walk_speed_m_per_sec / dt, 2)),
                ncol=1), # A vector by R defaults is a k by 1 matrix
    C0 = diag(rep(10^2, 4)))
  dlm_filter_mod <- dlmFilter(utm_coords, dlm_spec)
  dlm_smooth_mod <- dlmSmooth(dlm_filter_mod)
  ```
- Please plot the first 100 positions from the noisy measurements, the Kalman filter `dlm_filter_mod`, and the Kalman Smoother `dlm_smooth_mod`
  on the same graph then **comment on their difference** (this should create 300 points).
- Please use the output from `dlm_smooth_mod` to extract the speed (speed = $$\sqrt{velocity_x^2 + velocity_z^2}$$) across the records.
- Please examin the speed distribution across the different data collection sessions, what can you infer from this comparison?

#### Question 3: Final Project Check-in
- Please write down the main question for your final project.
  - Please articulate the ideal dataset for answering your question
  - Please articulate how this is related to on-going research on Columbia or how it will help an existing effort you wish to accomplish.

{% include lib/mathjax.html %}
