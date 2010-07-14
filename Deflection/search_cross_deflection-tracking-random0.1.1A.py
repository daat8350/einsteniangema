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
import os
from random import random



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
    x=[]
    y=[]
    for lens in lenses:
        coord=lens[1]
        x.append(coord[0])
        y.append(coord[1])
    m1=(max(x)-min(x))*30
    n1=(max(y)-min(y))*30
    mm=round(max([m1,n1]))
    nn=mm
    #mm=500
    #nn=500
    imgf=create.white(mm, nn)
    imgfblack=create.white(mm, nn)
    imgraw=create.white(mm, nn)
    #Iterating:
    for i in xrange(int(center[0]-mm/2), int(center[0]+mm/2)):
        for j in xrange (int(center[1]-nn/2), int(center[1]+nn/2)):
            ob=array([i,j])
            pos, readable=raytrace(ob, lenses, i, j)
            if readable==True:
                imgf[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=read(pos, image)
                imgfblack[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=readblack(pos, image)
                imgraw[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=readblack(array([i,j]), image)
            else:
                imgf[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=(1,1,0)
                imgfblack[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=(0,0,0)
                imgraw[i-int(center[0]-mm/2)][j-int(center[1]-nn/2)]=readblack(array([i,j]), image)
    return imgf, imgfblack, imgraw

def exporter(image, head, filecode, format='.png', digits=5, interpolation='nearest'):
    'Exports an image to file. Options:'
    '  head: a common string to open the file'
    '  filecode: a numerical index'
    '  digits: how many digits should the code have. Beware of upper limits!'
    plt.imshow(image).set_interpolation(interpolation)
    savefig(head+str(filecode).zfill(digits)+format)
    plt.clf()

def movelenses(lenses):
    'A function to move the lenses through the image.'
    a=2
    for lens in lenses:
        lens[0]=abs(lens[0]+(random()-0.5)*0.03)
        lens[1]=lens[1]+array([(random()-0.5)*a, (random()-0.5)*a])
    return lenses

def exportlenses(lenses, filename, n):
    db=''
    for lens in lenses:
        db+=str(lens[0])+str(lens[1])           # 1*0.1[500.3,500.5]0.2[500.3,508.5]->split('*'), split(']'), split('['), split(',')
    line=str(n)+'*'+db+'\n'
    filename.write(line)
    filename.flush()
    os.fsync(filename.fileno())

def centerpoint(lenses):
    pos=array([0,0])
    weight=0
    for lens in lenses:
        weight+=lens[0]
        pos+=lens[0]*array(lens[1])
    pos=pos/weight
    return pos


print "Wellcome to the searching of Einstein's cross through random moving lenses"
print

# Setup:
print 'Starting.'
psyco.full()
t0=time()
img=mpimg.imread('hdf_l.png')
top=900

m=len(img)
n=len(img[0])


# Parameters:

#lensesdb=[[0.1,[500.3,500.5]], [0.1,[500.3,505.5]],[0.1,[500.3,510.5]], [0.07,[497.9,505.5]],[0.07,[502.5,505.5]]]
lensesdb=[[0.1,[500.3,500.5]], [0.2,[500.3,508.5]],[0.1,[500.3,516.5]]]


textfilename='randomlensesfile.txt'
dir1='random_'
dir2='randomblack_'
dir3='randomraw_'
lensesfile=open(textfilename, 'w+')

distance=50000                 # Distance from 

print 'Iterating...',

last=0
if last!=0:
    for i in xrange(1, last): lensedb=movelenses(lensesdb)

for it in xrange(last+1, top+1):
    central=centerpoint(lensesdb)
    exportlenses(lensesdb,lensesfile, it)
    imagf, imagfb, imagraw=a(img, lensesdb, central)
    exporter(imagf,dir1, it)
    exporter(imagfb, dir2, it)
    exporter(imagraw, dir3, it)
    del(imagf)
    del(imagfb)
    del(imagraw)
    lensesdb=movelenses(lensesdb)
    print it,

lensesfile.close()

print
print 'Finished.'


t1=time()

#Results

#plt.imshow(imgf).set_interpolation('nearest')
tf=time()
print 'Total time:', tf-t0, 's'
print 'Mean of', (t1-t0)/(top-last), 's per image.'


#show() 
