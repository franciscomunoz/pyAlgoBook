"""Experimental execution using bare strings,lists, list comprehensions, and 
list generators. The idea is to measure running time when characters are copied."""
import sys
from time import time

def repeated_concat():
    """Append chars directly to a string"""
    # Strings are inmutable, so a new one must be created during each += op
    letters = ''
    with open('lorem.txt', 'rU') as document:
        start = time()                 # record the start time (in seconds)
        for c in document:
            if c.isalpha():
                letters += c
        end = time()                   # record the end time (in seconds)
    return (end - start)

def append_to_list():
    """Append chars to list"""
    data = []
    letters = ''
    with open('lorem.txt', 'rU') as document:
        start = time()                 # record the start time (in seconds)
        for c in document:
            if c.isalpha():
                data.append(c)
        letters = ''.join(data)
        end = time()                   # record the end time (in seconds)
    return (end - start)

def append_to_list_comprehension():
    """Use list comprehension"""
    letters = ''
    with open('lorem.txt', 'rU') as document:
        start = time()                 # record the start time (in seconds)
        letters  = ''.join([c for c in document if c.isalpha()])
        end = time()                   # record the end time (in seconds)
    return (end - start)

def append_to_list_generator():
    """Use list generator"""
    letters = ''
    with open('lorem.txt', 'rU') as document:
        start = time()                 # record the start time (in seconds)
        letters = ''.join(c for c in document if c.isalpha())
        end = time()                   # record the end time (in seconds)
    return (end - start)



if __name__ == '__main__':

    print('Running time  for concat {0:.3f} ms'.format(repeated_concat()*1000000))
    print('Running time for append to list {0:.3f} ms'.format(append_to_list()*1000000))
    print('Running time using list comprehension  {0:.3f} ms'.format(append_to_list_comprehension()*1000000))
    print('Running time using list generators  {0:.3f} ms'.format(append_to_list_generator()*1000000))
