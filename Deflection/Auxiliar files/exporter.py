import matplotlib.pyplot as plt
import numpy as np
from pylab import show, savefig

img=mpimg.imread('galaxy.png')

for i in xrange(3):
    img2=img[1:30*(i+1), 20*(i+1):300] 
    plt.imshow(img2).set_interpolation('nearest')
    savefig('section'+str(i).zfill(5)+'.png')
