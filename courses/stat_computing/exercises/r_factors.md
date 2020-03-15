#### Excercises

- What error is produce when we try to turn a character into a numeric value?
  ```r
  char_demo <- c("red", "blue", "blue", "green", "red")
  as.numeric(char_demo)
  ```
- Without running the code, try to guess the output from the final line.
  ```r
  facts <- factor(c("red", "blue", "blue", "green", "red"))
  levels(facts)
  # [1] "blue"  "green" "red"  
  levels(facts)[facts]
  ```
