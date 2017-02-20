"""Recursive function that determines if a string has more vowels than consonants"""


def count_vo_con(data,i):

    if i < 0:
        return 0,0
    else:
        vowel,consonant = count_vo_con(data,i-1)
        ch = data[i].lower()
        if ch.isalpha():
            if ch in ('a','e','i','o','u'):
                vowel += 1
            else:
                consonant += 1
        return vowel,consonant

if __name__ == '__main__':
    tests=[]
    tests.append("Hello world")
    tests.append("The quick BROWN FOX")
    tests.append("aeiouxxx")
    tests.append("qwerty")
    for i in range(len(tests)):
        vowels,consonants = count_vo_con(tests[i],len(tests[i])-1)
        print("String {0} has more ".format(tests[i]),end="")
        print("vowels than consonants") if vowels > consonants else \
        print("consonants than vowels")
