#!/usr/bin/env python 
import itertools 
  
def findsubsets(s):    
    subset_list=[]
    for i in range(0, len(s)):
        subset_list.append(list(itertools.combinations(s,i)))
        #print (list(itertools.combinations(s,i)))
    print (subset_list)
# Driver Code 
s = {1, 2, 3, 4} 
findsubsets(s)