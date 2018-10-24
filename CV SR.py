# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:19:10 2018

@author: Irfan Habib

Plotter for CV scanrates from EC Lab software

"""


import matplotlib.pyplot as plt
import numpy as np


"""User defined variables"""

path = r'' # path name - be sure to use // instead of / for Windows
sname = [] # file names of data to be plotted
scanrate = [5,10,20,40,50,75,100,150,200] #scan rates from data
labels = ['5mV/s','10mV/s','20mV/s','40mV/s','50mV/s','75mV/s','100mV/s','150mV/s','200mV/s'] #scan rate labels, must correlate with above
mass = 0.00328 #g - mass of active material

"""beginning of actual plotting code"""

fig  = plt.figure(dpi=150)
fname=[]
for i in sname:
    fname.append(path+i + '.txt')
################# beginning of loop ##############
for j in range(len(sname)):
    voltage, current, cycle = np.genfromtxt(fname[j], delimiter = '\t',skip_header = 57,skip_footer =1, usecols = (0,1,2),unpack =True,dtype = str)

    for arr in [voltage, current, cycle]:
            for k in range(len(arr)):
                arr[k]=arr[k].replace(',','.')
                arr[k] = float(arr[k])

    start = cycle.tolist().index('2.0')
    try:
        end = cycle.tolist().index('3.0')-1
    except:
        end = len(cycle)-1

    Cs = []
    sr = scanrate[j]
    for i in current:
        Cs.append(float(i)/(sr*mass))

    plt.plot(voltage[start:end], Cs[start:end], label = labels[j])
############# end of loop ####################

plt.xlabel(r'$V_{WE}$ [V]')
plt.ylabel( 'Specific Capacitance [F/g]')
plt.legend()
plt.grid()
plt.savefig(path+'Scan rates for Pristine MX.png')
plt.show()
