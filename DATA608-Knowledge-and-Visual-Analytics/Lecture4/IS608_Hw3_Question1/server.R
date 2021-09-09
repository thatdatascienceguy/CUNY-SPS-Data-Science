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

# get data from 2010 only
mortality_US_2010 <- mortality_US %>% filter(Year == "2010") %>%
  select(Cause_Of_Death, State, Crude_Mortality_Rate)

shinyServer(function(input, output, session) {
  
  # input will be the cause of death and output will be the graph of
  # State vs Crude Mortality Rate
  
  output$distPlot <- renderPlot({
    # dataset will change based on input of cause of death (cod)
    causeofdeath <- mortality_US_2010 %>% 
      filter(Cause_Of_Death == input$cod) %>%
      arrange(Crude_Mortality_Rate)
    
    # plot based on input, use reorder to order x axis in specified order
    ggplot(data = causeofdeath, aes(x = reorder(State, -Crude_Mortality_Rate),
                                    y = Crude_Mortality_Rate)) +
    geom_bar(stat = "summary", fun.y = "sum") +
    theme_bw() +
    theme(panel.border = element_blank(), panel.background = element_blank(),
          panel.grid = element_blank(), axis.title.x = element_blank(),
          axis.title.y = element_blank())
  })
})
