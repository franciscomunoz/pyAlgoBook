"""Show how to use the transfer function, described in Excercise R-6.3, and two 
temporary stacks, to replace the contents of a given stack S with those same
elements, but in reversed order."""

"""Basic example of an adapter class to provide a stack interface to Python's list."""
from exceptions import Empty
from exceptions import Full

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self, maxlen = None):
        """Create an empty stack."""
        self._data = [None] * maxlen if maxlen != None else []
        self._maxlen = maxlen
        #Maybe top is not the right name for the following variable
        self._top = 0
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._top

    def is_empty(self):
        """Return True if the stack is empty."""
        return True if (self._top - 1) == -1  else False

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._top == self._maxlen:
            raise Full('Stack is full')
        self._data[self._top] = e                # new item stored at end of list
        self._top = self._top + 1 

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._top - 1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        val = self._data[self._top - 1]              # remove last item from list
        self._top = self._top - 1
        return val

if __name__ == '__main__':

    S = ArrayStack(4)                 # contents: [ ]
    T = ArrayStack(4)
    S.push(4)
    S.push(3)
    S.push(2)
    S.push(1)

    import pdb;pdb.set_trace()
    while not S.is_empty():
        T.push(S.pop())
    #T has the elements inverted with respect to S (S is now empty)
    
