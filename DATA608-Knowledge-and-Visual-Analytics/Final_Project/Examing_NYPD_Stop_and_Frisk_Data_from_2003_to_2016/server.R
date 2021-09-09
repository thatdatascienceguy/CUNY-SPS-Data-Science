library(shiny)
if (!require(shiny)) install.packages("shiny")
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(data.table)) install.packages("data.table")
if (!require(dplyr)) install.packages("dplyr")
#if (!require(tabplot)) install.packages(("tabplot"))


shinyServer(function(input, output) {
  
   # do a ggplot where x is the year and the y variable is determinted after
  # selecting a year
  
  
  output$NYPD_plot <- renderPlot({
    yr <- input$year
    nypd_stat <- input$statistic
    result <- NYPD %>% filter(year == yr)
    ggplot(result, aes(x = year)) +
      geom_bar() +
      facet_wrap(nypd_stat)
  })
})

