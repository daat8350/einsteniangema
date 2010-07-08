# Simulation deflecting rays.
from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array, dot, linalg
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

def read(x, y, pic):                   #Eats two coordinates and returns the correspondient pixel
    if x<0: return (0,0,1)
    elif y<0: return (1,0,0)
    elif x>=m: return (0,1,0)
    elif y>=n: return (1,0,1)
    else: return pic[x][y]

def bilinear(x0, pic):
    x1=x0[0] #x
    x2=x0[1] #y
    x10=int(x1)
    x11=x10+1
    x20=int(x2)
    x21=x20+1

    t=(x1-x10)/(x11-x10)
    u=(x2-x20)/(x21-x20)
    
    #RED
    y1=read(x10, x20,pic)[0]
    y2=read(x11, x20,pic)[0]
    y3=read(x11, x21,pic)[0]
    y4=read(x10, x21,pic)[0]

    yred=(1-t)*(1-u)*y1+t+(1-u)*y2+t*u*y3+(1-t)*u*y4

    #GREEN
    y1=read(x10, x20,pic)[1]
    y2=read(x11, x20,pic)[1]
    y3=read(x11, x21,pic)[1]
    y4=read(x10, x21,pic)[1]

    ygreen=(1-t)*(1-u)*y1+t+(1-u)*y2+t*u*y3+(1-t)*u*y4

    #BLUE
    y1=read(x10, x20,pic)[2]
    y2=read(x11, x20,pic)[2]
    y3=read(x11, x21,pic)[2]
    y4=read(x10, x21,pic)[2]

    yblue=(1-t)*(1-u)*y1+t+(1-u)*y2+t*u*y3+(1-t)*u*y4

    return [yred, ygreen, yblue]


    

def dist(a,b):
#    if len(a)!=len(b): raise 'TypeError: should be list of the same length'     #We can assume that, for the shake of perfomance.
    d=0
    for i in xrange(len(a)):
       d+=(a[i]-b[i])**2
    return sqrt(d)


# Setup:
psyco.full()
t0=time()
img=mpimg.imread('galaxy.png')

m=len(img)
n=len(img[0])

imgf=create.white(m, n)


# Parameters:


lenses=[[20,[301,314]]]   # [Schwarchild radius, (vector position, R^2)]
distance=300                 # Distance from 
bes=[]

#Iterating:
for i in xrange(m):
    for j in xrange (n):
        ob=array([i,j])
        readable=True
        for lens in lenses:
            b=dist([i,j],lens[1])
            if b<=lens[0]:
                imgf[i][j]=(1,1,0)  # Ray eaten.
                readable=False
                break
            else:
                sa=lens[0]/b
                a=tan(asin(sa))
#                a=sa/sqrt(1-sa**2)
                bes.append(a)
                vdir=norm(array(lens[1])-array([i, j]))                      #Director vector.
                ob+=a*distance*vdir
                #print vdir,a, ob
        if readable==True: imgf[i][j]=bilinear(ob,img)



# Results
print max(bes)
print min(bes)
print
print

plt.imshow(imgf).set_interpolation('nearest')
print time()-t0

show()
