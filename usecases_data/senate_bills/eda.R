library(jsonlite)
library(plyr)

votes <- jsonlite::fromJSON('votes.json')
voters <- jsonlite::fromJSON('voters.json')
votes_dfs <- lapply(votes, as.data.frame)
votes_df <- plyr::rbind.fill(votes_dfs)
rownames(votes_df) <- names(votes_dfs)
voting_matrix <- t(votes_df)

# Explore two party division using correlation of voting records
senate_cor <- cor(voting_matrix, use='pairwise.complete.obs')


cor_vals <- senate_cor[lower.tri(senate_cor)]
hist(cor_vals)

mcconnell <- 'S174'
condition <- !is.na(senate_cor[, mcconnell])
senate_cor <- senate_cor[condition, condition]
my_ord <- order(senate_cor[, colnames(senate_cor) == mcconnell], decreasing=TRUE)
senate_cor <- senate_cor[my_ord, my_ord]
image(senate_cor, col=hcl.colors(12, 'RdBu'), zlim=c(-1, 1))

poss_rep <- senate_cor[, 1] > 0.2

cor_with_repub <- apply(senate_cor[, poss_rep], 1, function(x) mean(x, na.rm=TRUE))

condition <- senate_cor[, 1] < 0 & cor_with_repub > 0
condition <- senate_cor[, 1] > 0 & cor_with_repub < 0

cor_with_repub[condition]

ols <- lm(voting_matrix[,1] ~ voting_matrix[, 2])
summary(ols)
