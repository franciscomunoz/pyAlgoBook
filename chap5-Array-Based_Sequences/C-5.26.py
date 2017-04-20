"""Describe an algorithm for finding five integers in B that are repeated. B
is an array with n >= 6 containing integers from 1 to n - 5 """

def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):         # from 1 to n-1
        cur = A[k]                       # current element to be inserted
        j = k                            # find correct index j for current
        while j > 0 and A[j-1] > cur:    # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                       # cur is now in the right place

def find_repeated(data):
    repeated = -1
    count = 0
    insertion_sort(data)
    for i in range((len(data) - 1)):
        if data[i] == data[i + 1]:
            count += 1
            if count == 5:
                repeated = data[i]
        else:
            count = 0
    return repeated

if __name__ == '__main__':
    tests = []
    tests.append([1,2,3,4,5,6,7,8.9,10,5,5,5,5,5])
    tests.append([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5])

    for i in range(len(tests)):
        repeated = find_repeated(tests[i])
        print("Test {0} has ".format(i),end="")
        print("no repeated elements") if repeated == -1 else\
        print("5 repeated elements : {0}".format(repeated))

