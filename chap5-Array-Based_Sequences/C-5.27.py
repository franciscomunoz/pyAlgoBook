"""Give a List L of n positive integers, each represented with 

            k = ceil(log(n)) +  1 bits

describe an O(n) method for finding a k-bit integer not in L """

import math

def find_missing_elements(data,n):
    k = math.ceil(math.log(n)) + 1
    test_array = [False] * int(math.pow(2,k))
    not_in_array = []

    for i in range(len(data)):
        if data[i] <= len(test_array) - 1 :
            test_array[data[i]] = True

    for i in range(len(data)):
        if test_array[i] == False:
            not_in_array.append(i)

    return not_in_array
            
if __name__ == '__main__':

    tests = []
    tests.append([3,5,6,7,8,2,1,0])
    tests.append([1,2,3,4,5,6,7,8,9])
    tests.append([2,4,6,8,10])

    for i in range(len(tests)):
        print("Test {0} : The elements missing in the array are : {1}".\
                format(i,find_missing_elements(tests[i],len(tests[i]))))
   
