import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from pylab import show, savefig

from random import random

    
img=mpimg.imread('stinkbug.png')

m=len(img)
n=len(img[0])

for i in xrange(m):
    for j in xrange(n):
        img[i][j]=img[i][j]/2


#plot
plt.imshow(img)
show()
name=raw_input("filename: ")
if name!="0": savefig(name+".png")

