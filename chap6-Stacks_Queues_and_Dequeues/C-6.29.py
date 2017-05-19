"""In certain applications of the queue ADT, it is common tp repeatedly dequeue an
element, process it in some way, and then inmmeaditely enqueue the same element.
Modify the ArrayQueue implementation to include a rotate method that has 
semantics idential to the combination, Q.enqueue(Q.dequeue()). However, your
implementation should be more efficient than making two separate calls (for
example, because there is no need to modify _size) """

from exceptions import Empty

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
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

    def dequeue(self):
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

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self.data))     # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def rotate(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        e = self._data[self._front]
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        #subtract 1 to size otherwise there is a gap when inserting
        avail = (self._front + self._size - 1) % len(self._data)
        self._data[avail] = e
        print(self._data)
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

    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)
    
    Q.dequeue()
    Q.dequeue()
    Q.rotate()
    Q.rotate()
    Q.rotate()
    

    
