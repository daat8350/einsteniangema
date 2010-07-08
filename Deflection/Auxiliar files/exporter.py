from __future__ import division
import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
from math import sqrt, tan, asin
from time import time
import psyco


img=mpimg.imread('hdf_l.png')

for i in xrange(1):
#    img2=img[1:30*(i+1), 20*(i+1):300] 
    plt.imshow(img).set_interpolation('nearest')
    savefig('section'+str(i).zfill(5)+'.png', dpi=205)
