"""Write a python program for a Matrix class that can add and multiply two-dimensional 
arrays of numbers, assuming the dimensions are appropiate for the operation"""


class Matrix:
    """Represent a matrix"""
    def __init__(self, n, m):
        """Create an empty n x m matrix"""
        self._matrix = [ [ 0 for j in range(m) ] for i in range(n)]
        self._n = n
        self._m = m
    
    def __getitem__(self, index):
        return self._matrix[index[0]][index[1]]

    def __setitem__(self, index, value):
        self._matrix[index[0]][index[1]] = value

    def __add__(self, other):
        """Adds Matrices provided both have the same dimensions"""
        if isinstance(other,(Matrix)):
            if self._n != other._n or self._m != other._m:
                raise ValueError("dimensions must agree")
            result = [ [self._matrix[n][m] + other._matrix[n][m] for m in range(self._m) ]\
                    for n in range(self._n)]
        else:
            raise TypeError("Bad argument, addition cannot be performed")
        return result

    
    def __mul__(self, other):
        """Performs matrix multiplication provided dimensions agree"""
        product  = [ [ 0 for j in range(other._m) ] for i in range(self._n)]
        if isinstance(other,(Matrix)):
            if self._m !=  other._n:
                raise ValueError("dimensions must agree")
            """The way I saw it is ...
            i is the current row of left matrix
            j is the current colum of right matrix
            k is the current row  of righth matrix """
            for i in range(self._n):
                for j in range(other._m):
                    for k in range(other._n):
                        product[i][j] += self._matrix[i][k] * other._matrix[j][k]
        else:
            raise TypeError("Bad argument, addition cannot be performed")
        return product

if __name__ == '__main__':

    matrix1 = Matrix(2,3)
    matrix1[0,0] = 1
    matrix1[0,1] = 2
    matrix1[0,2] = 3
    matrix1[1,0] = 4
    matrix1[1,1] = 5
    matrix1[1,2] = 6
   
    matrix2 = Matrix(3,3)
    matrix2[0,0] = 2
    matrix2[0,1] = 2
    matrix2[0,2] = 2
    matrix2[1,0] = 2
    matrix2[1,1] = 2
    matrix2[1,2] = 2
    matrix2[2,0] = 2
    matrix2[2,1] = 2
    matrix2[2,2] = 2

    product = matrix1 * matrix2
    print("The product between {0} and {1} is : {2}".format(matrix1,matrix2,product)) 
    sum_matrix = matrix1 + matrix1
    print("The sum between {0} and {1} is : {2}".format(matrix1,matrix2,sum_matrix)) 
