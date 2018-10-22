# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:19:10 2018

@author: ifooh_000

Plotter for CV scanrates 8% OLC

Irfan Habib
"""


import matplotlib.pyplot as plt
import numpy as np

path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\CV\\SR\\'
fig  = plt.figure(dpi=150)

sname = ['CV_lowscan_01_CV_C01', 'CV_lowscan_02_CV_C01','CV_sr_01_CV_C01', 'CV_sr_02_CV_C01', 'CV_sr_03_CV_C01', 'CV_sr_04_CV_C01', 'CV_sr_05_CV_C01', 'CV_sr_06_CV_C01', 'CV_sr_07_CV_C01']

scanrate = [5,10,20,40,50,75,100,150,200]
labels = ['5mV/s','10mV/s','20mV/s','40mV/s','50mV/s','75mV/s','100mV/s','150mV/s','200mV/s']

mass = 0.00328 #g 
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