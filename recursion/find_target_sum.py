#!/usr/bin/env python 
import itertools 


def check_if_sum_possible(arr, k):
	subset_list = findsubsets(arr)
	print (subset_list)
	return doesListhasTarget(subset_list,k)
  
def findsubsets(s):    
	subset_list=[]
	for i in range(0, len(s)+1): # why the +1 
		subset_list.append(list(itertools.combinations(s,i)))
	    #print (list(itertools.combinations(s,i)))
	return subset_list

def doesListhasTarget(l, t):
	for l_list in l:
		for tuple_item in l_list:
			v=0
			for item in tuple_item:
				print (tuple_item)
				v+=item
				if v==t:
					print(True)
					return 1
	print (False)				
	return 0

# Driver Code 
s = [-10,10]
t = 0
check_if_sum_possible(s,t)


