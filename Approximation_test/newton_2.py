# Testing of the plane approach.
# Non-approximated version.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array, dot, linalg
from pylab import show, savefig
from math import sqrt
from time import time
import create
import psyco

def raytrace(x0, v, mass):
    f=array([0,0,0])
    for point in mass:
        r=array([x0[0]-point[0][0], x0[1]-point[0][1], x0[2]-point[0][2]])
        r2=mag2(r)
        M=point[1]
        fi=M/r2
        f+=mag(r)*fi
    f*=G
    v+=f*dt
    v[2]=0
    x0+=v*dt
    return x0, v

def mag2(vec):
    return dot(vec,vec)

def mag(vec):
    return linalg.norm(vec)

def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0 or y<0: return (1,0,0)
    elif x>m or y>n:
        #print x, y
        return (0,1,0)
        
    else: return pic[x][y]




# Setup:
img=mpimg.imread('gal.png')
#plt.imshow(img)
#plt.draw()

m=len(img)
n=len(img[0])

imgf=create.white(m, n)

# Parameters:
G=50                                # Newton constant, in some units. Probably.
lens=(((60,80,10),10),((80,100,20),20)) # Just playing with the numbers, not carefully chosen.
dt=2
maxit=5                             # Fast test

#Iterating:
psyco.full()

print 'start'
t0=time()

for x in range(m):
    for y in range(n):
        z=0
        pos=array([x,y,z])
        vel=(0, 0, 1)
        
        for it in range(maxit):
            pos, vel=raytrace(pos,vel,lens)
        imgf[x][y]=read(pos, img)
        


print 'finish', str(time()-t0)

plt.imshow(imgf)
show()
#savefig('imgf.png')

#raw_input('Ready to substract? ')

##imgdiff=create.white(m, n)
##for x in range(m):
##    for y in range(n):
##        imgdiff[x][y]=abs(imgf[x][y]-img[x][y])
##
##plt.imshow(imgdiff)
##show()
###savefig('imgdiff.png')
