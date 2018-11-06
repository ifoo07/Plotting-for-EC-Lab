
from pylab import *
import numpy as np

fig  = figure(figsize = (8,6), dpi=150)
path = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\post activation\\CD\\'

fname = path + 'cycling_02_CP_C01.txt'

capacitance_import, C_eff_import, cycle_import  = np.genfromtxt(fname, delimiter = '\t',skip_header = 53, usecols = (0,1,2),unpack =True,dtype = str)

for arr in [capacitance_import, C_eff_import, cycle_import]:
    for k in range(len(arr)):
        arr[k]=arr[k].replace(',','.')
        arr[k] = float(arr[k])

cycle, cap, C_eff = [],[],[]
N = len(cycle_import)
for i in range(N-1):
    if cycle_import[i+1] != cycle_import[i]:
        cycle.append(cycle_import[i])
        cap.append(float(capacitance_import[i]))
        C_eff.append(C_eff_import[i])
    else: pass


cap_n = []
for j in range(len(cap)):
    cap_n.append(100*(cap[j]/cap[1]))


ax1 = fig.add_subplot(211)
ax1.plot(cycle[10:],C_eff[10:], color = 'g', marker ='o', markersize = '0.5')
from matplotlib.ticker import NullFormatter
ax1.axes.get_xaxis().set_major_formatter(NullFormatter())
ax1.set_ylabel('Coulombic Efficiency [%]')
ax1.set_ylim(top = 105, bottom = 50)
ax1.grid()


ax2 = fig.add_subplot(212)
ax2.plot(cycle[1:], cap_n[1:], marker = 'o', markersize = '0.5')
ax2.set_xlabel('Cycle number')
ax2.set_ylabel('Capacitive Retention [%]')
ax2.set_ylim(top = 105, bottom = 50)
ax2.grid()

savefig(path + 'Pristine MX Efficiency.png')
show()
