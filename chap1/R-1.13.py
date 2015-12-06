#!/usr/bin/python

def myReverse(data):
	originalLength = len(data)
	dataLength = len(data[0:originalLength/2])
	for i in range(0,dataLength):
		data[i],data[originalLength-1-i] = data[originalLength-1-i],data[i]
	return data
values = [2,3,4,7,6,5]

data = myReverse(values)
print(data)
		
