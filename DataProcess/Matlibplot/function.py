#set xsticks
plt.xticks([-2.5, -1, 0, 1, 2.5],["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009", "May\n2009"]) #set specific value
plt.xticks(np.arange(5),('before 180nm', '180nm,130nm', '90nm,65nm', '45nm,32nm,22nm', '14nm & after'))

#import
a=np.loadtxt('raman1_data/Q1 Dark Wavelength.csv', delimiter=",", skiprows=18,max_rows=1043)
x=a[:,0]
