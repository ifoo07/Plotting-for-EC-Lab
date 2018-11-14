from pylab import *
import numpy as np
from scipy.optimize import curve_fit
#
#
def Z(f,Rs,Q1,n1,R1,Q2,n2,R2):
    complex = Rs + (1/(Q1*2*np.pi*f*1j)**n1) + (1/(Q2*2*np.pi*f*1j)**n2)
    z_re = complex.real
    z_im= -1*complex.imag
    return z_re


path =r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\8% OLC H2SO4\\EIS\\'
sname = ['EIS_before','EIS_before_zfit','EIS_after', 'EIS_after_zfit']
header = [63,3,63,3]
fig  = plt.figure(dpi=150)
colors = ['b','b','r','r']
labels = ['Measured EIS before cycling', 'Fitted EIS before cycling','Measured EIS after cycling', 'Fitted EIS after cycling']
fname=[]
for i in range(len(sname)):
    fname.append(path + sname[i] + '.txt')

for j in range(len(sname)):
    data_z_re, data_z_im  = np.genfromtxt(fname[j], delimiter = '\t',skip_header = header[j], usecols = (0,1),unpack =True,dtype = str)

    for arr in [data_z_re, data_z_im]:
            for k in range(len(arr)):
                arr[k]=arr[k].replace(',','.')
                arr[k] = float(arr[k])

    if j == 0 or j==2:
        scatter(data_z_re, data_z_im,color = colors[j], marker = 'o', label = labels[j])
    else:
        plot(data_z_re, data_z_im, color =colors[j],linestyle = '--', label = labels[j])
legend()
grid()
xlabel(r'Re(Z) [$\Omega$]')
ylabel(r'-Im(Z) [$\Omega$]')
# savefig(path + 'EIS_fit_MX.png')
show()
