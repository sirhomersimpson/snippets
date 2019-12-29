#!/usr/bin/env python 

#https://leetcode.com/problems/generate-parentheses/solution/
#Backtracking
#TC - Catalan number 4^n/sqrt(n)
#TS - Calalan number 4^n/sqrt(n)
def generate (N):
	ans = []
	def backtrack (S = '', left=0, right=0):
		if len(S) == 2*N:
			ans.append(S)
			return
		if left<N:
			backtrack(S+'(', left+1, right)
		if right < left:
			backtrack(S+')', left, right+1)
	
	backtrack()
	print (ans)
	return ans

generate(2)                                           