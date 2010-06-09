import numpy
from visual import *
##try: from visual import *
##except: pass
import psyco
#import povexport

# Notes:
# The axis go like
#
#   ^  Z
#   |
#   |
#   |
#   |
#   |
# Y 0 ------------> -X
#

def n(pos):                             #Radial refractive index: Selfoc fiber
    x=pos[0]
    y=pos[1]
    z=pos[2]                                
    e=3.7                              
    return e**((-(z-1)**2))
    
def gradn(pos):
    x=pos[0]
    y=pos[1]
    z=pos[2]

    h=0.002
    hh=2*h

    xx=(n(vector(x+h, y, z))-n(vector(x-h, y, z)))/hh
    yy=(n(vector(x, y+h, z))-n(vector(x, y-h, z)))/hh
    zz=(n(vector(x, y, z+h))-n(vector(x, y, z-h)))/hh

    return vector(xx,yy,zz)

def check(pos):
    #if pos[1]<0:
    #    return True
    return False

def show():
    scene.visible=True
    
print "Simulation of optical paths: exercise 7"

print
print

psyco.full()

## GRAPHICAL CORE
scene=display()
scene.title='Simulation of optical paths.'
scene.width=700
scene.height=200
scene.autoscale=False
scene.range=(16,16,16)  #
scene.center=(0, 0, 0)  #
scene.x=100             #
scene.y=20              #
scene.fullscreen=False
scene.exit=False
srr=frame()
scene.show_rendertime=True
scene.forward=(0,-1,0)
scene.up=(0,0,1)


## PARAMETERS
r=vector(15, 0, 0)
rp=vector(-1,0,0)

dt=0.0005
it=0

maxit=60000
resolution=200
fps=100
k=0

## INICIALICITING
photon=sphere(frame=srr,pos=r,radius=0.5,color=color.yellow, vel=rp)
tray=curve(frame=srr,color=color.yellow, pos=r, radius=0.1)


print "Starting..."

## ITERATING

while True:
    for i in xrange(resolution):
        rpp=n(r)*gradn(r)
        rp+=rpp*dt
        r+=rp*dt
        it+=1

    photon.pos=r
    tray.append(pos=r)

    if check(r)==True:
        break
    
    
    if it>=maxit:
        break

    #if k<10: povexport.export(filename= "Selfoc 00%d.pov" % k)
    #elif k<100: povexport.export(filename= "Selfoc 0%d.pov" % k)
    #elif k<1000: povexport.export(filename= "Selfoc %d.pov" % k)
    #k+=1
    rate(fps)

print "Done"
