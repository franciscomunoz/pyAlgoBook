"""Find the sum of an n x n data set using comprehension syntax"""

def find_sum(data):
    return sum([sum(sublist) for sublist in data])

if __name__ == '__main__':

    tests = []
    tests.append([[1,7,5,8],[3,9,8,7],[1,2,3,4]])
    tests.append([[4,5,6,7],[6,5,4,3],[1,8,9,3]])
    for i in range(len(tests)):
        total = find_sum(tests[i])
        print("The sum of all elements of matrix = {0}".format(total))

