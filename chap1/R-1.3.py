#!/usr/bin/python

def minmax(data):
	values = ()
	min = data[0]
	max = data[0]
	for i in range(0,len(data)-1):
		if min < data[i+1]:
			max = data[i+1]
		else:
			min = data[i+1]
	return (min,max)

values = (2,1,3,6,10,22,40,35)
x = minmax(values)
print("Min and max values of tupple are : {0} , {1}".format(x[0],x[1]))
