# Data is using
# https://www.alphavantage.co/documentation/

library(dplyr)
library(httr)
library(jsonlite)

# This is to not expose my api_key...
creds <- read_json('../credentials.json')
api_key <- creds[['alpha_vantage_api_key']]
url <- "https://www.alphavantage.co/query"

symbols = c('VOO', 'BLV', 'BSV', 'VTIP', 'BIV', 'VTC',
            'VIG', 'VUG', 'VYM', 'VV', 'VO')
params <- list("function"="TIME_SERIES_DAILY_ADJUSTED",
               outputsize='full',
               apikey=api_key)
Sys.sleep(60)
dfs <- list()
for(symbol in symbols){
    print(symbol)
    params['symbol'] <- symbol
    response <- GET(url=url, query=params)

    dat <- content(response)
    ts <- dat[['Time Series (Daily)']]
    df <- bind_rows(ts)
    names(df) <- sub("[0-9]+\\. ", "", names(ts[[1]]))
    df <- as.data.frame(sapply(df, as.numeric))
    df$date <- names(ts)
    df$symbol <- symbol

    dfs[[symbol]] <- df
    Sys.sleep(12)
}
bdf <- bind_rows(dfs)

# jsonlite::write_json(bdf, "alpha_vantage_etfs_ts_daily.json")
write.csv(bdf, 'alpha_vantage_etfs_ts_daily.csv', row.names=FALSE)
