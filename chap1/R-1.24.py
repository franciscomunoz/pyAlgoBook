#!/usr/bin/python

def countVowels(string):
	count = 0
	for letter in string:
		if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or\
			letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or\
			letter == 'u' or letter == 'U':
			count += 1
	return count

string = ("HIjo de la chIngada")
count = countVowels(string)
print("The number of vowels in " + string + " is " + str(count))
