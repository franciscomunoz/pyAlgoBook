
def countDivideByTwo(number):
	if number/2 < 2:
		return 0

	return countDivideByTwo(number/2) + 1


count = countDivideByTwo(10)

print count


