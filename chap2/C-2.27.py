
class Range:
    def __init__(self, start, stop=None, step=1):
        """Initialize range instance.

        Semantics is similar to build-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:            #special case of range(n)
            start,stop = 0, start   #should be treated as if range(0,n)

        #calculate the effective length once
        self._length = max(0, (stop - start + step - 1) //step)

        #need knowledge of start and step(but not stop) to __getitem__
        self._start = start
        self._step = step


    def __len_(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self,k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)          #attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self,v):
        if not 0 <= v < self._length:
            return False
        else:
            return True


myRange = Range(10000000)
testValue = 9999999
result  = testValue in myRange
print("The value {0} is in range ? : {1}".format(testValue,result))


testValue = 2
"""If __contains__ is not implemented __getitem__ is called  implicity. It will iterate
untill the return value matches the value under test, so this is why it takes more time
for the test to evaluate values closer to the upper limit"""
result  = testValue in myRange
print("The value {0} is in range ? : {1}".format(testValue,result))





