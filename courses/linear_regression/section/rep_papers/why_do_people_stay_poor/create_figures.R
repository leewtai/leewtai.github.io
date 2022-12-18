df0 <- read.delim('data/PovertyTraps_analysis.tab.tsv')

# Figure 1
df <- df0[df0$survey == 1, ]
cond <- !is.na(df$Lk0) & df$treat == 1
plot(density(df$Lk0[cond], weights = df$popWeight[cond], na.rm=TRUE), col="blue")
cond <- !is.na(df$Lk0) & df$treat != 1
lines(density(df$Lk0[cond], weights = df$popWeight[cond], na.rm=TRUE), col="red")

cond <- !is.na(df$Lk1) & df$treat == 1
plot(density(df$Lk1[cond], weights = df$popWeight[cond], na.rm=TRUE), col="blue")
cond <- !is.na(df$Lk1) & df$treat != 1
lines(density(df$Lk1[cond], weights = df$popWeight[cond], na.rm=TRUE), col="red")


## Figure 4
cond <- (
  df0$survey == 1
  & df0$stup == 1
  & df0$treat == 1
  & df0$Lk1 <= 3
)
sdf <- df0[cond, ]
xmin <- log(10 * 18 / 1000 + 1)
xmax <- log(1000 * 18 / 1000 + 1)
plot(sdf$Lk1, sdf$Lk3, xlim=c(xmin, xmax), ylim=c(xmin, xmax))
lines(lowess(sdf$Lk1, sdf$Lk3, delta=0.062), col="blue")
abline(a=0, b=1, col="red")

df0['Lk1_placebo'] <- ifelse(df0$treat == 1, df0$Lk1, NA)
df0[df0$treat == 0, 'Lk1_placebo'] <- log(df0$k0 + df0$Pcows_no / 1000 + 1)[df0$treat == 0]
cond <- (
  df0$survey == 1
  & df0$stup == 1
  & df0$treat == 0
  & df0$Lk1_placebo <= 3
)
sdf <- df0[cond, ]

plot(sdf$Lk1, sdf$Lk3, xlim=c(xmin, xmax), ylim=c(xmin, xmax))
lines(lowess(sdf$Lk1, sdf$Lk3, delta=0.45), col="blue")
abline(a=0, b=1, col="red")



# Table 2
cond <- df0$survey == 1 & df0$stup == 1
sdf <- df0[cond, ]
hh <- log(sdf$k0 + sdf$Pcows_no/1000 + 1)
aboveT <- ifelse(!is.na(sdf$Lk1), sdf$Lk1 > 2.333, NA)
cond <- sdf$treat == 0 & !is.na(hh)
aboveT[cond] <- (hh > 2.333)[cond]
summary(lm(sdf$deltaLk3 ~ aboveT, subset=sdf$treat == 1))

