setwd("~/repos/leewtai.github.io/courses/linear_regression/section/rep_papers/why_do_people_stay_poor/")
df = read.delim("data/PovertyTraps_replication_data.tab.tsv")
df0 <- read.delim('data/PovertyTraps_analysis.tab.tsv')

df['pAssets'] = df$pAssets/1000

df['k0t'] = ifelse(df$survey == 1, df$pAssets, NA)
mean(is.na(df$k0t))
mean(df$survey == 1)

df['pAssets'] = ifelse(
    df$survey == 1
    & df$treat == 1
    & df$stup ==1,
    df$pAssets+(df$Pcows_no/1000),
    df$pAssets)


df['Qcows'] = df$Pcows_no * df$cows_no
df['Qpoultry'] = df$Ppoultry_no * df$poultry_no
df['Qgoat'] = df$Pgoat_no * df$goat_no
df['Qland'] = df$Pland_own_total_size * df$land_own_total_size
for(i in 4:13) {
    new_var = paste0('Qasset', i)
    p_val = paste0('Passet_value', i)
    no_val = paste0('asset_no', i)
    df[new_var] = df[p_val] * df[no_val]
}
Qassets = names(df)[regexpr('^Qasset', names(df)) > 0]
df['QbizAssets'] = apply(df[Qassets], 1, sum, na.rm=TRUE)
all_assets = c('Qcows', 'Qpoultry', 'Qgoat', 'Qland', 'QbizAssets')
df['QpAssets'] = apply(df[all_assets], 1, sum, na.rm=TRUE)
df['QpAssets'] = df$QpAssets/1000
Qk0t = ifelse(df$survey == 1, df$QpAssets, NA)
Qk0 = aggregate(Qk0t, list(df$hhid), max, na.rm=TRUE)
names(Qk0) <- c('hhid5', 'Qk0')
df <- merge(df, Qk0, all.x=TRUE)
rm(Qk0, Qk0t)
df['QpAssets'] = ifelse(
    df$survey == 1
    & df$treat == 1
    & df$stup == 1,
    df$QpAssets + (df$Pcows_no/1000), df$QpAssets)
summary(df$QpAssets)
summary(df0$QpAssets)


k0 = aggregate(df$k0t, list(df$hhid5), max, na.rm=TRUE)
names(k0) <- c('hhid5', 'k0')
df <- merge(df, k0, all.x=TRUE)
dim(df)
df['k0t'] <- NULL
# k0[k0['hhid5'] == 2572, ]
# df0[df0$hhid5 == 2572, c('hhid5', 'k0', 'survey_wave')]
# df[df$hhid5 == 2572, c('hhid5', 'k0', 'survey_wave')]
# summary(df$k0)
# summary(df0$k0)
# head(df0[which(is.na(df0$k0)), c('hhid5', 'k0', 'survey_wave')])

for(i in 1:5){
    sdf <- df[df$survey == i, ]
    agg_df <- aggregate(sdf[c('pAssets', 'QpAssets', 'resp_age', 'savings')],
                        list(sdf$hhid5), max, na.rm=TRUE)
    names(agg_df) <- c('hhid5', paste0('k', i), paste0('Qk', i), paste0('savings', i),
                       paste0('age', i))
    agg_df['survey_wave'] <- i
    df <- merge(df, agg_df, all.x=TRUE)
}

for(i in 0:5){
for(j in 1:4){
    survey_i = i
    if(i == 0) survey_i <- 1
    survey_cond <- df$survey == survey_i
    class_cond <- df$sclass == j
    if(i == 5) class_cond <- TRUE
    sdf <- df[survey_cond & class_cond, ]
    k_var <- paste0('k', i)
    cap <- quantile(sdf[[k_var]], .99)
    df[k_var] <- ifelse(
        survey_cond & class_cond & df[[k_var]] >= cap, NA, df[[k_var]])

    Qk_var <- paste0('Qk', i)
    Qcap <- quantile(sdf[[Qk_var]], .99)
    df[Qk_var] <- ifelse(
        survey_cond & class_cond & df[[Qk_var]] >= Qcap, NA, df[[Qk_var]])
}}
a <- df[, c('survey_wave', 'sclass', 'k0', 'hhid5')]
b <- df0[, c('survey_wave', 'sclass', 'k0', 'hhid5')]
aa <- merge(a, b, by=c('survey_wave', 'sclass', 'hhid5'))
head(aa[!is.na(aa$k0.x) & is.na(aa$k0.y), ])

vars_to_log <- c(
    names(df)[regexpr('^k[0-5]', names(df)) > 0],
    names(df)[regexpr('^savings', names(df)) > 0],
    names(df)[regexpr('^Qk[0-5]$', names(df)) > 0])

for(v in vars_to_log){
    df[paste0('L', v)] <- log(df[[v]] + 1)
}


vars_to_diff <- c(paste0('Lk', 2:5), paste0('LQk', 2:5))
for(v in vars_to_diff){
    base_var <- paste0(sub('[0-9]$', '', v), '1')
    df[paste0('delta', v)] <- df[v] - df[base_var]
}


df['Qk'] <- df$QpAssets
for(i in 1:5) {
    sdf <- df[df$survey == i & df$stup == 1, ]
    cap <- quantile(sdf$Qk, .99, na.rm=TRUE)
    df['Qk'] <- ifelse(df$Qk > cap & df$survey == i,
                       cap, df$Qk)
}

write.csv(df, 'data/r_rep_povertytraps_analysis.csv')
dim(df0)
dim(df)
names(df0)[!(names(df0) %in% names(df))]
names(df)[!(names(df) %in% names(df0))]
mean(is.na(df0$Qk))
mean(is.na(df$Qk))


**------------------------------------------------------------------------------
** PREPARE DATASET FOR STRUCTURAL ESTIMATION
**------------------------------------------------------------------------------
use "$Data/PovertyTraps_analysis.dta", clear 

set seed 190518
tempfile pf

* estimate production function (treatment villages only) -----------------------
keep if treat==1
replace pAssets=pAssets*1000
trimmean(pAssets), perc(1) gen(tri)
replace pAssets=. if tri==0
gen pAssets2=pAssets^2
gen pAssets3=pAssets^3
keep if survey==2
drop if pAssets==.
su livestock_hours_tot if stup==1
gen hiredInLabour = ot_livestock_hours_total + M_livestock_hours_total if head_gender==1
replace hiredInLabour=ot_livestock_hours_total  if head_gender==0
 drop if livestock_hours_tot==.
for var hiredInLabour: replace X=0 if X==.
gen totalLabour=hiredInLabour + livestock_hours_tot 

		/*estimate income as non linear function of K and L, cubic for low K, quadratic for high K*/
 nl (livestock_inc_tot=(({b1=0.5}*pAssets+{b2=0.5}*pAssets2)*(totalLabour)^{b4=0.5}))  

 gen b1=/b1
 gen b2=/b2
 gen b4=/b4
  
collapse b1 b2 b4 , by (branchid)

su b1 b2 b4
save `pf'

* main dataset: income, wage and hours -----------------------------------------
use "$Data/PovertyTraps_analysis.dta", clear 

gen savRate=savings/(savings+(pce_total*hhsize_adult_eq))
gen hiredInLabour=ot_livestock_hours_total +M_livestock_hours_total if head_gender==1
replace hiredInLabour=ot_livestock_hours_total  if head_gender==0
replace hiredInLabour=0 if hiredInLabour==.

keep hiredInLabour savRate livestock_inc_tot agri_daylabor_inc_tot maid_inc_tot selfemp_inc_tot wage_inc_tot poultry_inc_tot livestock_hours_tot agri_daylabor_hours_tot maid_hours_tot selfemp_hr_tot wage_hr_tot poultry_hours_tot total_hours_work pAssets livestock_inc_per_hr agri_daylabor_inc_per_hr maid_inc_per_hr total_income_resp branchid spotno hhid5 survey k0 treat stup cows_no other_poor middle rich sclass

for var *_inc_tot: renvars X, postdrop (7)
for var *_: renvars X, postf("Y")
for var *_hours_tot: renvars X, postdrop (9)
for var *_: renvars X, postf("H")
for var *_hr_tot: renvars X, postdrop (6)
for var *_: renvars X, postf("H")
for var *_inc_per_hr: renvars X, postdrop (10)
for var *_: renvars X, postf("R")
rename k0 pAssets0
rename total_hours_work labour_H
rename total_income_resp labour_Y

gen labour_R= labour_Y/labour_H


	/* NOTE: wage_H unavailable for W4. Compute as sum of maid and agri_daylabor hours.
		We use only maid and ag labor, since those are the two main wage labor 
		occupations and total income in those allows us to compute hourly wage  */
		
replace wage_H = maid_H + agri_daylabor_H if wage_H==.										


bys survey branchid: egen maidW=mean(maid_R)
bys survey branchid: egen agri_daylaborW=mean(agri_daylabor_R)

bys survey: egen maidWA=mean(maid_R)
bys survey: egen agri_daylaborWA=mean(agri_daylabor_R)

egen wageM=rowmean(maidW agri_daylaborW)
egen wageMA= rowmean(maidWA agri_daylaborWA)

for var *_H: gen Xshare=X/labour_H

label var hiredInLabour "HH members hours in livestock"

for var *_Y: label var X "income in activity X"
for var *_R: label var X "income per hour in activity X"
for var *_H: label var X "hours in activity X"
for var *W: label var X  "mean wage in X, branch level"
for var *WA: label var X "mean wage in X"
label var wageM "average maid/aglab wage, branch level"
label var wageMA "average maid/aglab wage"


	/* merge dependency ratio (?)
	
		rename hhid5 hhid3
		merge m:1 hhid3 using "${Data}/allHHMembers_dependencyratio.dta"
		drop if _merge==2
		drop _merge
		//rename hhid3 hhid5
		
	*/
	
	/* threshold variables
	
		gen kHat=2.34
		gen loSavKHat=2.36
		gen hiSavKHat=2.28
		label var kHat "k threshold"
		label var loSavKHat "k threshold for low saving HH"
		label var hiSavKHat "k threshold for high saving HH"

	*/
	
	




	* merge production function parameters 
merge m:1 branchid using `pf', nogen

	* save data
	
order branchid spotno treat survey_wave stup selfemp_H selfemp_Y wage_H wage_Y maid_H maid_Y maid_R poultry_H poultry_Y livestock_H livestock_Y livestock_R agri_daylabor_H agri_daylabor_Y agri_daylabor_R cows_no labour_H labour_Y hhid5 pAssets pAssets0 savRate hiredInLabour labour_R maidW agri_daylaborW maidWA agri_daylaborWA wageM wageMA selfemp_Hshare wage_Hshare maid_Hshare poultry_Hshare livestock_Hshare agri_daylabor_Hshare labour_Hshare 
	
compress
save "$Data/structural/input/PovertyTraps_structural.dta", replace 





* additional datasets ----------------------------------------------------------

	* HH wealth classes

	* wage hours by branch 
	
	* specially targeted ultra-poor (stup) IDs 
	
	* wave 5 only


**------------------------------------------------------------------------------
** PREPARE DATASET FOR SHAPE TEST AND P-SPLINE ESTIMATION
**------------------------------------------------------------------------------

use "$Data/PovertyTraps_analysis.dta", clear 
keep if survey==1 & stup & treat & Lk3!=. & Lk1<=3
keep Lk1 Lk3 
order Lk1 Lk3 
export delimited using "$stest/Test1data.csv", replace
 
