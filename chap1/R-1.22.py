#!/usr/bin/python


def dotProduct(vectora,vectorb):
	if len(vectora) != len(vectorb):
		ValueError("Vector length mismatch")
	else:
		product = [0] * len(vectora)
		for i in range(len(vectora)):
			product[i]=vectora[i] * vectorb[i]
	return product

vectora = [1,2,3,4,5]
vectorb = [6,7,8,9,10]

product = dotProduct(vectora,vectorb)

print("The dot product between " + str(vectora) + " and " + str(vectorb) + " is "\
				+ str(product))
