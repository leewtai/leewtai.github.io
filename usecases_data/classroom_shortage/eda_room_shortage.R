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
enrollment <- dat$Student_Enrollment_Count...22
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
day_cnts <- table(dat$Class_Days_Code)
day_cnts[day_cnts > 10]

begin_cnts <- table(dat$Class_Begin_Time)
begin_cnts[begin_cnts > 10]

dat$Class_Days_Code %in% c("M", "T", "W", "TR", "F")
plot(1, 1, type="N", xlim=c(0, 7),
     ylim=c(0,2400))
for(i in seq_len(nrow(dat)){
    days <- strsplit(dat$Class_Days_Code[i], "")[[1]]
    ybottom <- dat$Class_Begin_Time[i]
    ytop <- dat$Class_End_Time[i]

}

# 202003 + 20211 both have fewer than 20 (COVID)
table(dat$Term_Identifier, dat$Term_Calendar_Year)
table(dat$Term_Identifier, dat$Term_Code)
table(dat$Building_Name, dat$Class_Building_Code)
table(dat$Building_Name, dat$Class_Room_Code)

dat %>% filter(Term_Identifier == 20203) %>%
    select(Building_Name, Seating_Capacity_Count, Student_Enrollment_Count...22)
