#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Examing NYPD Stop and Frisk Data from 2003 to 2016"),
  h3("Author: Jonathan Hernandez"),
  h3("Email: jayhernandez1987@gmail.com"),
  h3("Github: https://github.com/jonathan1987"),
  h3("Source of NYPD data for this application:"),
  h5(a("NYPD Website for dataset",
       href = "http://www1.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page",
       target = "_blank")),
  br(),
  h4("This Shiny application is to show and examine stop and frisk activities."),
  h4("In this app, as a simple example and perhaps to be modified even better"),
  h4("you can select a specified year or multiple years and select different statistics"),
  
  # input year and input type of statistic to look up
  sidebarLayout(
    checkboxGroupInput("year", "Year", choices = unique(NYPD$year), selected = 2003),
    
    selectInput("statistic", "Select what statistic you'd like to view",
                 choices = c("explnstp", "othpers", "arstmade", "sumissue",
                             "frisked", "searched", "sex", "race", "rf_furt", "rf_bulg",
                             "sb_hdobj", "sb_outln", "sb_admis", "sb_other", 
                             "pf_hands", "pf_wall", "pf_grnd", "pf_drwep", 
                             "pf_ptwep", "pf_baton", "pf_hcuff", "pf_pepsp", "pf_other"))),
    
    # show ggplot of statistic
    mainPanel(
       plotOutput("NYPD_plot")
    )
  )
)