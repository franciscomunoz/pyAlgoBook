"""Insert function is changed in order to improve performance. If a resize
occurs elements are shifted to their final position during this operation"""
import ctypes                                      # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if 0 <= k < self._n:
            return self._A[k]                          # retrieve from array
        elif k == -1 and self._n != 0:
            return self._A[-1]
        else:
            raise IndexError('invalid index')

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)           # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                              # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                        # new (bigger) array
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
        self._A = B                                    # use the bigger array
        self._capacity = c

    def _make_array(self, c):                        # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()              # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            new_A = self._make_array(2 * self._capacity) 
            for i in range(k):
                new_A[i] = self._A[i]
            new_A[k] = value
            for j in range(k,self._capacity):
                new_A[j + 1] = self._A[j]
            self._A = new_A
            self._capacity = 2 * self._capacity
        else:
            for j in range(self._n, k, -1):                # shift rightmost first
                self._A[j] = self._A[j-1]
            self._A[k] = value                             # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):    # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None        # help garbage collection
                self._n -= 1                       # we have one less item
                return                             # exit immediately
        raise ValueError('value not found')    # only reached if no match
    """Needed in order to be able to print array (getitem too)"""
    def __len__(self):
        return self._n



if __name__ == '__main__':
    array = DynamicArray()
    array.append(3)
    array.append(4)
    """Capacity is full"""
    array.insert(1,10)
    """Array class does not know how to print itself. This is why we iterate"""
    print("Array after inserting new element :",end="")
    for i in range(len(array)):
        print(array[i],end="")
    print()





