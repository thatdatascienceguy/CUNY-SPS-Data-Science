library(data.table)
library(dplyr)
NYPD <- fread("NYPD_data.csv")
NYPD <- NYPD %>% select(-c(state)) # just NA values, can be omitted
# besides you are looking at NYC only
NYPD$year <- as.character(NYPD$year) # convert to character instead of integer
#NYPD$datestop <- as.Date(NYPD$datestop, "%m/%d/%Y")