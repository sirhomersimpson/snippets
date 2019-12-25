#!/usr/bin/env python 
from itertools import permutations

## Python program to print all permutations with 
## Below are the permutations of string ABC.a
##  ABC ACB BAC BCA CBA CAB
def toString (str):
  return ''.join(str)

### Ref: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string
### Use recursion
def permute(a, l, r): 
    if l==r: 
        print(toString(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack

#https://www.tutorialspoint.com/How-to-find-all-possible-permutations-of-a-given-string-in-Python
def permute_inbuilt(s):
	for p in permutations(s):
		print ("".join(p))

### Testing ...
string = "abc"
length_string = len(string) 
str_list = list(string)

print("using recursive:")
permute(str_list, 0, length_string-1)

print("using inbuilt itertools permutations:")
permute_inbuilt(string)