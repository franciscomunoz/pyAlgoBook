"""Implement a function that randomly moves elements in an array in the same
    way the shuffle method works. The implementation just swaps using randrange"""

import random

def myshuffle(data):
    l = len(data)
    for i in range(l):
        r = random.randrange(l)
        data[i], data[r] = data[r],data[i]
    return data

if __name__ == '__main__':

    tests = []
    tests.append([4,3,5,6,7,8,9,3,4,5,6,1,10])
    tests.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    tests.append([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])


    for i in range(len(tests)):
        print("Shuffling test {0} with myshuffle is : {1}"\
                .format(i,myshuffle(tests[i])))
