"""Implement a function which removes all the ocurrences of a number in an list.
This operation must occur in O(n)"""

def remove_all(data, val):
    """Compacts all non repeated elements by overwriting repeated locations
    of repeated elements"""
    keep = 0 
    for i in range(len(data)):
        if data[i] != val:
            data[keep] = data[i]
            keep += 1
    data = data[0:keep]


if __name__ == '__main__':
    tests = []
    remove_me = 10
    tests.append([1,2,3,4,10,6,7,8,9,10,10,1,2,3,4,5,1,2,3,4,5])
    for i in range(len(tests)):
        """Print the repeated element, otherwise None"""
        remove_all(tests[i],remove_me)
        print("Test {0} after removing : {1}".format(i, tests[i]))

