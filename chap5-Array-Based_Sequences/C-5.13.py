"""The output illustrates how the list capacity is changing
during append operations.  The key of this exercise is to
observe how the capacity changes when inserting data to an
an array that doesn't start at growing from size "0". We
use two arrays, the original from 5.1 and another starting
to grow from a different value. Both arrays grow by the same
values
"""

import sys                              # provides getsizeof function

if __name__ == '__main__':

    try:
        n = int(sys.argv[1])
    except:
        n = 100
    initial_size = 1000
    data = []
    data_init_size = [] * initial_size


    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        a_l = len(data_init_size) + initial_size
        b_l = sys.getsizeof(data_init_size)
        print("Reference : Length: {0:3d}; Size in bytes: {1:4d}" \
                " | | | Measured Array {2:3d}+  Length: {3:3d}; Size in bytes: {4:4d}:"\
              .format(a,b,initial_size,a_l,b_l))
        data_init_size.append(None)
        data.append(None)                     # increase length by one


