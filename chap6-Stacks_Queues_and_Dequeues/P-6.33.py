"""Give an array-based implementation of a double-ended queue supporting all
of the public behaviors shown in Table 6.4 for the collections.dequeue class,
inclusing use of the maxlen optional parameter. When a length-limited queue is
full, provide semantics similar to the collections.queue class, whereby a call
to insert an element on one end of a dequeue causes an element to be lost from 
the opposite side."""

"""append_left and delete last"""

from exceptions import Empty
from exceptions import Full


class ArrayDequeue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self,maxlen = 0):
        """Create an empty queue."""
        if maxlen != 0 and maxlen < 0:
            raise ValueError('Do not input negative dimensions')
        if maxlen > ArrayDequeue.DEFAULT_CAPACITY:
            self._data = [None] * maxlen
        else:
            self._data = [None] * ArrayDequeue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def __getitem__(self,k):
        """Return (but do not remove) the element in terms of the index k

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        if k < 0:
            index = k + len(self._data)
            if index < 0 or  index > self._size - 1:
                raise IndexError('Out of bounds')
            avail = (self._front + index) % len(self._data)
            return self._data[avail]
        else:
            if k >= self._size:
                raise IndexError('Out of bounds')
            index = (self._front + k) % len(self._data)
            return self._data[index]

    def __setitem__(self,k,v):
        """Return (but do not remove) the element in terms of the index k

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        if k < 0:
            index = k + len(self._data)
            if index < 0 or  index > self._size - 1:
                raise IndexError('Out of bounds')
            avail = (self._front + index) % len(self._data)
            self._data[avail] = v
        else:
            if k >= self._size:
                raise IndexError('Out of bounds')
            index = (self._front + k) % len(self._data)
            self._data[index] = v

    def pop_left(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def pop(self):
        """Remove and return the last element of the queue (i.e, FIFO)."""
        if self.is_empty():
            raise Empty('Queue is empty')
        
        self._size -= 1
        avail = (self._front + self._size) % len(self._data)
        return self._data[avail]

    def append(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            """When queue is full, an element from the oposite size is removed"""
            self._data[self._front] = None         # help garbage collection
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def apped_left(self, e):
        """Add an element to the front  of queue."""
        if self._size == len(self._data):
            """When queue is full, an element from the oposite size is removed"""
            self._size -= 1
            avail = (self._front + self._size) % len(self._data)
            self._data[avail] = None

        self._front = (self._front - 1) if self._front > 0 else\
                len(self._data) - 1
        self._data[self._front] = e
        self._size += 1

    def clear(self):
        """Eliminate array and set size and front back to 0"""
        self._data = [None] * len(self._data) 
        self._front = 0
        self._size = 0

    def rotate(self,k):    
        """Rotates values in a dequeue"""    
        if self.is_empty():
            raise Empty('Queue is empty')
        for i in range(k):
            avail = (self._front + self._size - 1) % len(self._data)
            right_val = self._data[avail]
            self._data[avail] = None
            if self._front == 0:
                self._front = len(self._data) - 1
            else:
                self._front -= 1
            self._data[self._front] = right_val
            
    def remove(self,v):
        """Removes the first ocurrence of the argument"""
        start = -1
        #Find index
        for i in range(self._size):
            index = (self._front + i) % len(self._data) 
            val = self._data[index]
            if v == val:
                start = i
                break
        if start == -1:
            raise ValueError('Value not found')
        #Shift elements by one and consider possible queue wrapping
        while start + 1 < self._size:
            index = (self._front + start) % len(self._data) 
            index_plus = (self._front + start + 1) % len(self._data) 
            self._data[index] = self._data[index_plus]
            start += 1
    
        index = (self._front + start) % len(self._data) 
        #Change the previous valid end of queue to None (now has been shifted)
        self._data[index] = None
        self._size -= 1
        
    def count(self,v):
        """Count matches of v """
        count = 0
        for i in range(self._size):
            index = (self._front + i ) % len(self._data)
            if self._data[index] == v:
                count += 1
        return count

    def _resize(self, cap):                  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]            # intentionally shift indices
            walk = (1 + walk) % len(old)         # use old size as modulus
        self._front = 0                        # front has been realigned

if __name__ == '__main__':

    D = ArrayDequeue()
    D.apped_left(1)
    D.append(2)
    D.apped_left(3)
    D.append(4)
    import pdb;pdb.set_trace()
    D.append(5)
    
    print(D[4])
    D[3] = 100 
    D.rotate(5) 
    D.remove(1)    
    print(D.count(100))
