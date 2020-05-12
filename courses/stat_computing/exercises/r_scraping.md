#### Exercise

Let's try to get the most popular male vs female baby names in the US.
Please visit the [Social Security Website for most popular names in the 1990s](https://www.ssa.gov/oact/babynames/decades/names1990s.html).
Please try to scrape the male and female names along with the numbers.
1. Use `GET()` to obtain the HTML information.
2. What tag contains the data we're interested in?
3. Please write the xpath that will grab all the tags that is one level above your answer in 2)
4. Use `xml_text()` on the first row from the table so the entire row is converted into a single character (i.e. both names and nubmers, along with the popularity rank).
5. Write a loop to obtain all the rows information, then use regular expression to obtain the names and numbers for each sex.
