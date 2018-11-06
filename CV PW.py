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
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Repeats\\Pristine MXene\\Pristine MX rerun\\CV\\PW\\'

sname = ['CV_PW_01_CV_C01','CV_PW_02_CV_C01','CV_PW_03_CV_C01','CV_PW_04_CV_C01','CV_PW_05_CV_C01']


mass = 0.00328 # active material mass [g]

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
    sr = 20
    for i in current:
        Cs.append(4*(float(i)/(sr*mass)))

    plt.plot(voltage[start:end], Cs[start:end])
############# end of loop ####################

plt.xlabel(r'$V_{WE}$ [V]')
plt.ylabel( 'Specific Capacitance [F/g]')
plt.grid()
plt.text(0.2,110,r'0.3V $\rightarrow$ 0.7V', fontsize = 16)
plt.savefig(path+'Potential Windows for Pristine MX.png')
plt.show()
