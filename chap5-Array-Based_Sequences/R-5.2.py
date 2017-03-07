"""The output illustrates how the list capacity is changing
during append operations. The capacity is printed and the
last capacity change is ignored, but it can easily be added"""

import sys                              # provides getsizeof function

if __name__ == '__main__':

    try:
        n = int(sys.argv[1])
    except:
        n = 300
    data = []

    z = sys.getsizeof(data)
    for k in range(n):
        b = sys.getsizeof(data)
        if z !=  b:
            a = len(data) - 1
            print('Capacity: {0:3d}; Size in bytes: {1:4d}'.format(a, z))
            z = b
        data.append(None)               # increase length by one




