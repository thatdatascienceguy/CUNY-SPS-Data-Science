# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:26:03 2017

@author: jonboy1987
"""

import pandas as pd
from Tkinter import Tk
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt

def plot_cars_data():
    Tk().withdraw()
    filename = askopenfilename()
    
    # Read in the dataset
    cars = pd.read_csv(filename, header=None)
    cars.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot',
                    'safety', 'class']
   
    # plot a histogram of buying, maint, safety and doors a 2x2 plot 
    cars.plot(by=['buying','safety'])
    
    
if __name__ == "__main__":
    car = plot_cars_data()
    print car