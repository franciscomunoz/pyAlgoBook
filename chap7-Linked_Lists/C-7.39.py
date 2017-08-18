"""To better model a FIFO queue in which entries may be deleted before reaching
the front, design a PositionalQueue class that supports the complete queue
ADT, yet with enqueue returning a position instane and support for a new method
, delete(p), that removes the associated with position p from the queue. You may
use the adapter design pattern using a PositionalList as your storage."""

#Not tested since implementation is just an simple adapter of the positional list
from positional_list import PositionalList

class PositionalQueue:

    def __init__(self):
        """Creates an empty positional queue"""
        self._data = PositionalList()

    def enqueue(self,e):
        """Add an element to the back to the positional queue and return pos"""
        return self._data.add_last(e)  

    def dequeue(self):
        """Removes an element from the front of the queue and return pos"""
        return self._data.delete(self._data.first())

    def first(self):
        """Returns to the first element from the queue front"""
        return self._data.first()

    def is_empty(self):
        """Return true if queue is empty"""
        return len(self._data)

    def delete(self, p):
        """Deletes an element from the queue given its position"""
        return self._data.delete(p)

    def __len__(self):
        """Return number of entries on positional queue"""
        return len(self._data)
