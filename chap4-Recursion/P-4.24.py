"""Recursive function which solves the following sum puzzle


            boy + girl = baby

            b  o  y  g  i  r  l  a
indexes     0, 1, 2, 3, 4, 5, 6, 7
weights THIS IS WHAT WE PERMUTATE AND MAKE THE SUM (initially same as index)

Many permutations will be created for assigning weights to each word. When a
permutation subset matches the Universe of words, each element is going to be
converted to integer, then added.

Values are hard-coded because the book hasn't covered nothing fancy yet
"""

def puzzlesolver(k,S,U):
    for i in range(len(U)):
        e = U[i]
        del U[i]
        S.append(e)
        if k == 1:
            """Test whether S is a permuation that solves the puzzle"""
            result = []
            val1 = int(S[0]+S[1]+S[2]+S[3])
            val2 = int(S[4]+S[5]+S[6]+S[7])
            result = int(S[0]+S[7]+S[0]+S[2])
            if val1 + val2 == result:
                print(k,i,S,U)
        else:
            puzzlesolver(k-1,S,U)
        U.insert(i,e)
        del S[-1]

if __name__ == '__main__':
    tests=[]
    tests.append(['0','1','2','3','4','5','6','7'])
    S = []
    for i in range(len(tests)):
        puzzlesolver(len(tests[i]),S,tests[i])







