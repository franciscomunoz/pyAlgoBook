#!/usr/bin/python

n = int(input("Type the number for the odd squared sum : "))
value = sum([i*i for i in range(0,n) if i & 1 != 0])
print("The sum is : " + str(value))
