#!/usr/bin/env python 
from itertools import permutations

## Python program to print all permutations with 
## Below are the permutations of string ABC.a
##  ABC ACB BAC BCA CBA CAB
def permute (s):
    return _permute(s, 0)

def _permute (s, index):
    if index==len(s)-1:
        print("".join(s))
    else:
        for i in range (index, len(s)):
            s[index], s[i] = s[i], s[index]
            _permute(s, index+1)    
            # backtrack
            
            s[index], s[i] = s[i], s[index] 

#https://www.tutorialspoint.com/How-to-find-all-possible-permutations-of-a-given-string-in-Python
def permute_inbuilt(s):
	for p in permutations(s):
		print ("".join(p))

### Testing ...
str = "abc"
print ("using recursive approach")
permute(list(str))

print("using inbuilt itertools permutations:")
permute_inbuilt(str)