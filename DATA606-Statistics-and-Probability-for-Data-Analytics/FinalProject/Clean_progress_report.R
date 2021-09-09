## Script to clean the school_progress_report

# Load some packages beforehand
if (!require(plyr)) install.packages('plyr')
if (!require(dplyr)) install.packages('dplyr')

clean_school_progress_report <- function(datasetReport){
# remove 'Under Review' row(s)
clean_report <- datasetReport %>% filter(GRADE != 'Under Review')

#Let's also convert the scores to a numerical value instead of a string for 
#better computation and plotting

clean_report$ENVIRONMENT.CATEGORY.SCORE <- 
  as.numeric(as.character(clean_report$ENVIRONMENT.CATEGORY.SCORE))

clean_report$PERFORMANCE.CATEGORY.SCORE <- 
  as.numeric(as.character(clean_report$PERFORMANCE.CATEGORY.SCORE))

clean_report$PROGRESS.CATEGORY.SCORE <- 
  as.numeric(as.character(clean_report$PROGRESS.CATEGORY.SCORE))

clean_report$OVERALL.SCORE <- 
  as.numeric(as.character(clean_report$OVERALL.SCORE))

# now convert the DBN values to meaningful borough names
# borough abbreviations
borough_abbr <- c('M', 'X', 'Q', 'K', 'R')

# extract the 3rd character in the DBN column
clean_report$DBN <- substr(clean_report$DBN, 3, 3)

# map abbreviations to the actual Borough Name
borough <- c("Manhattan", "Bronx", "Queens", "Brooklyn", "Staten Island")
clean_report$DBN <- mapvalues(clean_report$DBN, from = borough_abbr, to = borough)

# Extract columns what we need
clean_report <- clean_report %>%
  select(c("DBN", "SCHOOL.LEVEL.", "GRADE", "OVERALL.SCORE",
           "ENVIRONMENT.CATEGORY.SCORE", "PERFORMANCE.CATEGORY.SCORE",
           "PROGRESS.CATEGORY.SCORE", "QUALITY.REVIEW.SCORE"))

# rename some columns
colnames(clean_report) <- c("Borough", "School_Level", "Grade", 
                                       "Overall_Score", "Environment_Score",
                                       "Performance_Score", "Progress_Score",
                                       "Quality_Review_Score")

# Ensure the Borough is converted for proper summary
clean_report$Borough <- as.factor(clean_report$Borough)
return(clean_report)
}