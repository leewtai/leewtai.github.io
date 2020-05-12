library(httr)
library(xml2)

target_url <- "http://stat.columbia.edu/department-directory/faculty-and-lecturers/"


web_response <- GET(url=target_url)
web_content <- content(web_response, as='text')
html_dat <- read_html(web_content)
# The 'xpath' is like a regular-expression like language for xml trees
# our code here says look for "h3" nodes with the attribute of class="cn-entry-name"
name_node <- xml_find_all(html_dat, xpath='//h3[@class="cn-entry-name"]')
name_link_node <- xml_children(name_node)
all_names <- xml_text(name_link_node)


# Baby example:
target_url <- "https://www.ssa.gov/oact/babynames/decades/names1990s.html"

web_response <- GET(url=target_url)
web_content <- content(web_response, as='text')
html_dat <- read_html(web_content)
name_node <- xml_find_all(html_dat, xpath='//tbody/tr')
nas <- sapply(name_node, xml_text)
tail(nas)
nas <- nas[1:200]
nas_split <- strsplit(nas, split=" +")
mens <- sapply(nas_split, function(x) x[[2]])
womens <- sapply(nas_split, function(x) x[[4]])
answer <- data.frame(men=mens, women=womens)
write.csv(answer, "~/repos/leewtai.github.io/courses/stat_computing/data/men_women_names.csv", row.names=FALSE)

