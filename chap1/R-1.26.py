#!/usr/bin/python

def canBeUsedInFormula(a_in,b_in,c_in):
	if a_in + b_in == c_in:
		print("c = a + b")
	elif a_in == b_in -  c_in:
		print("a = b - c")
	elif a_in * b_in == c_in:
		print("a * b = c")
	else:
		print("The combination of a,b, and c cannot be used in any of the formulas")
	
canBeUsedInFormula(5,3,8)

canBeUsedInFormula(3,2,5)
