#!/usr/bin/python

def is_multiple(n,m):

	if n%m == 0:
		return True
	return False

x = 10
y =  5
z = is_multiple(x,y)
print("Calling is_multiple with x = {0}, y = {1} gives : {2}".format(x,y,z ))
