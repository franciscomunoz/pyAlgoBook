"""Describe a non recursive algorithm for enumerating all the permutations of 
the numbers {1,2,3,...,n}. This problem was solved as if we wanted to find the 
permutations of a string by inserting a + mark and generate permutations"""
import copy

from exceptions import Empty
from exceptions import Full

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self, maxlen = None):
        """Create an empty stack."""
        self._data = []                       # nonpublic list instance
        self._maxlen = maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._maxlen != None and len(self._data) >= self._maxlen:
            raise Full('Stack is full')
        self._data.append(e)                  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list


def find_permutations(data):
    S = ArrayStack()
    data.insert(0,"+")
    S.push(data)
    count = 0
    while not S.is_empty():
        val = S.pop()
        if val[len(val) - 1] == "+":
            count +=1
        else:
            z = val.index("+")
            """In case the + is at the beginning"""
            sub1 = val[0:z] if z > 0 else ''
            sub2 = val[z+1:]

            for i in range(len(sub2)):
                attemp = []
                """Append values from sub1 of not empty. We want to avoid the 
                creation of an '' element in the list"""
                if sub1 != '':
                    for j in range(len(sub1)):
                        attemp.append(sub1[j])
                    
                attemp.append(sub2[i])
                """
                Prepare deep copy and delete value which is going to be moved
                to the right of the + mark. We are gooing to be sampling values
                from the right of the + mark by moving them to the left
                """
                s = copy.deepcopy(sub2)
                del s[i]

                attemp.append("+")
                """Append remaining elements to the left of the + mark""" 
                for j in range(len(s)):
                    attemp.append(s[j])

                S.push(attemp)
    return count

if __name__ == '__main__':


    test = ["1","2","3","4"]

    print("The amount of permutation for the list : {0}".\
            format(find_permutations(test)))
