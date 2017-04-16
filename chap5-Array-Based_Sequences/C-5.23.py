"""Comparing efficiency when constructing a list using list comprehension syntax
vs append"""

import sys
from time import time

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000

from time import time            # import time function from time module

def average_append(n):
    squares = []
    start = time()
    for k in range(1, n + 1):
        squares.append(k * k)
    end = time()
    return (end - start) / n

def average_list_comp(n):
    start = time()
    squares = [ k * k for k in range(1, n + 1)]
    end = time ()
    return (end - start) / n

if __name__ == '__main__':
    n = 10
    while n <= maxN:
        print('Average using append {0:.3f} ms for n {1}'\
            .format(average_append(n)*1000000, n))
        print('Average using list comprehension is {0:.3f} ms for n {1}'\
            .format(average_list_comp(n)*1000000, n))
        n *= 10


