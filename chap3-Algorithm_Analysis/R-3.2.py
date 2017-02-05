# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:44:30 2016

@author: francisco
"""

import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1,30,1)

f_n1 = 8*n*np.log2(n)
f_n2 = 2*np.power(n,2)
fig, an = plt.subplots()
an.plot(f_n1)
an.plot(f_n2)
#Find the index in which fn_1 start exhibiting better performance
index = 0
for i in range(len(n)):
    if f_n2[i] == f_n1[i]:
        index = i
        break

print "The index in which fn_1(A) shows better performance is : {0}".format(index + 1)


