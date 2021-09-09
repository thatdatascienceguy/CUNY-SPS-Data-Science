# -*- coding: utf-8 -*-
"""
@author: jonboy1987

Program to show the time it takes to use searching and sorting using
Numpy built-in sort/search functions
Python's own builtin sort/search functions
user made iteration sorting/searching using loops

for each test, 500 random numbers from 0,1000 are generated through 10000 itreations (tests)
"""
import timeit
setup = '''
import numpy as np
# Sorting functions

# Numpy Sorting
def numpy_sort(lst):
    return np.sort(lst)

# sorting with loops (bubblesort)
def sortwithloops(input):
    # For simplicity, using the Bubblesort algorithm 
    length = len(input)
    for i in range(length):
        for j in range(length-i-1):
            if (input[j] > input[j+1]): # swap
                input[j], input[j+1] = input[j+1], input[j]
                
    return input #return a value
	
# Built-in python sorted function
def sortwithoutloops(input):
    return sorted(input)#return a value

# Searching functions

# Numpy Searching
def numpy_search(lst, value):
    return np.any(lst[:] == value)
    
# Searching using iteration (linear searching)
def searchwithloops(input, value):
    found = False 
    length = len(input)
    for i in range(length): # loop through all values
        if input[i] == value: # if found
            found = True
            break
        
    return found #return a value

def searchwithoutloops(input, value):
    # just use the in operator
    return value in input #return a value

'''
if "__main__" == __name__:
    # check out timings of numpy sorting, python built in sorting and iteration sorting
    
    n = 10000 # number of iterations
    t_numpy_sort = timeit.Timer("L = [np.random.randint(0,1000) for r in xrange(500)]; numpy_sort(L)", 
                                      setup = setup)
    print "Numpy Sorting with 1000 iterations of 500 numbers: ", t_numpy_sort.timeit(n)
    
    t_builtin_sort = timeit.Timer("L= [np.random.randint(0,1000) for r in xrange(500)]; sortwithoutloops(L)",
                                       setup = setup)
    print "Builtin Python Sorting with 1000 iterations of 500 numbers: ", t_builtin_sort.timeit(n)
    
    t_iteration_sort = timeit.Timer("L=[np.random.randint(0,1000) for r in xrange(500)]; sortwithloops(L)", 
                                    setup = setup)
    print "Iteration Sorting with 1000 iterations of 500 numbers: ", t_iteration_sort.timeit(n)
    
    
    # Now test with searching methods
    t_numpy_search = timeit.Timer("L = [np.random.randint(0,1000) for r in xrange(500)]; numpy_search(L, 29)", 
                                      setup = setup)
    print "Numpy Searching with 1000 iterations of 500 numbers: ", t_numpy_search.timeit(n)
    
    t_builtin_search = timeit.Timer("L = [np.random.randint(0,1000) for r in xrange(500)]; searchwithoutloops(L, 29)", 
                                      setup = setup)
    print "Builtin Searching with 1000 iterations of 500 numbers: ", t_builtin_search.timeit(n)
    
    t_iteration_search = timeit.Timer("L = [np.random.randint(0,1000) for r in xrange(500)]; searchwithloops(L, 29)", 
                                      setup = setup)
    print "Iteration Searching with 1000 iterations of 500 numbers: ", t_iteration_search.timeit(n)
