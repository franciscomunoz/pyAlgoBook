#!/usr/bin/python

value = int(input("Enter a value to sum its squares : "))

x = sum([i*i for i in range(0,value)])
print("The value of the sum of squares is : {0}".format(x))
