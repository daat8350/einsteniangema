# Simulation deflecting rays.
from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array, dot, linalg
from pylab import show, savefig
from math import sqrt
from time import time
import create
import psyco


def mag2(vec):
    return float(dot(vec,vec))

def mag(vec):
    return float(linalg.norm(vec))

def norm(vec):
    return vec/mag(vec)

def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0: return (0,0,1)
    elif y<0: return (1,0,0)
    elif x>=m: return (0,1,0)
    elif y>=n: return (1,0,1)
    else: return pic[x][y]

def dist(a,b):
#    if len(a)!=len(b): raise 'TypeError: should be list of the same length'     #We can assume that, for the shake of perfomance.
    d=0
    for i in xrange(len(a)):
       d+=(a[i]-b[i])**2
    return sqrt(d)


# Setup:
img=mpimg.imread('gal.png')

m=len(img)
n=len(img[0])

imgf=create.white(m, n)


# Parameters:


lenses=[[1,[70, 75]]]  # [Schwarchild radius, (vector position, R^2)]
bes=[]

#Iterating:
for i in range(m):
    for j in range (n):
        for lens in lenses:
            b=dist([i,j],lens[1])
            if b<lens[0]: bes.append(0.01)  # Return black.
            else: bes.append(1/b)

print max(bes)
print min(bes)

# Results
#plt.imshow(imgf).set_interpolation('nearest')
