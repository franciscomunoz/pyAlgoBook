#!/usr/bin/python

def removePunctuation(string):
	newString = ""
	for char in string:
		if char == "." or char == "," or char == "'":
			newString += ""
		else:
			newString += char
	return newString

string = "Let's try, Mike."

newString = removePunctuation(string)
print(newString)
