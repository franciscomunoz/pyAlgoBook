#!/usr/bin/python

def pairProductOdd(data):
	for i in data:
		for j in data:
			if i * j & 1 != 0:
				print("The product {0} and {1} are odd".format(i,j))

data  = [2,3,4,4,5,3,3,5,8,9,10]
pairProductOdd(data)
				
