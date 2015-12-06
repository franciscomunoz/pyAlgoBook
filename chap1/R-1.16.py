#!/usr/bin/python

def scale(data,factor):
	print id(data)
	for i in range(len(data)):
		data[i] *= factor
	data = [];
	print id(data)
	
values = [1,2,3,4,5]
print id(values)
scale(values,2)
print values

