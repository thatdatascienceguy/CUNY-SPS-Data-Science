#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    # For simplicity, using the Bubblesort algorithm 
    length = len(input)
    for i in range(length):
        for j in range(length-i-1):
            if (input[j] > input[j+1]): # swap
                input[j], input[j+1] = input[j+1], input[j]
                
    return input#return a value
	
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    # use a builtin sorting algorithm
    return sorted(input)#return a value

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    
    found = False 
    length = len(input)
    for i in range(length): # loop through all values
        if input[i] == value: # if found
            found = True
            break
        
    return found#return a value

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    # just use the in operator
    return value in input#return a value	

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
