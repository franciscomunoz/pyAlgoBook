"""Give a complete ArrayDequeue implementation of the double-ended queue ADT 
as sketched in Section 6.3.2"""    


from exceptions import Empty

class ArrayDequeue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayDequeue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the the element at the end of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        
        avail = (self._front + self._size) % len(self._data)
        return self._data[avail]


    def delete_first(self):
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

    def delete_last(self):
        """Remove and return the last element of the queue (i.e, FIFO)."""
        if self.is_empty():
            raise Empty('Queue is empty')
        
        self._size -= 1
        avail = (self._front + self._size) % len(self._data)
        val = self._data[avail]
        self._data[avail] = None
        return val

    def add_last(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        """Add an element to the front  of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     # double the array size
        self._front = (self._front - 1) if self._front > 0 else\
                len(self._data) - 1
        self._data[self._front] = e
        self._size += 1

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
    import pdb;pdb.set_trace()
    D.add_first(1)
    D.add_first(2)
    D.add_first(3)
    D.add_first(4)
    D.add_first(5)
    D.add_first(6)
    D.add_first(7)
    D.add_first(8)
    D.add_first(9)
    D.add_first(10)
    D.delete_last()
    D.delete_last()
    D.add_last(2)
    D.add_last(3)
    D.add_last(4)
    D.add_last(5)
    



