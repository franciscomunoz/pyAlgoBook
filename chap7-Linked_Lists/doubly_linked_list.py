class DoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    #-------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'            # streamline memory

        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                           # user's element
            self._prev = prev                                 # previous node reference
            self._next = next                                 # next node reference

    #-------------------------- list constructor --------------------------

    def __init__(self):
        """Create an empty list."""
        self._header = None
        self._trailer = None
        self._size = 0                                      # number of elements

    #-------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    #-------------------------- nonpublic utilities --------------------------

    def _insert_first(self, e):
        """Inserts node at the head"""
        if self._header is None and self._trailer is None:
            """list is empty"""
            node = self._Node(e, None, None)
            node._element = e
            self._header = self._trailer = node
        else:
            node = self._Node(e, None, self._header)
            self._header = node
        return node

    def _remove_front(self):
        """Sets the header node to None and return element"""
        element = None
        if self._header is None and self._trailer is None:
           raise Exception("List is empty")
        else:
            element = self._header._element
            if self._header is self._trailer:
                self._header = self._trailer = None
            else:
                tmp = self._header
                element = tmp._element
                self._header = self._header._next
                self._header._prev = tmp._element = tmp._next = None
                tmp = None
        return element

    def _insert_last(self, e):
        """Inserts node at the end"""
        if self._header is None and self_trailer is None:
            """list is empty"""
            node = self._Node(e, None, None)
            node._element = e
            self._header = self._trailer = node
        else:
            node = self._Node(e, self._trailer, None)
            self._trailer._next = node
            self._trailer = node
        return node

    def _remove_back(self):
        """Sets the header node to None and return element"""
        element = None
        if self._header is None and self._trailer is None:
           raise Exception("List is empty")
        else:
            element = self._header._element
            if self._header is self._trailer:
                self._header = self._trailer = None
            else:
                tmp = self._trailer
                element = tmp._element
                self._trailer = self._trailer._prev
                self._trailer._next = tmp._element = tmp._prev = None
                tmp = None
        return element

    def _insert_between(self, e, predecessor, successor):
        node = None
        """Inserts an element between nodes. Nodes are validaded by client"""
        if predecessor is None and successor is self._header:
            """We default and insert at front, since this is what the user
            might have wanted in the first place"""
            node = self._insert_first(e)
        elif predecessor is self._trailer and successor is None:
            """We infer client wanted to insert at the end"""
            node = self._insert_last(e)
        elif predecessor is not None and successor is not None\
                and predecessor is not successor:
            """Insert between valid nodes"""
            node = self._Node(e, predecessor,successor)
            predecessor._next = node
            successor._prev = node
        else:
            raise IndexError("Either predecessor or successor or both invalid!")
        return node

    def _delete_node(self, node):
        element = None
        if node._prev is self._header and node is self._trailer:
            """single element"""
            element = node._element
            node._element = None
        elif node._prev is None and node._next is not None:
            element = self._remove_front()
        elif node._prev is not None and node._next is None:
            element = self._remove_back()
        else:
            """Remove in between"""
            successor = node._next
            predecessor = node._prev
            tmp = node
            element = tmp._element
            predecessor._next = successor
            successor._prev = predecessor
            tmp._prev = tmp._next = tmp._element = None
            tmp = None
        return element
            


