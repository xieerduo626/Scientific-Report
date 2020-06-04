import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


fig, ax = plt.subplots()
img = mpimg.imread('n1.98.png')
imgplot = plt.imshow(img)
#ax.set_ylabel('Z ($\mu m$)',fontsize=18)
ax.set_xlabel('X ($\mu m$)',fontsize=18)
plt.xticks(np.arange(0, len(img[1])+1, step=len(img[1])/4),[-10,-5,0,5,10])
plt.yticks(np.arange(0, len(img)+1, step=len(img)/3),[30,20,10,0])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(bottom=False, top=False, left=False, right=False)
plt.savefig('n1.98axis.png',bbox_inches='tight',transparent=True,dpi=500)
plt.show()


