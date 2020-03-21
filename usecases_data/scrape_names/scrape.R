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
