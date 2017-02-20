"""Recursive function that determines whether a string is a palindrome"""

def palindrome(data,i_f,i_b):
    if i_f > i_b:
        return "is a palindrome"
    else:
        tmp_str = data.lower()
        if tmp_str[i_f] != tmp_str[i_b]:
            return "is NOT a palindrome"
        return palindrome(data,i_f+1,i_b-1)


if __name__ == '__main__':
    tests=[]
    tests.append("Anna")
    tests.append("Kayak")
    tests.append("Madam")
    tests.append("Racecar")
    tests.append("Hello")
    tests.append("air")

    for i in range(len(tests)):
        print("The word {0} is palindrome ? : {1} ".format(tests[i],
            palindrome(tests[i],0,len(tests[i])-1)))

