# Data is using
# https://www.alphavantage.co/documentation/

library(httr)
library(jsonlite)

# This is to not expose my api_key...
source('api_key')
url="https://www.alphavantage.co/query"

params <- list("function"="TIME_SERIES_INTRADAY",
               symbol="VFINX",
               interval="60min",
               apikey=api_key)
response <- GET(url=url,
                query=params)
dat <- content(response)
ts_names <- sub(".* ", "", names(dat[['Time Series (60min)']][[1]]))

jsonlite::write_json(dat, "alpha_vantage_ts_intraday.json")

demo <- dat[['Time Series (60min)']][[1]]
