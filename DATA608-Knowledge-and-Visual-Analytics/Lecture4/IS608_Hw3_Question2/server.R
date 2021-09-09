if (!require(shiny)) install.packages("shiny")
if (!require(RCurl)) install.packages("RCurl")
if (!require(dplyr)) install.packages("dplyr")
if (!require(ggplot2)) install.packages("ggplot2")

# read data to start off from web
mortality_US_URL <- getURL("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA608/master/lecture3/data/cleaned-cdc-mortality-1999-2010-2.csv")

mortality_US <- read.csv(textConnection(mortality_US_URL), header = TRUE)

# alter Some Columns for better Data Reading
colnames(mortality_US)[1] <- "Cause_Of_Death"
colnames(mortality_US)[6] <- "Crude_Mortality_Rate"


shinyServer(function(input, output, session) {
   
  output$distPlot <- renderPlot({
    cod_state <- mortality_US %>% filter(Cause_Of_Death == input$cod,
                                         Year == input$year)
    
    # calculate the national average mortality rate for a particular year
    national_avg_MR <- mean(cod_state$Crude_Mortality_Rate)
    
    ggplot(data = cod_state, aes(x = State, y = Crude_Mortality_Rate)) +
      geom_bar(stat = "summary", fun.y = "sum") +
      # draw red line indicating national average for a particular year
      geom_hline(aes(yintercept = national_avg_MR), color = "red") +
      theme_bw() +
      theme(panel.border = element_blank(), panel.background = element_blank(),
            panel.grid = element_blank(), axis.title.x = element_blank(),
            axis.title.y = element_blank())
  })
  
})
