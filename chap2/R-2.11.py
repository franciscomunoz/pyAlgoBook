#!/usr/bin/python

class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self,d):
        """Create a d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self,j):
        """Return jth coordinate vector."""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self,other):
        """Return sum of two vectors."""
        if len(self) != len(other):     #relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
   
    def __radd__(self,other):
        """Return sim of two vectors when ."""
        if len(self) != len(other): #relies on __len__method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self,other):
        """Return difference of two vectors."""
        if len(self) != len(other):     #relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] -  other[j]
        return result

    def __eq__(self,other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other            #rely on existing __eq__ definition
    
    def __neg__(self):
        """Return vector with coordinates negated."""
        for i in range(len(self)):
            self[i] = self[i] * -1
        return self

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  #adapt list representation




myVector = Vector(3)
myVector[0] = 4
myVector[1] = 8
myVector[2] = 12

u = [5,3,10] + myVector



for i in range(len(myVector)):
        print(u[i])
