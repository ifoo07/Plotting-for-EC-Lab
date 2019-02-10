
from pylab import *
import numpy as np

fig  = figure(figsize = (8,6), dpi=150)
ax2 = fig.add_subplot(111)
path1 = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\Pristine H2SO4 rerun\\post activation\\CD\\'
path2 = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\4% OLC H2SO4\\CD\\'
path3 = r'D:\\Google Drive\\Masters Research - Supercapacitor\\Data\\EC data\\2 Electrode\\Swagelok T-Type\\8% OLC H2SO4\\CD\\'
fname1 = path1 + 'cycling_02_CP_C01.txt'
fname2 = path2 + 'cycling_01_CP_C01.txt'
fname3 = path3 + 'cycling_01_CP_C01.txt'
fname = [fname1,fname2, fname3]



for f in fname:
    capacitance_import, C_eff_import, cycle_import  = np.genfromtxt(f, delimiter = '\t',skip_header = 53, usecols = (0,1,2),unpack =True,dtype = str)

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


    # ax1 = fig.add_subplot(211)
    # ax1.plot(cycle[10:],C_eff[10:], color = 'g', marker ='o', markersize = '0.5')
    # from matplotlib.ticker import NullFormatter
    # ax1.axes.get_xaxis().set_major_formatter(NullFormatter())
    # ax1.set_ylabel('Coulombic Efficiency [%]')
    # ax1.set_ylim(top = 105, bottom = 50)
    # ax1.grid()



    ax2.plot(cycle[1:], cap_n[1:], marker = 'o', markersize = '0.5')
    ax2.set_xlabel('Cycle number')
    ax2.set_ylabel('Capacitive Retention [%]')
    ax2.set_ylim(top = 105, bottom = 50)
    ax2.grid()

path = r'C:\\Users\\ifooh_000\\Desktop\\graphs for ken\\'
savefig(path + 'Capacitive retention KEN.png')
show()