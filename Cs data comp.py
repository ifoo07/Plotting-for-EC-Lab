# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:03:41 2018

@author: ifooh_000
"""


from pylab import *
import numpy as np


fig = figure(figsize = (8,6), dpi=150)
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\\CCCD Cs Data\\'

sname = ['Pristine MX Cs data', '4% OLC Cs data','8% OLC Cs data']

fname=[]
for i in sname:
    fname.append(path+i + '.txt')

for j in range(len(sname)):
    CD, Cs = np.genfromtxt(fname[j], delimiter = '\t', usecols = (0,1),unpack =True,dtype = float)

    ax = fig.add_subplot(111)
    ax.plot(CD,Cs,marker='o', label = sname[j])

ax.set_xlabel('Current Density [A/g]')
ax.set_ylabel('Specific Capacitance [F/g]')
ax.legend()
ax.grid()
savefig(path +'Cs data comp new.png')
show()
