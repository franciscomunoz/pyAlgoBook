# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:20:14 2016

@author: francisco
"""

import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1,1024,1)

f_n1 = 8*n
f_n2 = 4*n*np.log2(n)
f_n3 = np.power(n,3)
f_n4 = np.power(2,n)
fig, an = plt.subplots()
plt.xscale('log')
plt.yscale('log')
#Plots are shown in increasing order
an.plot(f_n1)
an.plot(f_n2)
an.plot(f_n3)
an.plot(f_n4)
