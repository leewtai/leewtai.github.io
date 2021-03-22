# Data is using
# https://www.alphavantage.co/documentation/

library(httr)
library(jsonlite)

# This is to not expose my api_key...
creds <- read_json('../credentials.json')
api_key <- creds[['alpha_vantage_api_key']]
url <- "https://www.alphavantage.co/query"

params <- list("function"="TIME_SERIES_DAILY_ADJUSTED",
               symbol="VOO",
               outputsize='full',
               apikey=api_key)
response <- GET(url=url,
                query=params)
dat <- content(response)
ts <- dat[['Time Series (Daily)']]
ts_features <- sub("[0-9]+\\. ", "", names(ts[[1]]))
length(ts)

split_coeff <- as.numeric(sapply(ts, function(x) x[['8. split coefficient']]))
split_inds <- which(split_coeff != 1)
split_days <- names(ts)[split_inds]
adj_close <- sapply(ts, function(x) x[['5. adjusted close']])
dates <- strptime(names(ts), '%Y-%m-%d')

plot(dates, adj_close)

jsonlite::write_json(dat, "alpha_vantage_voo_ts_daily.json")
