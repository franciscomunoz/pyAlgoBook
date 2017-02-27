"""Iterative implementation of  power """
def power(x, n):
    k = 0
    while (1 << k) <= n:
        k += 1
    answer = 1.0
    for j in range(k-1, -1, -1):
        answer *= answer
        if (1 << j) & n > 0:
            answer *= x
    return answer

if __name__ == '__main__':
    tests=[]
    tests.append([9,4])
    tests.append([3,6])

    for i in range(len(tests)):
        x,y=tests[i][0],tests[i][1]
        print("The result of elevating {0} to the {1} is : {2}".format(x,y,power(x,y)))
