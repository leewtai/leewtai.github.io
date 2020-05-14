library(jsonlite)
library(httr)

api_key <- read_json("../credentials.json")['nytimes']

url <- "https://api.nytimes.com/svc/search/v2/articlesearch.json"

params = list(q= 'college', 'api-key'=api_key, page= 2)
response = GET(url=url, query=params)
out = content(response)

today <- strftime(Sys.time(), '%Y%m%d')
write_json(out, paste0('nytimes_article_search_', today, '.json'))
