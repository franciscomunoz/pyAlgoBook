#!/usr/bin/python
import random
def myshuffle(data):
	for i in range(len(data)):
		r =	random.randint(0,len(data)-1)
		data[i],data[r] = data[r],data[i]


list = [1,2,3,4,5,6,7,8,9,10]

myshuffle(list)
print list
	
