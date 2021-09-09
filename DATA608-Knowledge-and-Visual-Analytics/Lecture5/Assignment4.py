# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:55:58 2017

@author: jonboy1987
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib2

""" Data Acquisition/retrieval section """
# read in the dataset of Enterococcus levels in the Hudson River
url = "https://raw.githubusercontent.com/charleyferrari/CUNY_DATA608/master/lecture4/Data/riverkeeper_data_2013.csv"
response = urllib2.urlopen(url)
enteroData = pd.read_csv(url)
# print out first few rows of dataset
print enteroData.head(n=15)
""" End of Data Acquistion/retrieval section """

"""Cleaning up process """
# EnteroCount attribute containes some '>' and '<' which i'm assuming it means greater and less than respectively
# remove those from the dataset and assume the number next to them
enteroData["EnteroCount"] = enteroData["EnteroCount"].str.replace("<|>", "")
# the values are all strings, lets make them numbers for calculation
enteroData["EnteroCount"] = enteroData["EnteroCount"].astype(int)
#print type(enteroData["EnteroCount"][100]) # test it out

#print type(enteroData["Date"][100]) # the date is a str and should be converted to date
enteroData["Date"] = pd.Series([pd.to_datetime(date) for date in enteroData["Date"]])

enteroData["FourDayRainTotal"] = enteroData["FourDayRainTotal"].astype(float)
enteroData["SampleCount"] = enteroData["SampleCount"].astype(int)
""" End of Cleaning up Process """

""" Graph and List best and worst places to swim"""
# filter out based on acceptance of EnteroCount and SampleCount
site_counts = enteroData.Site.value_counts().to_dict()

best_sites = enteroData[(enteroData.EnteroCount < 100) | (enteroData.SampleCount < 30)]
# get a updated count of Sites meeting this criteria
site_counts_updated = best_sites.Site.value_counts().to_dict()

# see which sites are the cleanest by comparing the two dictionaries using set operation
sites_clean = set(site_counts.items()) & set(site_counts_updated.items())
sites_clean = list(sites_clean) # convert to list
sites_clean = [x[0] for x in sites_clean] # get states
sites_clean = enteroData[enteroData.Site.isin(sites_clean)] # get updated data
sites_clean.Site.value_counts().plot(kind = 'bar', title = "Count of Best Sites to Have Best Water Quality on EnterCount and Sample Size") # plot


worst_sites = enteroData[(enteroData.EnteroCount > 100) | (enteroData.SampleCount > 30)]
# get a updated count of Sites meeting this criteria
site_counts_updated = worst_sites.Site.value_counts().to_dict()
# see which sites are the cleanest by comparing the two dictionaries using set operation