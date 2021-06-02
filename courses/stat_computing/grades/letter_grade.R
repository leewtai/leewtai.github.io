library(tidyverse)
library(patchwork)
theme_set(theme_minimal())
data_all <- read_csv("data/20201226_132800_courseworks.csv")

# Peter had reached out early saying that he didn't know about the "Mark" button
# in the homeworks, i did agree to see i this would impact his final grade.
# condition <- data_all[['SIS User ID']] == 'pdk2115'
# data_all[condition,c('hw1', 'hw2')] <- 1


data_all <- data_all %>%
  filter(final > 0) %>%
  mutate(midterm = midterm * 2/3 + midterm_twitter/20 * 1/3,
         final = final * 1/2 + final_business/24 * 1/2) %>%
  select(Student:Section, hw1, hw2, hw3, hw4, hw5, midterm, final) %>% 
  mutate(total = 0.2 * (hw1 + hw2 + hw3 + hw4 + hw5) / 5 + 
           0.35 * ifelse(final > midterm, final, midterm) + 
           0.35 * final +
           0.1,
         Section = ifelse(Section ==
                            "STATGR5206_004_2020_3 - STAT COMP & INTRO DATA SCIENCE",
                          "Thibault", "Wayne"))
plot_grades <- function(data) {
  p1 <- data %>% 
    ggplot(aes(x = total, color = Section)) + 
    stat_ecdf() +
    labs(y = "ECDF")
  theme(legend.position = "none")
  p2 <- data %>%
    ggplot(aes(x = total, y = Section, color = Section)) +
    geom_boxplot() +
    theme(legend.position = "none")
  p3 <- data %>%
    ggplot(aes(x = total, color = Section)) +
    geom_density()
  p1 + p2 + p3
}

plot_grades(data_all)

t_test <- t.test(total ~  Section, data = data_all, alternative = "greater")

summary_stats <- data_all %>%
  group_by(Section) %>%
  summarize(min = min(total, na.rm = TRUE),
            q25 = quantile(total, prob = 0.25, na.rm = TRUE),
            mean = mean(total, na.rm = TRUE), 
            sd = sd(total, na.rm = TRUE),
            median = median(total, na.rm = TRUE),
            mode =  map_dbl(list(density(total)), function(f) f$x[which.max(f$y)]),
            q75 = quantile(total, prob = 0.75, na.rm = TRUE),
            max = max(total, na.rm = TRUE))

## Adjust the data by matching quantiles
quantile_thibault <- function(p) quantile(x = data_all %>% 
                                            filter(Section == "Thibault") %>% 
                                            pull(total),
                                          probs = p)

data_adjusted <- data_all %>%
  mutate(total = ifelse(Section == "Wayne" & total > 0.5, 
                        quantile_thibault(ecdf(total)(total)), total))

summary_stats_adjusted <- data_adjusted %>%
  group_by(Section) %>%
  summarize(min = min(total, na.rm = TRUE),
            q25 = quantile(total, prob = 0.25, na.rm = TRUE),
            mean = mean(total, na.rm = TRUE), 
            sd = sd(total, na.rm = TRUE),
            median = median(total, na.rm = TRUE),
            mode =  map_dbl(list(density(total)), function(f) f$x[which.max(f$y)]),
            q75 = quantile(total, prob = 0.75, na.rm = TRUE),
            max = max(total, na.rm = TRUE))

plot_grades(data_adjusted)

## Add letter grades
add_grades <- function(data) {
  cutoffs <- c(-0.1,
               0.5,
               0.65,
               0.75,
               0.85,
               0.9,
               0.99,
               2)
  levels <- c("F", paste0(rep(c("B", "A"), each = 3), 
                          rep(c("-", "", "+"), 2)))
  
  data %>%
    mutate(grade = cut(total, breaks = cutoffs, 
                       labels = levels, right = FALSE)) %>%
    arrange(total)
}

a <- data_adjusted %>% 
  select(Student, Section, total) %>%
  add_grades() 

write.csv(a, 'data/assigned_grades_2020.csv')
a %>%
  count(Section, grade) %>%
  pivot_wider(names_from = grade,
              values_from = n,
              names_sort = TRUE)

