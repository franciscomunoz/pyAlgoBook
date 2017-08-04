"""Design a forward list ADT that abstracts the operationson a singly linked
list, much as the positional list ADT abstracts the use of a doubly linled list.
Implement a ForwardList class that supports such an ADT"""

from positional_list import PositionalList

class ForwardList(PositionalList):
    """Create an abstraction of a Single Linked List using a Positional List"""
    def __init__(self):
        super().__init__()

    def remove_first(self):
        """Remove element at the head of the  Single Linked List"""
        p = super().first()
        if p is not None:
            super().delete(p)

    def remove_last(self):
        """Remove element at the end of the Single Linked List"""
        p = super().last()
        if p is not None:
            super().remove(p)

    def add_first(self,e):
        """Insert an element at the front of a SLL and return position"""
        super().add_first(e)

    def add_last(self,e):
        """Insert an element at the back of a SLL and return position"""
        super().add_last(e)

    def is_empty(self):
        """Return true if SLL is empty"""
        return False if super().first() is None else True

if __name__ == '__main__':
    fl = ForwardList()

    fl.add_first(5)
    fl.add_last(10)
    fl.add_last(11)
    fl.add_last(12)
    fl.add_last(13)
    #We use the __iter__ un super as it is, so we do not override it
    for i in fl:
        print(i)


