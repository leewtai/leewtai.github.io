library(jsonlite)

alpha <- jsonlite::read_json("alpha_vantage_voo_ts_daily.json")

ts <- alpha[['Time Series (Daily)']]
dates <- names(ts)
features <- sub('[0-9]+. ', '', names(ts[[1]]))
df <- t(sapply(ts, function(x) as.numeric(unlist(x))))
df <- as.data.frame(df)
names(df) <- features
df$dates = dates

write.csv(df, 'alpha_vantage_voo_ts_daily.json', row.names=FALSE)
