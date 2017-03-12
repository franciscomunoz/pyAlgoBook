"""Implement a function which finds duplicates in a sequence of elements. In
this implementation there isn't any need to sort the elements"""

def find_repeated(A):
    found = [False] * (len(A) + 1)
    for val in A:
        if found[val] == True:
            return val # Repeated element
        else:
            found[val] = True

if __name__ == '__main__':
    tests = []
    tests.append([1,2,3,4,6,7,8,9,10,10])
    tests.append([1,2,3,4,5])
    for i in range(len(tests)):
        """Print the repeated element, otherwise None"""
        print(find_repeated(tests[i]))

