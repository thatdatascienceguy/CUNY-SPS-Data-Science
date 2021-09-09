# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:20:09 2017

@author: Jonathan Hernandez

This is a program that gets data from the UCI Machine Learning
Repository: https://archive.ics.uci.edu/ml/datasets/Car+Evaluation

And retrieves 

- The top 10 cars sorted by Safety,
- The 15 most low maintenance cars
- All vehicles that have a high or very high rating on
  Maintenance, Safety and Buying sorted by # of doors
- All cars that are very expensive, medium maintenance, 4-door and can
- hold 4 or more people and saves that to a .txt file.

- The data should be downloaded and the program has a file open dialog 
  that you can search your downloaded file to begin.
"""

from Tkinter import Tk
from tkFileDialog import askopenfilename
import pandas as pd
import numpy as np
import sys

def getData():
    'Method to get the csv file by opening a file dialog box and uses the'
    'Pandas library to read the csv file, changes the column names and creates'
    'ordering for safety and maintenance.'
    Tk().withdraw()
    filename = askopenfilename()
    
    carsData = pd.read_csv(filename, header=None)
    # determine if all the data is "correct" and not properly categorized
    # create a dictionary of valid values that should be allowed in each
    # column
    # Set Column Names for better referencing
    carsData.columns = ['buying', 'maint', 'doors',
                        'persons', 'lug_boot', 'safety', 'class']
    
    # Set categorical variables for proper sorting and order
    carsData['safety'] = pd.Categorical(carsData['safety'],
                                        ["low", "med", "high"])
    carsData['maint'] = pd.Categorical(carsData['maint'],
                                        ["vhigh", "high", "med", "low"])
    return carsData
    
def _validData(data):
    'Function that checks if there are any bad in the dataset'
    
    valid_cars_data = {'buying': ['vhigh', 'high', 'med', 'low'],
                       'maint': ['vhigh', 'high', 'med', 'low'],
                        'doors': ['2', '3', '4', '5more'],
                        'persons': ['2', '4', 'more'],
                        'lug_boot': ['small', 'med', 'big'],
                        'safety': ['low', 'med', 'high'],
                        'class': ['unacc', 'acc', 'good', 'vgood']}
    
    true_false_cars = pd.DataFrame()
    # make a dataaset of True/False values based on good or bad data
    for key in valid_cars_data:
        true_false_cars[key] = data[key].isin(valid_cars_data[key])
    
    # compute the total number of bad data
    return sum(np.apply_along_axis(np.sum, 0, true_false_cars==False))
    
def top10Safety(data):
    'Retrieve the top 10 cars in safety'
    return data.sort_values('safety', ascending=False).head(n=10)
    
def bottom15Maint(data):
    'Retrieve the 15 cars with the lowest maintenance'
    return data.sort_values('maint').tail(n=15)
    
def vhigh_or_high(data):
    'Retrieve all cars that have high or vight ratings when it comes to'
    'safety, maintenance and buying'
    # search list
    search_high = "(high|vhigh)"
    # use str.contains to search each column based on the regex search_high
    search_result = data[data['buying'].str.contains(search_high) &
                        data['maint'].str.extract(search_high) &
                        data['safety'].str.extract(search_high)]
    return search_result.sort_values('doors')

def searchCar(data):
    'Retrieve all cars that are vhigh in buying, medium maintenance, 4-door'
    'and can hold 4 people or more'
    search_list = ["vhigh", "med", "4", "(4|more)"]
    search_result = data[(data['buying'] == search_list[0]) &
                    (data['maint'] == search_list[1]) &
                    (data['doors'] == search_list[2]) &
                    (data['persons'].str.extract(search_list[3]))]
    return search_result

if __name__ == "__main__":
    cdata = getData()
    # If there is at least 1 piece of data that is false or not valid exit
    if(_validData(cdata) != 0):
        print "There exists bad data in the dataset, please correct and re-run"
        sys.exit()
    
    print "Top 10 cars sorted by safety in descending order\n"
    print top10Safety(cdata)
    print 
    
    print "Bottom 15 cars sorted by maintenance\n"
    print bottom15Maint(cdata)
    print 
    
    print "Vechicles that are high or vhigh in Buying,"
    print "maintenance and 4 doors or more \n"
    print vhigh_or_high(cdata)
    
    print "Saving data containing vehicles such that the price is very high"
    print "okay maintenance, 4 door and is for 4 people or more"
    x = searchCar(cdata)
    x.to_csv('output.csv', index=False)
    