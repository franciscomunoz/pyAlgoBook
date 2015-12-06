#!/usr/bin/python

def sumPreviousEven(n):
	the_list = [i for i in range(0,n) if i & 1 == 0]
	for i in range(len(the_list)):
		if i > 0:
			the_list[i] = the_list[i]+the_list[i-1]
	print the_list



def myGenerator(the_list):
	for i in range(len(the_list)):
		if i > 0 :
			the_list[i] = the_list[i] + the_list[i-1]
			yield the_list[i]
		else:
			yield 0;
			

#Using a function
sumPreviousEven(15)
#Using a generator
the_list = [i for i in range(0,15) if i & 1 == 0]
final_list = [ i for i in myGenerator(the_list)]

print(final_list)
