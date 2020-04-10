import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from matplotlib import rcParams
import math as m

#Font
plt.rcParams["font.family"] = "sans-serif"
hfont = {'fontname':'Helvetica'}

#legend
rcParams["legend.fancybox"] = False

#data
x = np.linspace(-np.pi,np.pi,100)
y1 = np.sin(x)
y2 =np.cos(x)

#plot
fig, ax = plt.subplots()
ax.plot(x,y1,color='blue', linewidth=0.5, label="sin(x)")
ax.plot(x,y2,color='green', linewidth=0.5, label="cos(x)")
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1,1)
ax.set_title('Size Distrubution of Corn Stem Cells',fontsize=18)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel(r'y($\mu m^2$)',fontsize=14)

#design
ax.minorticks_on()
ax.legend(borderaxespad=0,edgecolor='black')
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.savefig("Q31.png",bbox_inches='tight',transparent=True,dpi=500)
plt.show()








