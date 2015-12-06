#!/usr/bin/python

def sum(a,b):
	return a + b

def sub(a,b):
	return a - b

a=int(input())
operator = (raw_input())
b=int(input())

if operator == "+":
	c = sum(a,b)
	print("The sum is " + str(c))
elif operatpr == "-":
	c = sub(a,b)
	print("The difference is " + str(c))
else:
	print("No operator")
