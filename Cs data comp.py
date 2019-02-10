# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:03:41 2018

@author: ifooh_000
"""


from pylab import *
import numpy as np

matplotlib.rcParams.update({'errorbar.capsize': 2})

fig = figure(figsize = (8,6), dpi=150)
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\\comp data\\'
labels = ['Pristine MX', '5% OLC','10% OLC']
sname = ['Pristine MX ESR data', '4% OLC ESR data','8% OLC ESR data']

fname=[]
for i in sname:
    fname.append(path+i + '.txt')

for j in range(len(sname)):
    CD, Cs = np.genfromtxt(fname[j], delimiter = '\t', usecols = (0,1),unpack =True,dtype = float)

    ax = fig.add_subplot(111)
    error = []
    for k in range(len(Cs)):
        error.append(Cs[k]*0.05)

    ax.errorbar(CD,Cs,yerr =error,marker='o', label = labels[j])

ax.set_xlabel('Current Density [A/g]')
ax.set_ylabel(r'ESR [$\Omega$]')
ax.legend()
ax.grid()
savefig(path +'ESR data comp new new.png')
show()
