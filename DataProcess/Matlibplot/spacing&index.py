import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from matplotlib import rcParams
import math as m
from scipy.signal import find_peaks


#Font
plt.rcParams["font.family"] = "Arial"
hfont = {'fontname':'Helvetica'}
plt.rcParams["mathtext.fontset"] = "cm"

#legend
rcParams["legend.fancybox"] = False

#size of the figure
rcParams['figure.figsize'] = 8, 5.6

rcParams['axes.linewidth'] = 0.75

x=['Isotropic\nn=1.8','n$_\mathsf{o}$=1.8\nn$_\mathsf{e}$=1.86','n$_\mathsf{o}$=1.8\nn$_\mathsf{e}$=1.92','n$_\mathsf{o}$=1.8\nn$_\mathsf{e}$=1.98']
spacing=[0.687,0.689,0.676,0.677]
n=[1.805,1.802,1.811,1.812]
fig, ax = plt.subplots()
ax.scatter(x[0],spacing[0],marker='o',c='white',edgecolors='black',label='d$_{\mathsf{fringes}}$')
ax.scatter(x[1],spacing[1],marker='o',c='white',edgecolors='black')
ax.scatter(x[2],spacing[2],marker='o',c='white',edgecolors='black')
ax.scatter(x[3],spacing[3],marker='o',c='white',edgecolors='black')
ax.scatter(-2,0.6,marker='s',c='white',edgecolors='blue',label='Calculated n$_{\mathsf{prism}}$')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax.set_ylabel('d$_{\mathsf{fringes}}$ ($\mu$m)',fontsize=30)
#ax.set_xlabel(fontsize=30)
ax.set_xlim(-1,4)
ax.set_ylim(0.6, 0.7)
#plt.yticks(alpha=0)
ax2 = ax.twinx()
ax2.scatter(x[0],n[0],marker='s',c='white',edgecolors='blue')
ax2.scatter(x[1],n[1],marker='s',c='white',edgecolors='blue')
ax2.scatter(x[2],n[2],marker='s',c='white',edgecolors='blue')
ax2.scatter(x[3],n[3],marker='s',c='white',edgecolors='blue')
ax2.set_ylabel('Calculated n$_{{\mathsf{prism}}}$',fontsize=30,color='blue')
ax2.set_ylim(1.79, 1.85)
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=False, width=0.5)
ax2.tick_params(direction='in', right=True, width=0.5)
ax2.tick_params(axis='y', colors='blue')
plt.yticks(fontsize=20)
fig.tight_layout()
ax.legend(borderaxespad=0, edgecolor=None,framealpha=0,loc=1,fontsize=15)
plt.savefig('spacing',bbox_inches='tight',transparent=True,dpi=500)

plt.show()


