#!/usr/bin/python
import random

def mychoice(values):
	randomIndex = random.randrange(0,len(values))
	return values[randomIndex]


myValues = [2,4,5,1,8,9,7,0]


print("Calling mychoice func for a random index gives "+str(mychoice(myValues)))

