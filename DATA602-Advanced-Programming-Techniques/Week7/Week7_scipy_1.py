# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:05:35 2017

@author: jonboy1987
"""

import timeit
setup='''
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

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

# using scipy/numpy


def func(x, a, b):
    return a * x + b
    
# Gaussian Fit
def gaussian(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))
    
brain_body = pd.read_csv("brainandbody.csv")
'''

if __name__ == "__main__":

    n = 100
    t_scipy_best_fit = timeit.Timer("parameters = curve_fit(func, brain_body.brain, brain_body.body);", 
                                      setup = setup)                
    print "Scipy best-fit with 100 iterations: ", t_scipy_best_fit.timeit(n)
    
    t_user_created_best_fit = timeit.Timer(
    "a, b = a_coefficent(brain_body.brain, brain_body.body), b_coefficent(brain_body.brain, brain_body.body);",
    setup = setup)
    print "User-Created best-fit with 100 iterations: ", t_user_created_best_fit.timeit(n)
    
    t_scipy_best_fit_gaussian = timeit.Timer(
    "parameters = curve_fit(gaussian, brain_body.brain, brain_body.body); print parameters[0]", 
                                      setup = setup)
    # the first 2 elements are the a and b parameters that fit the model and the last one is
    # the standard devivation that gives the best fit.
    print "Scipy best-fit using gaussian with 100 iterations: ", t_scipy_best_fit_gaussian.timeit(1)