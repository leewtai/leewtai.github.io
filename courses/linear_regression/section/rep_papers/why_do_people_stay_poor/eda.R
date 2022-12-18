df <- read.delim('data/PovertyTraps_replication_data.tab.tsv')

dim(df)
head(names(df))

vars = sapply(df, var)

which(names(df) == 'pAssets')

df['pAssets'] = df$pAssets / 1000

df['k0t'] = ifelse(df$survey_wave == 1, df$pAssets, NA)
df['pAssets'] = ifelse(df$survey_wave == 1
                       & df$treat == 1
                       & df$stup == 1,
                       df$pAssets + df$Pcows_no / 1000,
                       df$pAssets)
asset_class = c('cows', 'poultry', 'goat', 'land')
asset_class = c(asset_class, paste0('asset', 4:13))
for(i in seq_along(asset_class)){
    asset = asset_class[i]
    new_var = paste0('Q', asset)
    if(regexpr('^asset', asset) > 0){
        asset_num = sub('asset', '', asset)
        quant_asset = paste0('asset_no', asset_num)
        val_asset = paste0('Passet_value', asset_num)
    } else if(asset != 'land') {
        quant_asset = paste0(asset, '_no')
        val_asset = paste0('P', asset, '_no')
    } else {
        quant_asset = 'land_own_total_size'
        val_asset = 'Pland_own_total_size'
    }
    print(asset)
    print(new_var)
    print(val_asset)
    print(quant_asset)
    df[new_var] = df[val_asset] * df[quant_asset]
    print(mean(is.na(df[new_var])))
}

Qassets = names(df)[regexpr('Qasset', names(df)) > 0]
df['QbizAssets'] = apply(df[, Qassets], 1, sum)
df['QpAssets'] = apply(df[, c('Qcows', 'Qpoultry', 'Qland', 'Qgoat', 'QbizAssets')], 1, sum)
mean(is.na(df$QbizAssets))
mean(is.na(df$QpAssets))

df['QpAssets'] = df$QpAssets / 1000
df['Qk0t'] = ifelse(df$survey_wave == 1, df$QpAssets, NA)
hh_Qk0 = tapply(df$Qk0t, df$hhid, max, na.rm=TRUE)

mean(is.na(df$pAssets)) # <0.0002

df[1, ]
