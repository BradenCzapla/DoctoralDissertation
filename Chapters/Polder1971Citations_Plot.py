# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 20:06:22 2018
Created by Lab 127
"""

from __future__ import absolute_import, division, print_function
#from builtins import *

import numpy as np
#import scipy as sp
#import mpmath as mp
from collections import Counter

import matplotlib.pyplot as plt
from matplotlib import rcParams
import time
import os

start = time.time()
plt.close('all')
cwd = os.getcwd()

rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 1.5

color_cycle = [(148./255., 103./255., 189./255.), (44./255, 160./255., 44./255.), (214./255., 39./255., 40./255.), (31./255., 119./255., 180./255.), (127./255., 127./255., 127./255.), (206./255., 103./255., 0./255.)]
###############################################################################

year_list = np.genfromtxt('Polder1971Citations_20181202.csv', dtype=float, delimiter=',', skip_header=1)

years = Counter(year_list).keys() # equals to list(set(words))
freqs = Counter(year_list).values() # counts the elements' frequency


fontsize1 = 28
labelsize1 = 24
legendsize = 24

plt.figure('Polder and van Hove Citationa',figsize=(9.71,6.0))
ax = plt.subplot(1,1,1)


plt.hist(year_list, bins=44, range=(1971,2018))

plt.xlim(1970,2020)
plt.ylim(0,150)

plt.xlabel('Year', fontsize=fontsize1)
plt.ylabel('New Citations', fontsize=fontsize1)

ax.tick_params(axis='x', pad=10)
plt.tick_params(labelsize=labelsize1)
plt.minorticks_on()  
#ax_lll_1.set_yticks([1e5,1e7,1e9], minor=True)
ax.tick_params(axis = 'both', which = 'major', width = 1.5, length = 8, direction='in')
ax.tick_params(axis = 'both', which = 'minor', width = 1.5, length = 4, direction='in')
#ax.axes.get_xaxis().set_ticklabels([])

ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')


plt.plot([1971,1996],[23,23], linewidth=2, color='black')
plt.plot([1971,1971],[23,5], linewidth=2, color='black')
plt.plot([1996,1996],[23,5], linewidth=2, color='black')
plt.plot([1983.5,1983.5],[23,40], linewidth=2, color='black')

ax.text(1983.5, 45, "23 Citations Before 1997", ha="center", va="center", size=labelsize1-4)

## Number of citations before 1997 - 23
# print( np.sum(freqs[:15]) )


#plt.savefig('Polder1971Citations.pdf', bbox_inches='tight', format='pdf')






















###############################################################################
end = time.time()
print("Runtime:", end - start, "seconds")
