# 2.10.3

## a) 
library(readxl)
library(quantmod)
library(fma)
library(fpp2)
setwd("C:/Users/neil.hwang/Downloads")
retaildata <- readxl::read_excel("retail.xlsx", skip=1)

## b)
### Browse through all the columns to decide which one to select for analysis
head(retaildata)
names(retaildata)
myts <- ts(retaildata[,"A3349335T"],frequency=12, start=c(1982,4))

## c)
### autoplot(), ggseasonplot(), ggsubseriesplot(), gglagplot(), ggAcf()
### seasonality, cyclicity and trend? What do you learn about the series?
### First, install and call into scope necessary libraries. Specifically, I install {ggfortify}
###  since {ggfortify} let {ggplot2} know how to interpret ts objects. Also, {zoo} is a dependency.
library(ggplot2)
library(ggfortify)
library(zoo)
autoplot(myts) + ggtitle("Total Turnover for A3349335T") + 
  theme(plot.title = element_text(hjust = 0.5)) + # to center the plot title
  xlab("Month_Year") +
  ylab("Total_Sales in A$'000s")

library(forecast) #for ggseasonplot()
ggseasonplot(myts, year.labels=TRUE, year.labels.left=TRUE) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title
  ylab("Total_Sales in A$'000s by Year") +
  ggtitle("Seasonal plot: Total Turnover for A3349335T")

ggsubseriesplot(myts) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title+
  ylab("Total_Sales in A$'000s") +
  ggtitle("Seasonal subseries plot: Total Turnover for A3349335T")

### start with year 1983 since that is the first year with the full available data
myts2 <- window(myts, start=1983)
gglagplot(myts2)

ggAcf(myts2)


# 2.10.7
head(arrivals)
myts <- ts(arrivals,frequency=4, start=c(1981,1))
autoplot(myts) + ggtitle("Arrivals by Source Country") + 
  theme(plot.title = element_text(hjust = 0.5)) + # to center the plot title
  xlab("Year") +
  ylab("Arrivals in thousands")

ggseasonplot(myts[,1], year.labels=TRUE, year.labels.left=TRUE) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal plot: Quarterly Arrivals from Japan")

ggseasonplot(myts[,2], year.labels=TRUE, year.labels.left=TRUE) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal plot: Quarterly Arrivals from New Zealand")

ggseasonplot(myts[,3], year.labels=TRUE, year.labels.left=TRUE) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal plot: Quarterly Arrivals from U.K.")

ggseasonplot(myts[,4], year.labels=TRUE, year.labels.left=TRUE) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal plot: Quarterly Arrivals from U.S.")


ggsubseriesplot(myts[,1]) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title+
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal subseries plot: Japan")

ggsubseriesplot(myts[,2]) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title+
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal subseries plot: New Zealand")

ggsubseriesplot(myts[,3]) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title+
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal subseries plot: U.K.")

ggsubseriesplot(myts[,4]) +
  theme(plot.title = element_text(hjust = 0.5)) +  # to center the plot title+
  ylab("Arrivals in thousands") +
  ggtitle("Seasonal subseries plot: U.S.")


#2.10
head(dj)
ddj <- diff(dj)
autoplot(ddj) + ggtitle("Daily Changes in Dow Jones Index") + 
  theme(plot.title = element_text(hjust = 0.5)) + # to center the plot title
  xlab("292 Consecutive Trading Days") +
  ylab("Daily Changes in %")

ggAcf(ddj)


#3.1.
## usnetelec
library(gridExtra) #for grid.arrange
p1 <- autoplot(usnetelec)
(lambda <- BoxCox.lambda(usnetelec))
p2 <- autoplot(BoxCox(usnetelec,lambda))
grid.arrange(p1, p2, nrow = 1)

## usgdp
p1 <- autoplot(usgdp)
(lambda <- BoxCox.lambda(usgdp))
p2 <- autoplot(BoxCox(usgdp,lambda))
grid.arrange(p1, p2, nrow = 1)

## mcopper
p1 <- autoplot(mcopper)
(lambda <- BoxCox.lambda(mcopper))
p2 <- autoplot(BoxCox(mcopper,lambda))
grid.arrange(p1, p2, nrow = 1)

## enplanements
p1 <- autoplot(enplanements)
(lambda <- BoxCox.lambda(enplanements))
p2 <- autoplot(BoxCox(enplanements,lambda))
grid.arrange(p1, p2, nrow = 1)

#Problem 3.8
## a) Split the data from 2.10.3 into two parts using
myts <- ts(retaildata[,"A3349335T"],frequency=12, start=c(1982,4))
myts.train <- window(myts, end=c(2010,12))
myts.test <- window(myts, start=2011)

## b) Check that your data have been split appropriately by producing the following plot.
autoplot(myts) +
  autolayer(myts.train, series="Training") +
  autolayer(myts.test, series="Test")
fc <- snaive(myts.train)
accuracy(fc,myts.test)
checkresiduals(fc)
