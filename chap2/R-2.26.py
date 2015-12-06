#!/usr/bin/python

class ReverseSequenceIterator:
    """An iterator for any Python's sequence types."""
    def __init__(self,sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence           #keep a regerence to the underlying data
        self._k = len(sequence)        #will increment to 0 on the first call to next

    def __next__(self):
        """Return the next element, or else raise StopIterator error."""
        self._k -= 1
        if self._k >= 0:
            return (self._seq[self._k])     #return the data element
        else:
            raise StopIteration()           #there are no more elements

    def __iter__(self):
        """By convention, an iterator must return  itself as an iterator."""
        return self



list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,0]
it = ReverseSequenceIterator(list)
for n in it:
    print(n)



