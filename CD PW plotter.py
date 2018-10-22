# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:01:09 2018

@author: ifooh_000
"""

from pylab import *
import numpy as np

fig  = figure(dpi=150)

"CCCD Plotter"

path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\CD\\PW\\'
     
sname =['CD_pw_01_CP_C01','CD_pw_02_CP_C01','CD_pw_03_CP_C01','CD_pw_04_CP_C01','CD_pw_05_CP_C01']

fname=[]
for i in sname:
    fname.append(path+i + '.txt')
    
V,Cycle,t = [],[],[]

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
        
    plt.plot(time[start:end], voltage[start:end])
    
xlabel(r'time[s]')
ylabel(r'$V_{WE}$')
text(8,0.65, r'0.3V $\rightarrow$ 0.7V',fontsize = 16,rotation = 45)
grid()
savefile = path+'Potential Windows (CD) for Pristine MX' 

savefig(savefile+'.png')
show()