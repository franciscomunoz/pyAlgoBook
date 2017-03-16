"""This short program illustrates the amount of microseconds required for 
inserting elements in the beginning, middle and end of a list"""

import sys                              # provides getsizeof function
from time import time


if __name__ == '__main__':

    tests = []
    tests.append([0]*100)
    tests.append([0]*1000)
    tests.append([0]*10000)
    tests.append([0]*100000)
    tests.append([0]*1000000)

    print("-------------------------------------------------------------------")
    for k in range(len(tests)):
        l = len(tests[k])
        start_time = time()
        tests[k].insert(0, None)
        end_time = time()
        elapsed = (end_time - start_time) * 1000000
        print("Inserting at 0 of list with length of N = " +
                "{0:7} requires  {1:.4f} us".format(l, elapsed))

    print("-------------------------------------------------------------------")
    for k in range(len(tests)):
        l = len(tests[k])
        start_time = time()
        tests[k].insert(l//2, None)
        end_time = time()
        elapsed = (end_time - start_time) * 1000000
        print("Inserting at n/2 of list with length of N " +
                "{0:7} requires {1:.4f} us".format(l, elapsed))

    print("-------------------------------------------------------------------")
    for k in range(len(tests)):
        l = len(tests[k])
        start_time = time()
        tests[k].insert(l-1, None)
        end_time = time()
        elapsed = (end_time - start_time) * 1000000
        print("Inserting at n of list with length of N = " +
                "{0:7} requires {1:.4f} us".format(l, elapsed))

