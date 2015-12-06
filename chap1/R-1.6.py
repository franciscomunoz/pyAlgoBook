#!/usr/bin/python

def sumOddSqrts(n):
	sum = 0;
	for i in range(0,n):
		if i & 1 != 0:
			sum += i*i
	return sum

value = int(input("Type the number you want to find the odd squared sum : "))
print("The  odd squared sum is : " + str(sumOddSqrts(value)))
