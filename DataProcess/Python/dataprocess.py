import numpy as np

a = np.loadtxt('data.csv', delimiter=",", skiprows=1)
wanteddata=a[2:3,4:6]


#fit
from numpy.polynomial.polynomial import polyfit

b, m = polyfit(xsmall, sizesmall, 1) #linear


#findpeaks
peaks, _ = find_peaks(y, distance=200, height=100)

