"""Implement a function that accepts a PositionalList L of n integers sorted
in nondecreasing order, and another value V, and determines in O(n) time if 
there are two elements of L tha sum precisely to V. The function should return 
a pair of positions of such elements, if found, or None otherwise."""

from positional_list import PositionalList

def find_sum(pl, V):

    left = pl.first()
    right = pl.last()
    while left != right:
        sum = left.element() + right.element()
        if sum == V:
            return left, right
        left = pl.after(left)
        right = pl.before(right)
    return None, None

if __name__ == '__main__':

    pl = PositionalList()

    pl.add_last(2)
    pl.add_last(4)
    pl.add_last(6)
    pl.add_last(8)
    pl.add_last(10)
    pl.add_last(12)
    pl.add_last(14)
    pl.add_last(16)
    pl.add_last(18)
    pl.add_last(20)

    values = [2,4,6,20,34,18,22]
    for i in values:
        x,y = find_sum(pl,i)
        if x is not None:
            print("The elements that sum : {0} are,  {1} and {2}".format(i, 
                x.element(), y.element()))
