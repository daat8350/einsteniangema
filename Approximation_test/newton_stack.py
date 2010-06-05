# Testing of the plane approach.
# Non-approximated version.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import array, dot, linalg
from pylab import show, savefig
from math import sqrt, sin, cos, atan, pi
from time import time
import create
import psyco

def raytrace(x0, v, mass):
    f=array([0.,0.,0.])
    for point in mass:
        r=array(point[0]-x0)
        if r[0]!=0: a=atan(float(r[1])/r[0])
        else:
            if r[1]>0: a=pi/2
            else: a=1.5*pi
        u=array([cos(a), sin(a), 0])
        r2=mag2(r)
        M=float(point[1])
        fi=M/r2
        f+=fi*u
        
    f*=G
    v+=f*dt
    v[2]=zp0                        #Global variable. Default velocity.
    x0+=v*dt 
    return x0, v

def mag2(vec):
    return float(dot(vec,vec))

def mag(vec):
    return float(linalg.norm(vec))


def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0: return (0,0,1)
    elif y<0: return (1,0,0)
    elif x>=m: return (0,1,0)
    elif y>=n: return (1,0,1)
    else: return pic[x][y]


# Stack
images=('chess.png','galaxy.png')
lenses=([((100,100,2),2000)],[((260,355,2),5000),((500,250,5),3800)])
names=('board', 'twoholes')


for i in (0,1):
    # Setup:
    log=open('log.txt', 'a')
    lens=lenses[i]
    img=mpimg.imread(images[i])
    name=names[i]

    m=len(img)
    n=len(img[0])

    imgf=create.white(m, n)

    # Parameters:
    G=50.                                # Newton constant, in some units. Probably.
    zp0=1

    dt=0.02
    maxit=30                             # Fast test

    #Iterating:
    psyco.full()
    
    print 'start'
    t0=time()

    for x in range(m):
        for y in range(n):
            z=0
            pos=array([x,y,z])
            vel=(0, 0, zp0)
            
            for it in range(maxit):
                pos, vel=raytrace(pos,vel,lens)
            imgf[x][y]=read(pos, img)
            
    t=str(time()-t0)
    print 'finish', t

    log.write(str(images[i] + '   '+ name + '   '+t +'   '+ '\n'))
    log.close()
    

    plt.imshow(imgf)
    if name!="0": savefig(name+".png")

