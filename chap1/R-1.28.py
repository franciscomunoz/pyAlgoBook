#!/usr/bin/python

def norm(v,p):
	theNorm = 0
	for i in v:
		theNorm+=i**p
	return theNorm**(1/p)

def norm(v):
	theNorm = 0
	for i in v:
		theNorm+=i**2
	return theNorm**(1/2)
	
