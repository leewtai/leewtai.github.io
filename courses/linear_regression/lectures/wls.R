
# morning period has 5 sections, each with 20 students
# afternoon period has 20 sections, each with 30 students

section_n <- c(20, 30)
section_freq <- c(5, 20)
ms <- c(82, 75)
period_n <- section_n * section_freq
n <- sum(period_n)
x <- rnorm(n, mean = rep(ms, period_n), sd=7)
y <- x + rnorm(n, sd=7)
y <- ifelse(y >= 100, 100, y)
df <- data.frame(midterm=x, final=y,
                 period=rep(c("morning", "non-morning"), period_n),
                 section=rep(1:sum(section_freq), rep(section_n, section_freq)))
plot(x, y, col=rep(c('red', 'black'), period_n))
gdf <- aggregate(df[, c("midterm", "final")], df[c("section", "period")], mean)
head(gdf)
plot(gdf$midterm, gdf$final,
     col=rep(c("red", "black"), section_freq))


ols_mod <- lm(final ~ midterm, gdf)
# wls_mod <- lm(final ~ midterm, gdf, weights=)
