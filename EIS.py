from pylab import *
import numpy as np
from scipy.optimize import curve_fit
#
#
# def Z(f,Rs,Q1,n1,R1,Q2,n2,R2):
#     ans = Rs + (1/(Q1*2*np.pi*f)**n1) + (1/(Q1*2*np.pi*f)**n1)
#     return ans
path =r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\'
sname = ['EIS_C01_1', 'EIS_C01_zfit 1']
header = [63,3]
fig  = plt.figure(dpi=150)
labels = ['Experimental data', 'Equivalent series circuit fit']
fname=[]
for i in range(len(sname)):
    fname.append(path + sname[i] + '.txt')

for j in range(len(sname)):
    z_re, z_im  = np.genfromtxt(fname[j], delimiter = '\t',skip_header = header[j], usecols = (0,1),unpack =True,dtype = str)

    for arr in [z_re, z_im]:
            for k in range(len(arr)):
                arr[k]=arr[k].replace(',','.')
                arr[k] = float(arr[k])

    if j == 0:
        scatter(z_re, z_im,marker = 'o', label = labels[j])
    else:
        plot(z_re, z_im, color ='r', linestyle = '--', label = labels[j])
legend()
show()
