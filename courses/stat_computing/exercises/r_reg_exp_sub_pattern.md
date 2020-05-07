#### Exercise

- Here is a slightly modified demo:
  ```r
  demo <- c("https://www.google.com", "http://www.r-project.org",
            "https://www.linkedin.com", "http://xkcd.com")

  pattern <- "https://(www\\.)?[^\\.]+\\.(com|org)"
  sub(pattern, "caught ya!", demo)
  ```
  Please modify `pattern` so all values will be replaced with `"caught ya!"`
- Please try to get the email addresses from the following examples:
  ```r
  demo <- c("this is my email: test1@yahoo.com",
            "test2@yahoo.com",
            "@Doug, please reply to test-user3@yahoo.com")
  ```
