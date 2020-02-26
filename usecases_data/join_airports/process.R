faa <- read.csv("748757223_T_T100I_MARKET_ALL_CARRIER.csv")
faa_domestic <- read.csv("748757223_T_T100D_MARKET_ALL_CARRIER.csv")

slim <- unique(faa[, c("ORIGIN", "ORIGIN_AIRPORT_ID", "DEST", "DEST_AIRPORT_ID")])
slim_domestic <- unique(faa_domestic[, c("ORIGIN", "ORIGIN_AIRPORT_ID", "DEST", "DEST_AIRPORT_ID")])

write.csv(slim, "unique_international_us_flights_2019.csv", row.names = FALSE)
write.csv(slim_domestic, "unique_domestic_us_flights_2019.csv", row.names = FALSE)
