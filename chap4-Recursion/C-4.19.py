"""Function that places even numbers before odd

if returns are removed in the else condition, the recursion
tree becomes messy as shown :

    (0, 6, [2, 3, 5, 7, 9, 4, 8])
    (1, 6, [2, 3, 5, 7, 9, 4, 8])
    (2, 5, [2, 8, 5, 7, 9, 4, 3])
    (3, 4, [2, 8, 4, 7, 9, 5, 3])
    (4, 3, [2, 8, 4, 7, 9, 5, 3])
    (3, 4, [2, 8, 4, 7, 9, 5, 3])
    (4, 3, [2, 8, 4, 7, 9, 5, 3])
    (2, 5, [2, 8, 4, 7, 9, 5, 3])
    (3, 4, [2, 8, 4, 7, 9, 5, 3])
    (4, 3, [2, 8, 4, 7, 9, 5, 3])
    (1, 5, [2, 8, 4, 7, 9, 5, 3])
    (2, 4, [2, 8, 4, 7, 9, 5, 3])
    (3, 3, [2, 8, 4, 7, 9, 5, 3])
    (4, 2, [2, 8, 4, 7, 9, 5, 3])
    [2, 8, 4, 7, 9, 5, 3]

with the return statements in place gives a shorter recursion tree

    (0, 6, [2, 3, 5, 7, 9, 4, 8])
    (1, 6, [2, 3, 5, 7, 9, 4, 8])
    (2, 5, [2, 8, 5, 7, 9, 4, 3])
    (3, 4, [2, 8, 4, 7, 9, 5, 3])
    (4, 3, [2, 8, 4, 7, 9, 5, 3])
    [2, 8, 4, 7, 9, 5, 3]
"""
def move_even_odd(data,start,stop):
    #print(start,stop,data)
    if start > stop:
        return
    else:
        if data[start] % 2 == 1 and data[stop] % 2 == 0:
            data[start],data[stop] = data[stop],data[start]
            move_even_odd(data,start+1,stop-1)
            return
        if data[start] % 2 == 0 and data[stop] % 2 == 0:
            move_even_odd(data,start+1,stop)
            return
        if data[start] % 2 == 1 and data[stop] % 2 == 1:
            move_even_odd(data,start,stop-1)
            return
    move_even_odd(data,start+1,stop-1)

if __name__ == '__main__':
    tests=[]
    tests.append([2,3,5,7,9,4,8])
    tests.append([0,0,0,0,0,0,0])
    tests.append([2,2,2,2,2,2,2])
    tests.append([3,3,3,3,3,3,3])
    tests.append([9,8,7,6,5,4,3,2,1])
    tests.append([0,1,2,3,4,5,6,7,8,9])
    tests.append([1,1,1,3,4,5,6,9,9,9])

    for i in range(len(tests)):
        move_even_odd(tests[i],0,len(tests[i])-1)
        print(tests[i])



