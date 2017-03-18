"""Find the sum of an n x n data set using standard control structures"""

def find_sum(data):
    total = 0
    for sublist in data:                #row
        for i in range(len(sublist)):   #colum
            total += sublist[i]
    return total

if __name__ == '__main__':

    tests = []
    tests.append([[1,7,5,8],[3,9,8,7],[1,2,3,4]])
    tests.append([[4,5,6,7],[6,5,4,3],[1,8,9,3]])
    for i in range(len(tests)):
        total = find_sum(tests[i])
        print("The sum of all elements of matrix = {0}".format(total))
