
f = open('latin_paragraphs.txt')

file_contents = f.read().lower()
ocurrences = [0] * 26
#count ocurrences
for k in file_contents:
    print(ord(k))
    if k >= 'a' and k <= 'z':
        ocurrences[ord(k) - 97]+=1

#print ocurrences in file
for k in range(len(ocurrences)):
    print("{0} : {1}".format(chr(k + 97), "*" * ocurrences[k]))

f.close()
