"""Resurvive implementation for finding min and max in a list.
   It iterates from the last element to the first by making
   recursive calls until it finally finds index 0 which is
   the base case. Then it compares values between the current
   and previous activation record in order to find the minimum
   and maximum"""

def find_min_max(data,i):
    if i == 0:
        return data[i],data[i]
    else:
        current_mini = data[i]
        current_maxi = data[i]
        """Prev values """
        mini,maxi = find_min_max(data,i-1)
        if mini > current_mini:
            mini = current_mini
        if maxi < current_maxi:
            maxi = current_maxi
        """After values are updated, a tupple is returned"""
        return mini,maxi

if __name__ == '__main__':

    tests=[]
    tests.append([1,2,4,5,6,7,89,9,0])
    tests.append([833,3,3,3,3,311,-1])
    tests.append([0])

    for i in range(len(tests)):
        min,max = find_min_max(tests[i],len(tests[i])-1)
        print("The minimun = {0} and maximun = {1} in list = {2}".format(min,max,tests[i]))
