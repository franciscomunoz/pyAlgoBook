"""Recursive implementation of a function which finds whether there is a
sum that is equal to k in a sorted sequence """

def find_sum(data,start,stop,k):
    if start > stop:
        return 0,0
    else:
        s = data[start] + data[stop]
        if s == k:
            return start,stop
        elif s > k:
            return find_sum(data,start,stop-1,k)
        else:
            return find_sum(data,start+1,stop,k)

    
if __name__ == '__main__':
    tests=[]
    tests.append([2,3,5,7,9,4,8])
    tests.append([0,0,0,0,0,0,0])
    tests.append([2,2,2,2,2,2,2])
    tests.append([3,3,3,3,3,3,3])
    tests.append([0,1,2,3,4,5,6,7,8,9])
    tests.append([1,3,4,5,6,9,9,9])
    tests.append([2,3,5,7,9,4,8,9,10,23,123,200])

    for i in range(len(tests)):
        k = 5
        x,y = find_sum(tests[i],0,len(tests[i])-1,k)
        print("The indexes that sum to {0}".format(k),end="")
        print(" are {0},{1}".format(x,y)) if x != 0 or y != 0 else \
        print(" were not found")



