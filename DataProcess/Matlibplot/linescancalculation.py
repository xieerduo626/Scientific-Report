import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from matplotlib import rcParams
import math as m
from scipy.signal import find_peaks


#Font
plt.rcParams["font.family"] = "Arial"
hfont = {'fontname':'Helvetica'}

#legend
rcParams["legend.fancybox"] = False

#size of the figure
#rcParams['figure.figsize'] = 7.5, 5.6


filename = '1.92'
angle=45
fileload= filename + '.csv'
a = np.loadtxt(fileload, delimiter=",", skiprows=8)

[numRows,numCols] = a.shape

no=1.8
ne=1.98
npsi=1.28
wavelength = 633*10**-9
cut=round(numRows/2-10)
b=np.delete(a,slice(0,cut),0)

#indexn = round(100*no-169)
x=b[:,0];
y=b[:,1];
curvename='no=' + str(no) +' ne=' + str(ne) + ' angle='+ str(angle)+'$^\circ$'#+', ne='+ str(ne)
peaks, _ = find_peaks(y, distance=15)
peaksn=4
peaks=np.delete(peaks,slice(peaksn,len(peaks)))
peaksx=x[peaks]
nprism = np.arange(peaksn-1,dtype=float)
d =np.arange(peaksn-1,dtype=float)


for i in range(0,peaksn-1):
    di=10**(-6)*(peaksx[i+1]-peaksx[i])
    nprismi=np.sqrt(npsi**2*(np.sin(angle*np.pi/180))**2+(wavelength/(2*di)+npsi*np.sin(2*angle*np.pi/180)/2)**2/(np.sin(angle*np.pi/180))**2)
    nprism[i]=round(nprismi,3)
    d[i]=di
dum=d*10**6
daverage=np.mean(dum)
dstd=np.std(dum)
naverage=np.mean(nprism)
nstd=np.std(nprism)
print (daverage,naverage)

fig, ax = plt.subplots()
ax.plot(x,y,label=curvename)
ax.plot(peaksx,y[peaks],"x",label='Position for calculation')
ax.legend(borderaxespad=0,edgecolor='black')
ax.set_ylabel('Intensity(a.u.)',fontsize=18)
ax.set_xlabel('x($\mu m$)',fontsize=18)
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
savename=filename+'_peaks.png'
plt.savefig(savename,bbox_inches='tight',transparent=True,dpi=500)

plt.show()


