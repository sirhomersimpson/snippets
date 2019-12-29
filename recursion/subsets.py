#!/usr/bin/env python 
import itertools 
  
# using itertools
def findsubsets(s):    
    subset_list=[]
    for i in range(0, len(s)):
        subset_list.append(list(itertools.combinations(s,i)))
        #print (list(itertools.combinations(s,i)))
    print (subset_list)


#using recursive 
## https://www.youtube.com/watch?v=bGC2fNALbNU
def all_subsets(given_array):
    subset = [None]* len(given_array)
    _all_subsets(given_array, subset, 0)

def _all_subsets (given_array, subset, i):
    if i == len(given_array):
        print_pretty(subset)
    else:
        subset[i] = None
        _all_subsets(given_array, subset, i+1)
        subset[i] = given_array[i]
        _all_subsets(given_array, subset, i+1)

def print_pretty(s):
    l = []
    for item in s:
        if item is not None:
            l.append(item)
    print (l)   

# Driver Code 
s = {1, 2, 3, 4} 
print ("from itertools combinations")
findsubsets(s)
print ("from some magical recursiveness...")
all_subsets([1,2,3])
