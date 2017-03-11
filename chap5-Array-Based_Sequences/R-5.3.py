"""The output illustrates how the list capacity is growing
during append operations and how it shrinks after several
pops. The list capacity is reduced differently when compared
to how it grows"""

import sys                              # provides getsizeof function

if __name__ == '__main__':

    try:
        n = int(sys.argv[1])
    except:
        n = 100
    data = []

    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)               # increase length by one

    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.pop()                      # decrease length by one


