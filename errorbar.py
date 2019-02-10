
from pylab import *
import numpy as np
matplotlib.rcParams.update({'errorbar.capsize': 2})

# figC = figure(figsize = (8,6), dpi=150)
figR = figure(figsize = (8,6), dpi=150)


path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\\comp data\\'
# labels = ['Pristine MX', '5% OLC','10% OLC']
labels = ['0.25A/g','0.5A/g','1A/g','2A/g','3A/g','4A/g','5A/g']
sname = ['Pristine MX ESR data.txt','4% OLC ESR data.txt','8% OLC ESR data.txt']
savename = ['Ragone_MX.png' , 'Ragone_4.png', 'Ragone_8.png']
m = [0.00328,0.00304,0.00328]
um = 0.000005
uC = []

j = 2

fname= path + sname[j]
CD,ESR,Cs,Pmax,Emax = np.genfromtxt(fname, delimiter = '\t',skip_header = 1,skip_footer =0, usecols = (0,1,2,3,4),unpack =True,dtype = float)

uC = Cs*(um/m[j])

# c_ax = figC.add_subplot(111)
# c_ax.errorbar(CD,Cs,yerr = uC, marker = 'o', label = labels[j])
uESR = 0.05*ESR
print(uESR)
uE = Emax*(uC/Cs)
uP = Pmax*sqrt((um/m[j])**2  + (uESR/ESR)**2 )
# print(uP)

r_ax = figR.add_subplot(111)
for i in range(len(Pmax)):
    r_ax.errorbar(Pmax[i], Emax[i],yerr = uE[i], xerr = uP[i], fmt = 'o', label = labels[i])


# c_ax.set_xlabel('Current Density [A/g]')
# c_ax.set_ylabel(r'Specific Capacitance [F/g]')
# c_ax.legend()
# c_ax.grid()

r_ax.set_xlabel(r'Maximum Power Density [$W\cdot kg^{-1}$]')
r_ax.set_ylabel(r'Maximum Energy Density [$W \cdot h \cdot kg^{-1}$]')
r_ax.grid()
r_ax.legend()
figR.savefig(savename[j])


# show()
