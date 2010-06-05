# Testing of the plane approach.
# Non-approximated version.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array
from pylab import show, savefig
from time import time
import create

def raytrace(x0, v, mass):
    f=array([0,0,0])
    for point in mass:
        r2=mag2(x0-point[0])
        M=point[1]
        f+=M/r2
    f*=G
    v+=f*dt
    x1=x0+v*dt
    return x1, v

def mag2(vec):
    return vec*vec

def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0 or y<0 or x>m or y>n: return (1,0,0)
    else: return pic[x][y]




# Setup:
img=mpimg.imread('chess.png')

m=len(img)
n=len(img[0])

imgf=create.white(m, n)

# Parameters:
G=50                                # Newton constant, in some units. Probably.
lens=(((1,2,3),1),((2,2,4),2))      # Just playing with the numbers, not carefully chosen.
dt=1
maxit=2                             # Fast test

#Iterating:
print 'start'
t0=time()

for x in range(m):
    for y in range(n):
        z=0
        vel=(0, 0, 1)
        for it in range(maxit):
            pos=array([x,y,z])
            pos, vel=raytrace(pos,vel,lens)
        imgf[x][y]=read(pos, img)
        


print 'finish', str(time()-t0)

plt.imshow(imgf)
show()
savefig('imgf.png')

raw_input('Ready to substract? ')

imgdiff=create.white(m, n)
for x in range(m):
    for y in range(n):
        imgdiff[x][y]=abs(imgf[x][y]-img[x][y])

plt.imshow(imgdiff)
show()
savefig('imgdiff.png')
