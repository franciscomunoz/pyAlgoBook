"""There is a simple, but ineficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n - 1 times,
where, in each scan, the algorithm compares the current element with the next
one and swaps them if they are out of order. Implement a bubble-sort function
that takes a positional list L as a parameter. What is the running time of this
algorithm, assuming the positional list is implemented with a doubly linked list"""

from positional_list import PositionalList

def bubble_sort(L):
    if len(L) > 1:
        x = 0
        while x < len(L) - 1:    #number of passess 
            k = L.first()
            j = 0               #reset counter each iteration
            """use index since last node changes if we swap"""
            while j < len(L) - x - 1:
                node_right= L.after(k)
                value = node_right.element()
                if k.element() > value:
                    L.add_before(k,value)
                    L.delete(node_right)
                else:
                    """k is automatically forwarded every time we swap nodes"""
                    k = L.after(k)
                for i in L:
                    print(i,end=" ")
                print("")
                j += 1
            x += 1
            print("##############################")            
    return L

if __name__ == '__main__':

    pl = PositionalList()

    pl.add_last(20)
    pl.add_last(2)
    pl.add_last(12)
    pl.add_last(8)
    pl.add_last(10)
    pl.add_last(4)
    pl.add_last(14)
    pl.add_last(16)
    pl.add_last(18)
    pl.add_last(6)
    L = bubble_sort(pl)
    for i in L:
        print(i, end=" ")


    

