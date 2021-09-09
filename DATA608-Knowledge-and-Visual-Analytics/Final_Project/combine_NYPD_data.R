# preprocess data (one time only)
# Script combines all data from 2003 to 2016, puts them into a list of datasets
# and keeps only the main attributes as well as what they have in common.

if (!require("data.table")) install.packages("data.table")
if (!require("dplyr")) install.packages("dplyr")
if (!require("plyr")) install.packages("plyr")

# get data (all *.csv files from current directory)

NYPD_files <- list.files(pattern = "*.csv")
# NYPD_data <- lapply(NYPD_files, fread, sep = ",", header = TRUE, fill = TRUE)

# dataset all together is over 3-4 GB lets get some columns to graph and do EDA
# grab columns that are most important save to a one time file
# file will be used in shiny app and for rest of project

data_to_select <-c("year", "pct", "ser_num", "datestop", "timestop", "explnstp",
                   "crimsusp", "othpers", "arstmade", "sumissue",
                   "frisked", "searched", "sex", "race", "dob", "age", 
                   "city", "state", "zip", "xcoord", "ycoord", "rf_furt", "rf_bulg",
                   "sb_hdobj", "sb_outln", "sb_admis", "sb_other", 
                   "pf_hands", "pf_wall", "pf_grnd", "pf_drwep", "pf_ptwep", "pf_baton",
                   "pf_hcuff", "pf_pepsp", "pf_other")

# for each NYPD dataset get the columns below and then combine them into one
NYPD_data <- list()
data_2003 <- fread(NYPD_files[1], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2004 <- fread(NYPD_files[2], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2005 <- fread(NYPD_files[3], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2006 <- fread(NYPD_files[4], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2007 <- fread(NYPD_files[5], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2008 <- fread(NYPD_files[6], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2009 <- fread(NYPD_files[7], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2010 <- fread(NYPD_files[8], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2011 <- fread(NYPD_files[9], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2012 <- fread(NYPD_files[10], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2013 <- fread(NYPD_files[11], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2014 <- fread(NYPD_files[12], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2015 <- fread(NYPD_files[13], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)
data_2016 <- fread(NYPD_files[14], sep = ",", fill = TRUE, select = data_to_select, header = TRUE)

NYPD_data <- list(data_2003,data_2004, data_2005, data_2006, data_2007, data_2008,
                  data_2009, data_2010, data_2011, data_2012, data_2013, data_2014,
                  data_2015, data_2016)

NYPD_data <- rbindlist(NYPD_data)
fwrite(NYPD_data,"NYPD_data.csv")