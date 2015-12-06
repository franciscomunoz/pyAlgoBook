#!/usr/bin/python

def myreverse(str):
	strLength = len(str)-1
	for i in range(0,strLength/2):
		list[i], list[strLength-i] = list[strLength-i], list[i]
list=[]
allReversed = []
while(1):
	try:
		str = raw_input("Type the input string to be reversed : ")
		for i in str:
			list.append(i)
		myreverse(list)
		allReversed.append(list)
	except EOFError:
		print(list)
		break;




