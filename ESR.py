# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:01:09 2018

@author: ifooh_000
"""

from pylab import *
import numpy as np



"CCCD Plotter"

"User defined variables"


path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\8% OLC H2SO4\\CD\\CD\\'  # path name - be sure to use // instead of / for Windows
sname =['CD_03_CP_C01','CD_02_CP_C01','CD_01_CP_C01','CD_05_CP_C01','CD_06_CP_C01','CD_07_CP_C01','CD_08_CP_C01'] #filenames of data files (withour file extensions - will be added later automatially) to plot
labels = ['0.25A/g','0.5A/g','1A/g','2A/g','3A/g','4A/g','5A/g']
CD = [0.25,0.5,1,2,3,4,5]
mass = 0.00328

"Beginning of actual plotting code"

fig1  = figure(figsize = (8,6), dpi=150)
fig2 = figure(figsize = (8,6), dpi=150)

ESR = []
Cs = []
Pmax = []
Emax = []

fname=[]
for i in sname:
    fname.append(path +i+ '.txt')



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
    V1 = float(V[pos_t0])
    V2 = float(V[pos_t0 + 1])
    V_IR = V1-V2 # IR drop


    t0 = t[pos_t0]                      # assign t0
    t1 = t[-1]                          # assign t1 to last element of time array
    td = float(t1) - float(t0)          # calculate discharge time
    V0 = float(max(V)) - float(min(V))

    Cs.append( 4*(CD[j]*td)/V0 )

    ESR.append(V_IR/(2.0*CD[j]*mass))

    pmax_temp = ((V0**2))/(4*mass*ESR[j])
    print(ESR[j])
    Pmax.append(pmax_temp)

    Emax.append((Cs[j]*(V0**2)*1000)/(2*3600))

    d_ax = fig2.add_subplot(111)
    d_ax.scatter(Pmax[j], Emax[j],marker = 'o', label = labels[j])



d_ax.set_xlabel(r'Maximum Power Density [$W\cdot kg^{-1}$]')
d_ax.set_ylabel(r'Maximum Energy Density [$W \cdot h \cdot kg^{-1}$]')
d_ax.grid()
d_ax.legend()
fig2.savefig(path+'Ragone for 8% OLC.png')


d_ax = fig1.add_subplot(111)
d_ax.plot(CD, ESR,marker = 'o', label = labels[j])
d_ax.set_xlabel('Current Density [A/g]')
d_ax.set_ylabel(r'ESR [$\Omega$]')
d_ax.grid()
fig1.savefig(path+'ESR for 8% OLC.png')

f = open(path+'8% OLC ESR data.txt', 'w')
f.write('CD' + '\t' + 'ESR' + '\t' + 'Pmax' + '\t' + 'Emax' + '\n')
for i in range(len(CD)):
    f.write(str(CD[i]) + '\t' + str(ESR[i]) + '\t' + str(Pmax[i])+ '\t' + str(Emax[i]) + '\n')
f.close()


show()
