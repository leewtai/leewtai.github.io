library(lubridate)

df <- read.csv("global_pref_survey_individual.csv")

dates <- as_date(df$date)
range(dates, na.rm=TRUE)


date_ranges <- tapply(dates, df$country, range)
png('date_ranges_cntry.png')
boxplot(dates ~ df$country)
dev.off()


dim(df)
max(sapply(df, function(x) mean(is.na(x))))

max(tapply(df$isocode, df$country, function(x) length(unique(x))))
max(tapply(df$region, df$country, function(x) length(unique(x))))
max(tapply(df$ison, df$country, function(x) length(unique(x))))

redundant_feats <- names(df) %in% c('ison', 'country', 'X', 'id_gallup')
df <- df[, -which(redundant_feats)]
df['isocode'] <- as.factor(df$isocode)
df$age[df$age == '99 99+'] <- '99'
df$age <- as.integer(df$age)
df$age2 <- df$age^2
df$age_norm <- df$age / 100
df$age2 <- df$age_norm^2

mod <- lm(patience ~ subj_math_skills + gender + age_norm + age2 + isocode, data=df)
summary(mod)$coefficients[1:6, ]
head(mod$coefficients)

has_na <- apply(df[, c('patience', 'subj_math_skills', 'gender', 'age_norm', 'age2', 'isocode')], 1, function(x) any(is.na(x)))
sum(!has_na)


mod2 <- lm(patience ~ subj_math_skills + gender + age_norm + isocode, data=df)
summary(mod2)
summary(mod2)$coefficients[1:6, ]

png('marginal_patience.png', 600, 400)
par(mfrow=c(1, 2))
plot(df$age2, df$patience, pch=16, col='#00000022')
plot(df$age2[!has_na], mod2$residuals, pch=16, col='#00000022')
dev.off()

png('distr_patience.png')
hist(df$patience)
dev.off()

png('residuals.png')
plot(mod$fitted.values, mod$residuals, pch=16, col='#00000022')
dev.off()

cor(mod$fitted.values, mod$residuals)

df['math2'] <- df$subj_math_skills^2
df['math3'] <- sample(df$subj_math_skills)
mod3 <- lm(patience ~ subj_math_skills + math3 + gender + age_norm + age2 + isocode, data=df)
summary(mod3)$coefficients[1:6, ]
summary(mod3)

