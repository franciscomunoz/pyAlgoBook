"""Modify ArrayQueue implementation so that the queue's capacity is limited
to maxlen elements, where maxlen is an optional parameter to the constructor
(that defaults to None). If queue is called when the queue is at full capacity,
throw a Full exception (defined similarly to Empty)"""

from exceptions import Empty
from exceptions import Full

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    def __init__(self, capacity = None):
        """Create an empty queue."""
        self._data = [None] * capacity if capacity != None else [None] * 0
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
            raise Full('Queue is full')
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    #not used in this example
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

    S1 = ArrayQueue()
    try:
        S1.enqueue(1)
    except Full as e:
        print(e)
    S2 = ArrayQueue(4)
    S2.enqueue(1)
    S2.enqueue(2)
    S2.enqueue(3)
    S2.enqueue(4)
    S2.dequeue()
    S2.dequeue()
    S2.enqueue(5)
    S2.enqueue(6)
    print(S2.first())

