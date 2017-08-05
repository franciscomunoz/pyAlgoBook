"""Give a complete implementation of the positional list ADT using a doubly
linked list that does not include any centinel nodes"""

from doubly_linked_list import DoublyLinkedList

class MyPositionalList(DoublyLinkedList):
    """A sequential container of elements allowing positional access."""

    """Solution to Exercise 7.35"""
    #-------------------------- nested Iterator class --------------------------
    class Position_Iterator:

        def __init__(self, head_node):

            self._node = head_node

        def __iter__(self):
            """By convention, an iterator must return itself as an iterator"""
            return self

        def __next__(self):
            if self._node is not None:
                tmp = self._node._element
                self._node = self._node._next
                return tmp
            else:
                raise StopIteration()      #There are no more elements
    #-------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element.


        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)               # opposite of __eq__

    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        return self.Position(self, node)         # legitimate position

    #------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    """
    def __iter__(self):
        Generate a forward iteration of the elements of the list.
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    """
    def __iter__(self):
        """Excercise 7.35 This is the actual iterator"""
        return self.Position_Iterator(self._header)

    #------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, None, self._header)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer, None)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def clear(self):
        """Removes all the elements from, the list"""
        node = self.first()._node
        while node  is not None:
            tmp = node
            node = node._next
            tmp._prev = tmp._next = tmp._element = None
        self._header  = self._trailer

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element       # temporarily store old element
        original._element = e               # replace with new element
        return old_value                    # return the old element value

if __name__ == '__main__':
    pl = MyPositionalList()
    pl.add_last(6)
    pl.add_last(7)
    pl.add_first(5)
    pl.add_first(4)
    pl.add_first(3)
    pl.add_first(2)
    pl.add_after(pl.last(),10)
    pl.add_before(pl.last(),9)
    pl.delete(pl.before(pl.last()))
    pl.delete(pl.last())
    pl.delete(pl.first())
    pl.replace(pl.first(),1)
    for i in pl:
        print(i)

    pl.clear()
    for i in pl:
        print(i)

