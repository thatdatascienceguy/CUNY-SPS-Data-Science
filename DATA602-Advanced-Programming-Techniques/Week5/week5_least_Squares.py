# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:17:56 2017

@author: Jonathan Hernandez
@email: jayhernandez1987@gmail.com

Program to compute the least squares coefficients with the given dataset
brainandbody.csv. the goal is to find a and b such that

bo = b*br + a where 
bo = body weight and
br = brain weight
"""
import csv
import matplotlib.pyplot as plt

def a_coefficent(x,y):
    """ compute a which is defined as 
    sum(y)*sum(x^2) - sum(x*y) / n*sum(x^2) - (sum(x)^2)
    where n is the number of observations
    """
    
    if (len(x) != len(y)): # if the two variables don't have the same # of
    # columns, exit
        print "columns need to properly match to do least squares calculations"
        exit
    
    # compute a using sum, list comprehensions and the zip functions
    a = (sum(y)*sum([i**2 for i in x])) - (sum(x)*sum([i*j for i,j in zip(x,y)]))
    a = a / (len(x) * sum([i**2 for i in x]) - (sum(x)**2))
    return a

def b_coefficent(x,y):
    """ compute b which is defined as 
    n*sum(x*y) - sum(x)*sum(y) / n*sum(x^2) - (sum(x)^2)
    where n is the number of observations
    """
    
    if (len(x) != len(y)): # if the two variables don't have the same # of
        print "columns need to properly match to do least squares calculations"
        exit
    
    # compute a using sum, list comprehensions and the zip functions
    b = (len(x)*sum([i*j for i,j in zip(x,y)])) - (sum(x)*sum(y))
    b = b / (len(x) * sum([i**2 for i in x]) - (sum(x)**2))
    return b

if __name__ == "__main__":
    print """Computing the least squares given a dataset with two numerical values
    """
    brain, body = [], []
    
    # read the dataset line by line and get
    with open('brainandbody.csv', 'rb') as brain_and_body:
        reader = csv.reader(brain_and_body)
        for row in reader:
            brain.append(row[2]) # brain weights
            body.append(row[1]) # body weights
    brain_and_body.close()
    
    # convert to floats as the data is read as strings
    brain[1:] = list(map(float, brain[1:])) 
    body[1:] = list(map(float, body[1:]))  
    
    print "Computing coefficent a in bo=b*br+a:"
    a = a_coefficent(brain[1:], body[1:])
    print a
    
    print "Computing coefficent b in bo=b*br+a:"
    b = b_coefficent(brain[1:], body[1:])    
    print b
    
    print "least squares line that best fits the data: bo = ", round(b,3), "*br +", round(a,3)
    
    # plot the dataset
    plt.plot(brain[1:], body[1:], 'ro')
    
    # draw the least-squares line i blue
    least_squares_line = [b * x + a for x in brain[1:]]
    plt.plot(brain[1:], least_squares_line, 'b--')