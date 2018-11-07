# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:19:10 2018

@author: Irfan Habib

Plotter for CV scanrates from EC Lab software

"""


import matplotlib.pyplot as plt
import numpy as np


"""User defined variables"""
pathS = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\comp data\\'
pathMX =  r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\CV\\SR\\'
path4 = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\4% OLC H2SO4\\CV\\SR\\' # path name - be sure to use // instead of / for Windows
path8 =  r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\8% OLC H2SO4\\CV\\SR\\'
path = [pathMX,path4,path8]
sname = 'CV_sr_03_CV_C01' # file names of data to be plotted
scanrate = 50
labels = ['Pristine MX', 'MX/OLC (5%)', 'MX/OLC (10%)'] #scan rate labels, must correlate with above
mass = [0.00328,0.00304,0.00328] #g - mass of active material

"""beginning of actual plotting code"""

fig  = plt.figure(dpi=150)
fname=[]
for i in range(len(path)):
    fname.append(path[i]+sname + '.txt')
################# beginning of loop ##############
for j in range(len(fname)):
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
    sr = scanrate
    for i in current:
        Cs.append(4*(float(i)/(sr*mass[j])))

    plt.plot(voltage[start:end], Cs[start:end], label = labels[j])


############# end of loop ####################

plt.xlabel(r'$V_{WE}$ [V]')
plt.ylabel( 'Specific Capacitance [F/g]')
plt.legend()
plt.grid()
fig.savefig(pathS+'SR_comp.png')
plt.show()
