library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Mortality Rates across the U.S in 2010 for Given Cause of Deaths"),
  h3("Jonathan Hernandez IS 608 Fall 2017 Assignment #3 Question 1"),
  
  h4("Select a cause of death below which will display a graph to the right of"),
  h4("the screen Crude Mortality Rate vs State in order of Crude Mortality Rate"),
  
  sidebarPanel(
    selectInput('cod', "Cause of Death", unique(mortality_US_2010$ICD.Chapter))
    ),
  # Show a plot of the generated distribution
    mainPanel(
       plotOutput("distPlot")
    )
  )
)
