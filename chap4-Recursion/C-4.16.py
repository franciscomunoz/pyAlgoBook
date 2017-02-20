"""Recursive function which prints a string in reverse"""

def print_reverse(data,i):
    if i < 0:
        return
    else:
        print(data[i],end="")
    return print_reverse(data,i-1)


if __name__ == '__main__':
    tests=[]
    tests.append("pots&pans")

    for i in range(len(tests)):
        print_reverse(tests[i],len(tests[i])-1)
        print()
