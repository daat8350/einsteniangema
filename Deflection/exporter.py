from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
from math import sqrt, tan, asin
from time import time
import create
import psyco


img=mpimg.imread('galaxy.png')
it=0

for i in xrange(3):
    img2=img[1:30*(i+1), 20*(i+1):300] 
    plt.imshow(img2).set_interpolation('nearest')
    savefig('section'+str(i)+'.png')
