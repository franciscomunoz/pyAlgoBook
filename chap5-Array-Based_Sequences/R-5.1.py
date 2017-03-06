"""The output illustrates how the list capacity is changing
during append operations. The empty list has 64 bytes used
for representint its internal state. However, after making
appends we can observe how the capacity grows when the list
is internally being reallocated """

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
        data.append(None)                     # increase length by one


