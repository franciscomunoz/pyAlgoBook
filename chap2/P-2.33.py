import pdb;
import re;

poly = input("Input the polynomial you want to find its derivative : ")

coefficients = re.split("x\^[+-]?[0-9]+",poly)
exponents = re.split("[+-]?[0-9]+x\^",poly)

#print(coefficients)
#print(exponents)

coefficients = [ i for i in coefficients if i !='']
exponents = [i for i in exponents if i !='']

#print(coefficients)
#print(exponents)

derivative=""
for i in range(len(coefficients)):
    print(coefficients[i])
    print(exponents[i])
    coefficient = int(coefficients[i])*int(exponents[i])
    exponent = int(exponents[i]) - 1
    sign = "+" if coefficient >= 0 else " "
    if exponent == 0:
        derivative += sign + str(coefficient)
    else:
        derivative += sign + str(coefficient) + "x^" + str(exponent)

print("The original value is {0}".format(poly))
print("The derivative is {0}".format(derivative))
