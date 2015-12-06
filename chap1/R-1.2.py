#!/usr/bin/python

def is_even(k):
	
	if k & 1 == 0 :
		return True
	return False
x = 10
print(" The number {0} is even ? : {1}".format(x,is_even(x)))
