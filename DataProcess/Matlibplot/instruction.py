import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import math as m

#Font
plt.rcParams["font.family"] = "sans-serif"
hfont = {'fontname':'Helvetica'}

#data
x = np.linspace(-np.pi,np.pi,100)
y = np.sin(x)

#plot
fig, ax = plt.subplots()
ax.plot(x,y,color='blue', linewidth=0.5, label="sin(x)")
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1,1)
ax.set_title('Size Distrubution of Corn Stem Cells',fontsize=18, **hfont)
ax.set_xlabel('x',fontsize=14,**hfont)
ax.set_ylabel(r'y($\mu m^2$)',fontsize=14,**hfont)
ax.legend(loc=2) #need to be filled

#design
ax.minorticks_on()
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.show()








