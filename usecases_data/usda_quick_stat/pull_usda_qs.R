# This file pulls data from USDA
library(httr)
library(jsonlite)

URL <- "http://quickstats.nass.usda.gov/api/"

params <- list(param="class_desc",
               key="")
out <- GET(paste(URL, "get_param_values", sep=""),
           query=params)
char_content <- rawToChar(out$content)
data <- fromJSON(char_content)
data[[params[['param']]]][1:10]

# Estimate the count of variables
year_start <- 1950
year_end <- 2018
years <- year_start:year_end
names(years) <- rep('year', length(years))
short_descs <- c("CORN, GRAIN - ACRES HARVESTED",
                 "CORN, GRAIN - PRODUCTION, MEASURED IN BU")
names(short_descs) <- rep('short_desc', length(short_descs))

params <- list(sector_desc="CROPS",
               commodity_desc="CORN",
               group_desc="FIELD CROPS",
               domain_desc="TOTAL",
               agg_level_desc="STATE",
               key="")
params <- c(years, short_descs, params)
out = GET(paste(URL, 'get_counts', sep=""),
          accept_json(),
          query=params)
est_rows = content(out)[['count']]
if(est_rows > 50000){
    print(paste("too many records, estimating ", est_rows, 
                " data call will fail"))
} else {
    print(paste('Estimated ', est_rows, ' rows of data'))
}
# Calling the desired output
usda_resp <- GET(url=paste(URL, 'api_GET', sep=""),
                 query=params)

usda_resp$status_code == 200
data <- content(usda_resp)[['data']]

data <- as.data.frame(do.call(rbind, data))
write.csv(data, paste(c("state_level", year_start, year_end, "corn_yield.csv"), collapse="_"), row.names=FALSE)
