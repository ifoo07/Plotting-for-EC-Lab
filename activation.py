# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:19:10 2018

@author: ifooh_000

Plotter for CV potential windows 4% OLC

Irfan Habib
"""


import matplotlib.pyplot as plt
import numpy as np


fig  = plt.figure(dpi=150)
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\8% OLC H2SO4\\'  # path name - be sure to use // instead of / for Windows
sname = ['test1_C01', 'test2_CV_C01']
labels = ['before activation','after 1A/g activation']
mass = 0.00328 # active material mass [g]

fname=[]
for i in sname:
    fname.append(path+i + '.txt')
################# beginning of loop ##############
for j in range(len(sname)):
    voltage, current, cycle = np.genfromtxt(fname[j], delimiter = '\t',skip_header = 72,skip_footer =1, usecols = (0,1,2),unpack =True,dtype = str)

    for arr in [voltage, current, cycle]:
            for k in range(len(arr)):
                arr[k]=arr[k].replace(',','.')
                arr[k] = float(arr[k])



    Cs = []
    sr = 20
    for i in current:
        Cs.append(4*float(i)/(sr*mass))

    plt.plot(voltage, Cs, label = labels[j])
############# end of loop ####################

plt.xlabel(r'$V_{WE}$ [V]')
plt.ylabel( 'Specific Capacitance [F/g]')
plt.legend()
plt.grid()
plt.savefig(path+'activation for 8% OLC_MX.png')
plt.show()
