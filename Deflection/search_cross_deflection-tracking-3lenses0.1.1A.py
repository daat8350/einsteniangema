# Simulation deflecting rays.
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

def readblack(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0: return (0,0,0)
    elif y<0: return (0,0,0)
    elif x>=m: return (0,0,0)
    elif y>=n: return (0,0,0)
    else: return pic[x][y]

def dist(pp,b):
#    if len(pp)!=len(b): raise 'TypeError: should be list of the same length'     #We can assume that, for the shake of perfomance.
    d=0.
    for i in xrange(len(pp)):
       d+=(pp[i]-b[i])**2
    return sqrt(d)

def raytrace(obj0, lenses, ii, jj):
        obj=obj0
        for lens in lenses:
            b=dist(obj,lens[1])
            if b<=lens[0]:
                return obj0, False  # Ray eaten.
                break
            else:
                sa=lens[0]/b
                pp=tan(asin(sa))
                #pp=sa/sqrt(1-sa**2)
                vdir=norm(array(lens[1])-array([ii, jj]))                      #Director vector.
                obj+=pp*distance*vdir
                return obj, True


def a(image,lenses, center):
    mm=500
    nn=500
    imgf=create.white(mm, nn)
    imgfblack=create.white(mm, nn)
    #Iterating:
    for i in xrange(int(center[0]-mm/2), int(center[0]+mm/2)):
        for j in xrange (int(center[1]-nn/2), int(center[1]+nn/2)):
            ob=array([i,j])
            pos, readable=raytrace(ob, lenses, i, j)
            if readable==True:
                imgf[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=read(pos, image)
                imgfblack[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=readblack(pos, image)
            else:
                imgf[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=(1,1,0)
                imgfblack[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=(0,0,0)
    return imgf, imgfblack

def exporter(image, head, filecode, format='.png', digits=5, interpolation='nearest'):
    'Exports an image to file. Options:'
    '  head: a common string to open the file'
    '  filecode: a numerical index'
    '  digits: how many digits should the code have. Beware of upper limits!'
    plt.imshow(image).set_interpolation(interpolation)
    savefig(head+str(filecode).zfill(digits)+format, dpi=205)
    plt.clf()

def movelenses(lenses):
    'A function to move the lenses through the image.'
    for lens in lenses:
        lens[1]=lens[1]+array([-3, 4])
    return lenses


    
# Setup:
print 'Starting.'
psyco.full()
t0=time()
img=mpimg.imread('hdf_l.png')
top=90

m=len(img)
n=len(img[0])

#imgf=create.white(m, n)    # done inside a()

# Parameters:

#lensesdb=[[0.1,[500.3,500.5]], [0.1,[500.3,505.5]],[0.1,[500.3,510.5]], [0.07,[497.9,505.5]],[0.07,[502.5,505.5]]]
lensesdb=[[0.1,[500.3,500.5]], [0.1,[515.3,504.5]],[0.1,[500.3,510.5]]]

distance=50000                 # Distance from 

print 'Iterating...',

last=3
if last!=0:
    for i in xrange(1, last): lensedb=movelenses(lensesdb)
for it in xrange(last+1, top+1):
    central=lensesdb[2][1]
    imgf, imgfb=a(img, lensesdb, central)
    exporter(imgf,'ROI_3\cross_track3_', it)
    exporter(imgfb, 'ROI_3\black\crossblack_track3_', it)
    del(imgf)
    del(imgfb)
    lensedb=movelenses(lensesdb)
    print it,
print
print 'Finished.'


t1=time()

#Results

#plt.imshow(imgf).set_interpolation('nearest')
tf=time()
print 'Total time:', tf-t0, 's'
print 'Mean of', (t1-t0)/(top-last), 's per image.'


#show() 
