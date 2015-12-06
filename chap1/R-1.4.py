#!/usr/bin/python

def sumOfSqrts(n):
	n = range(0,n)
	sum = 0
	for i in n:
		print(i)
		sum += i*i
	return sum
value = int(input("Enter a value to sum its squares : "))
x = sumOfSqrts(value)
print("The value of the sum of squares is : {0}".format(x))
