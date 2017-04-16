"""Experiment which compares the relative efficiency between calling the extend
method and performing multiple append opperations on a list instance"""
import sys
from time import time

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000

from time import time            # import time function from time module
def average_append(n):
  """Perform n appends to an empty list and return average time elapsed."""
  data = []
  start = time()                 # record the start time (in seconds)
  for k in range(n):
    data.append(None)
  end = time()                   # record the end time (in seconds)
  return (end - start) / n       # compute average per operation

def average_extend(n):
  """Perform n appends to an empty list and return average time elapsed."""
  data = []
  single_element = ['0']
  start = time()                 # record the start time (in seconds)
  for k in range(n):
    data.extend(single_element)
  end = time()                   # record the end time (in seconds)
  return (end - start) / n       # compute average per operation

if __name__ == '__main__':
    n = 10
    while n <= maxN:
        print('Average append is {0:.3f} ms for n {1}'\
            .format(average_append(n)*1000000, n))
        print('Average extend is {0:.3f} ms for n {1}'\
            .format(average_extend(n)*1000000, n))
        n *= 10


