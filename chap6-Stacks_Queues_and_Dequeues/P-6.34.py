""""Implement a program that can input an expression in posix notation (See
excercise C-6.22) and output its value """

from array_stack import ArrayStack

def postfix(data):
    S  = ArrayStack()
    for i in data:
        if i not in ('*','+','/','-'):
            S.push(i)
        else:
            a = S.pop()
            b = S.pop()
            if i == '+':
                S.push(a + b)
            elif i == '-': 
                S.push(a - b)
            elif i == '*': 
                S.push(a * b)
            elif i == '/': 
                S.push(a / b)
    x = S.pop()
    if not S.is_empty():
        raise ValueError('Expression problem')
    return x

if __name__ == '__main__':

    tests = []

    tests.append([5,6,2,'*','+',8,'+'])
    tests.append([5,7,'+',8,'+',10,'+'])
    #Error scenario
    #tests.append([5,7,'+',8,'+',10,'+','+'])
    #tests.append([5,7,'+',8,'+',10,'+',10])

    for i in range(len(tests)):
        print("The result of evalueting postfix expressions : {0}".\
                format(postfix(tests[i])))



    
