from doubly_linked_base import _DoublyLinkedBase
from exceptions import Empty

class LinkedDeque(_DoublyLinkedBase):         # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
    """Return (but do not remove) the element at the front of the deque.

    Raise Empty exception if the deque is empty.
    """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element        # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element       # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)   # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)   # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)  # use inherited method

    def concatenate(self, anotherDeque):
        if self.is_empty():
            raise Empty("Deque is empty")
        if anotherDeque.is_empty():
            raise Empty("Argument dequeue is empty")
        """Connect forward and backward nodes"""
        self._trailer._prev._next = anotherDeque._header._next
        anotherDeque._header._next._prev = self._trailer._prev
        """Point trailer backward pointer to the new end of the deque"""
        self._trailer._prev = anotherDeque._trailer._prev
        anotherDequeue._header = None
        anotherDequeue._trailer = None
        anotherDequeue._size = 0




        
        
