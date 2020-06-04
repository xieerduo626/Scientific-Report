import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from matplotlib import rcParams
import math as m
from scipy.signal import find_peaks


#Font
plt.rcParams["font.family"] = "Arial"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams['mathtext.rm'] = 'Arial'

#hfont = {'fontname':'Helvetica'}

#legend
rcParams["legend.fancybox"] = False

#size of the figure
rcParams['figure.figsize'] = 10, 5.6
rcParams['axes.linewidth'] = 0.75


a = np.loadtxt('45-001.csv', delimiter=",", skiprows=8)
x1=a[:,0]-10
y1=a[:,1]
b = np.loadtxt('1.86.csv', delimiter=",", skiprows=8)
x2=b[:,0]
y2=b[:,1]
c = np.loadtxt('1.92.csv', delimiter=",", skiprows=8)
x3=c[:,0]
y3=c[:,1]
d = np.loadtxt('1.98.csv', delimiter=",", skiprows=8)
x4=d[:,0]
y4=d[:,1]
fig, ax = plt.subplots()
wid=1.5
ax.plot(x1,y1,label='Isotropic n=1.8',color='black',linewidth=wid)
ax.plot(x2,y2,label=r'n$_\mathsf{o}$=1.8 n$_\mathsf{e}$=1.86',color='blue',linewidth=wid)
ax.plot(x3,y3,label=r'n$_\mathsf{o}$=1.8 n$_\mathsf{e}$=1.92',color='red',linewidth=wid)
ax.plot(x4,y4,label=r'n$_\mathsf{o}$=1.8 n$_\mathsf{e}$=1.98',color='green',linewidth=wid)
ax.set_ylabel('Intensity (Arb.)',fontsize=30)
ax.set_xlabel('X ($\mu$m)',fontsize=30)
ax.set_xlim(-7.5, 7.5)
ax.set_ylim(0, 6.3)
plt.yticks(alpha=0,fontsize=30)
plt.xticks(fontsize=30)
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True, width=0.5)
ax.legend(borderaxespad=0, edgecolor=None,framealpha=0,loc=2,fontsize=18, ncol=2)
plt.savefig('45deginterferencepattern',bbox_inches='tight',transparent=True,dpi=500)

plt.show()


