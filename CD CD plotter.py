# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:01:09 2018

@author: ifooh_000
"""

from pylab import *
import numpy as np

fig1  = figure(figsize = (8,6), dpi=150)
fig2 = figure(figsize = (8,6), dpi=150)
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Repeats\\Pristine MXene\\Pristine MX rerun\\CD\\CD\\CD files to plot\\'

"CCCD Plotter"


sname =['CD_cd_01_CP_C01','CD_cd_02_CP_C01','CD_cd_03_CP_C01','CD_cd_04_CP_C01','CD_cd_05_CP_C01','CD_cd_06_CP_C01','CD_cd_07_CP_C01','CD_cd_08_CP_C01','CD_cd_09_CP_C01','CD_cd_10_CP_C01','CD_cd_11_CP_C01','CD_cd_12_CP_C01'] #filenames of data files (withour file extensions - will be added later automatially) to plot

labels = ['0.25A/g','0.3A/g','0.4A/g','0.5A/g','1A/g','2A/g','3A/g','4A/g','5A/g','10A/g','15A/g','20A/g']
CD = [0.25,0.3,0.4,0.5,1,2,3,4,5,10,15,20]
fname=[]
for i in sname:
    fname.append(path +i+ '.txt')

Cs = []

for j in range(len(sname)):
    time,voltage, cycle = np.genfromtxt(fname[j], delimiter = '\t',skip_header = 57,skip_footer =1, usecols = (0,1,2),unpack =True,dtype = str)

    for arr in [voltage, time, cycle]:
            for k in range(len(arr)):
                arr[k]=arr[k].replace(',','.')
                arr[k] = float(arr[k])

    start = cycle.tolist().index('2.0')
    try:
        end = cycle.tolist().index('3.0')-1
    except:
        end = len(cycle)-1


    norm = float(time[start])
    for k in range(start,end,1):
        time[k] = float(time[k])- norm

    V = voltage[start:end]
    t = time[start:end]

    pos_t0 = V.tolist().index(max(V))   # find index of t0
    t0 = t[pos_t0]                      # assign t0
    t1 = t[-1]                          # assign t1 to last element of time array
    td = float(t1) - float(t0)          # calculate discharge time
    V0 = float(max(V)) - float(min(V))

    Cs.append( 4*(CD[j]*td)/V0 )


    d_ax = fig1.add_subplot(111)
    d_ax.plot(t, V, label = labels[j])

d_ax.set_xlabel(r'time[s]')
d_ax.set_ylabel(r'$V_{WE}$')
d_ax.legend(loc=1)
d_ax.grid()
fig1.savefig(path+'Current Densities for Pristine MX.png')


Cs_ax = fig2.add_subplot(111)

Cs_ax.plot(CD,Cs, marker = 'o')
Cs_ax.set_xlabel('Current Density [A/g]')
Cs_ax.set_ylabel('Specific Capacitance [F/g]')
Cs_ax.grid()
fig2.savefig(path+'Cs vs CD for Pristine MX.png')

f = open(path+'Pristine MX Cs data.txt', 'w')
for i in range(len(Cs)):
    f.write(str(CD[i]) + '\t' + str(Cs[i]) + '\n')
f.close()


show()
