library(shiny)

shinyUI(fluidPage(
  
  # Application title
  titlePanel("Mortality Rates across the U.S in for Given Cause of Deaths for a particular year"),
  h3("Jonathan Hernandez IS 608 Fall 2017 Assignment #3 Question 1"),
  
  h4("Select a cause of death below which will display a graph to the right of"),
  h4("the screen Crude Mortality Rate vs State in order of Crude Mortality Rate"),
  h4("The graph will also show a horizontal red line indicating the average mortality rate"),
  h4("for a given year."),
  h4("This shows which states for a partcular cause of death have maintained lower or higher"),
  h4("mortality rates."),
  
  sidebarPanel(
    selectInput('cod', "Cause of Death", unique(mortality_US_2010$ICD.Chapter)),
    selectInput('year', "Year", unique(mortality_US$Year))
  ),
  # Show a plot of the generated distribution
  mainPanel(
    plotOutput("distPlot")
  )
))