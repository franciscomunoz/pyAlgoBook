"""Function that places numbers smaller than k before and bigger after. 
Both functions represent the same Algorithm, but one is iterative and the 
other recursive."""

def iter_k(data,k):
    i = -1
    for j in range(len(data)):
        if data[j] <= k:
            if data[i] == k and data[j] < data[i]:
                data[i],data[i+1] = data[i+1],data[i]
                data[i],data[j] = data[j],data[i]
                i = i + 1
            else:
                i = i + 1
                data[i],data[j] = data[j],data[i]
        #print(i,j,data)
def recu_k_dist(data,l,k):
    if l ==  0:
        return -1,0
    else:
        i, j = recu_k_dist(data,l-1,k)
        if data[j] <= k:
            if data[i] == k and data[j] < data[i]:
                """This is a variation of the quick sort partition. Example
                 data[i] = 5
                 data[j] = 4
                 2,3,5,7,9,4,8
                 After first swap
                 2,3,7,5,9,4,8
                 After second swap
                 2,3,4,5,9,7,8
                """
                data[i],data[i+1] = data[i+1],data[i]
                data[i],data[j] = data[j],data[i]
                i = i + 1
            else:
                """Regular quicksort partition"""
                i = i + 1
                data[i],data[j] = data[j],data[i]
        #print(i,j,data)
    return i,j+1



if __name__ == '__main__':
    tests=[]
    tests.append([2,3,5,7,9,4,8])
    tests.append([0,0,0,0,0,0,0])
    tests.append([2,2,2,2,2,2,2])
    tests.append([3,3,3,3,3,3,3])
    tests.append([9,8,7,6,5,4,3,2,1])
    tests.append([0,1,2,3,4,5,6,7,8,9])
    tests.append([1,1,1,3,4,5,6,9,9,9])
    tests.append([6,1,1,3,4,5,6,9,9,9])
    tests.append([9,9,9,3,4,5,6,9,9,9])
    tests.append([9,9,9,3,4,5,6,9,9,9])
    tests.append([9,9,9,3,4,6,9,9,9])
    tests.append([2,3,5,7,9,4,8,7,6,5,4,3,2])

    for i in range(len(tests)):
        #iter_k(tests[i],5)
        recu_k_dist(tests[i],len(tests[i]),5)
        print(tests[i])



