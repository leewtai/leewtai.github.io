library(readxl)
library(tidyverse)
library(ggplot2)

inventory <- read_csv("~/Downloads/Registrar Clasrooms Inventory_2020_aw_10062021.xlsx - rg_room_attributes.csv")
# Quick sanity check for duplicates
dim(inventory)
dim(unique(inventory[, c("Building", "Room_Code")]))
# Sanity check that Uris and Warren are nnot i nthe inventory
sum(regexpr("uris", tolower(inventory$Building)) != -1)
sum(regexpr("warren", tolower(inventory$Building)) != -1)

new_invt <- read_csv("~/Downloads/Uris & Warren Classrooms_V2.xlsx - Sheet1.csv")
# WARNING, last 2 values are NA
new_invt_cap <- new_invt$Occupancy
invt_cap <- inventory[['Seating Capacity Count']]

temp_cat <- cut(seq(1, 400, by=20), breaks=seq(0, 400, by=20))
seat_cap <- data.frame(capacity=cut(c(invt_cap, new_invt_cap), seq(0, 400, by=20), labels=levels(temp_cat)),
                       source=rep(c('2020 Inv', 'Uris/Warren'), c(length(invt_cap), length(new_invt_cap))))
seat_cap_sum <- aggregate(rep(1, nrow(seat_cap)), seat_cap, sum, drop=FALSE)
png("current_seat_capacity_hist.png", 800, 400)
ggplot(seat_cap_sum, aes(fill=source, x=capacity, y=x)) + geom_bar(position="stack", stat="identity")
dev.off()

dat <- read_excel("sequestered_use_fall16-fall21_10072021_v2.xlsx")

# Why are there multiple Class_Building_Code to a Building Name?
# e.g. LAW + GRE both map to Green Hall Law Building
dat <- dat %>% select(-Class_Building_Code, -Student_Enrollment_Count...22)
# Seems like you need Building_Code + Class_Room_Code to get a unique classroom
# e.g. Class_Room_Code 101 maps to Green Hall Law Building, PRENTIS HALL, and more
enrollment <- dat[['Student_Enrollment_Count...14']]
capacity <- dat$Seating_Capacity_Count

uniq_terms <- unique(dat$Term_Identifier)
for(ut in uniq_terms){
    condition <- dat$Term_Identifier == ut
    temp_enroll <- enrollment[condition]
    temp_cap <- capacity[condition]
    enroll_cats <- cut(temp_enroll, seq(0, 600, 20), include.lowest=FALSE)
    cap_cats <- cut(temp_cap, seq(0, 600, 20), include.lowest=FALSE)
    temp_dat <- data.frame(enrollment=enroll_cats, capacity=cap_cats)
    temp_sum <- aggregate(rep(1, nrow(temp_dat)), temp_dat[1], sum, drop=FALSE)
    png(paste0("term_", ut,"_enroll_hist.png"), 1200, 400)
    myplot <- ggplot(temp_sum, aes(x=enrollment, y=x)) + geom_bar(stat="identity") +
        ggtitle(paste0("Term: ", ut)) + scale_y_continuous(limits=c(0, 90))
    print(myplot)
    dev.off()
}


names(dat)
# Days are very complicated, these are requested classes (over representative of weird schedules perhaps?)
dat <- dat[dat$Term_Identifier == 20213, ]
day_cnts <- table(dat$Class_Days_Code)
day_cnts[day_cnts > 10]
enrollment <- dat[['Student_Enrollment_Count...14']]
enroll_cats <- cut(enrollment, seq(0, 600, 20), include.lowest=FALSE)

begin_cnts <- table(dat$Class_Begin_Time)
begin_cnts[begin_cnts > 10]

for(j in 1:4){
    lvl <- levels(enroll_cats)[j]
    condition <- enroll_cats == lvl
    temp_dat <- dat[condition, ]
    png(paste0("time_block_enrollment_", j,".png"), 500, 1000)
    plot(1, 1, type="n", xlim=c(0, 7),
         ylim=c(500,2400), main=paste("2021 Fall - Enrollment", lvl),
         ylab="Time of Day", xlab="Day of Week (1=Monday)")
    for(i in seq_len(nrow(temp_dat))){
        days <- strsplit(temp_dat$Class_Days_Code[i], "")[[1]]
        ybottom <- rep(temp_dat$Class_Begin_Time[i], length(days))
        ytop <- rep(temp_dat$Class_End_Time[i], length(days))
        days_fact <- factor(days, levels=c("M", "T", "W", "R", "F", "S"))
        xleft <- as.numeric(days_fact) - 0.5
        xright <- as.numeric(days_fact) + 0.5
        rect(xleft=xleft, xright=xright, ybottom=ybottom, ytop=ytop, col="#00000011")
    }
    dev.off()
}

# the subcommittee wants to see the data broken out by sizes of the rooms



dat$popular_time <- (
    grepl("[MTWR]", dat$Class_Days_Code) &
    dat$Class_Begin_Time %in% c(1010, 1140, 1310, 1810))
table(dat$Class_Days_Code[dat$popular_time])
table(dat$Class_Days_Code[!dat$popular_time])
enrollment <- dat[['Student_Enrollment_Count...14']]
capacity <- dat$Seating_Capacity_Count

for(pop in c(TRUE, FALSE)){
    condition <- dat$popular_time == pop
    temp_enroll <- enrollment[condition]
    temp_cap <- capacity[condition]
    enroll_cats <- cut(temp_enroll, seq(0, 600, 20), include.lowest=FALSE)
    cap_cats <- cut(temp_cap, seq(0, 600, 20), include.lowest=FALSE)
    temp_dat <- data.frame(enrollment=enroll_cats, capacity=cap_cats)
    temp_sum <- aggregate(rep(1, nrow(temp_dat)), temp_dat[1], sum, drop=FALSE)
    png(paste0("populartime_", pop,"_enroll_hist.png"), 1200, 400)
    myplot <- ggplot(temp_sum, aes(x=enrollment, y=x)) + geom_bar(stat="identity") +
        ggtitle(paste0("Is Popular: ", pop)) + scale_y_continuous(limits=c(0, 50))
    print(myplot)
    dev.off()
}

dat[enrollment > 500, c("Course_Number", "Office_Long_Name...9", "Class_Days_Code", "Class_Begin_Time")]
