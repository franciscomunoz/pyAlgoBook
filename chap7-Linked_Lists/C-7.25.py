"""Give a complete implementation of the queue ADT using a sungly linked list 
that includes a header sentinel"""

from exceptions import Empty

class LinkedQueue:
    """FIFO implementation using a singly  linked list for storage."""
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next' #stramline memory usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
   #------------------------------- queue methods ----------------------------
    def __init__(self):
       """Create empty queue"""
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return true if the queue is empty."""
        return self._size == 0

    def enqueue(self, e):
        """Adds element to the queue."""
        self._header = Node(e, self._next)
        self._size += 1
    
    def dequeue(self):
        """Remove element from the queue."""
        if self.is_empty():
            raise Empty("Queue is empty")
        element = self._element
        self._header = self._next
        self._size -= 1
        return element

    def top(self):
        """Return the element to be dequeue."""
        if self.is_empty():
            raise Empty("The queue is empty.")
        return self._header._element

    



