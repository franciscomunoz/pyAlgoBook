#!/usr/bin/python

def repeatedElements(data):
	dataLen = len(data)
	for i in range(0,dataLen):
		for j in range(0,dataLen):
			if i != j:
				if data[i] == data[j]:
					print("Index {0} and {1} repeat is value with {2}".format(i,j,data[i]))


values = (4,3,5,67,8,8,2,4,5)
repeatedElements(values)
