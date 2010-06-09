import numpy
from visual import *
##try: from visual import *
##except: pass
import psyco

# Notes:
# The axis go like
#
#   ^  Y
#   |
#   |
#   |
#   |
#   |
# Z 0 ------------> X
#

def n(pos):                             #Spherical refractive index: Maxwell fisheye
    r=mag(pos)
    a=3.6                               # 
    return 7/(1+(r/a)**2)
    
def gradn(pos):
    x=pos[0]
    y=pos[1]
    z=pos[2]

    h=0.0002
    hh=2*h

    xx=(n(vector(x+h, y, z))-n(vector(x-h, y, z)))/hh
    yy=(n(vector(x, y+h, z))-n(vector(x, y-h, z)))/hh
    zz=(n(vector(x, y, z+h))-n(vector(x, y, z-h)))/hh

    return vector(xx,yy,zz)

def check(pos):
    if mag(pos)<0.1:
        return True
    else: False

def show():
    scene.visible=True

def hide():
    scene.visible=False
    
print "Simulation of optical paths: Maxwell fisheye"

print
print

psyco.full()

## GRAPHICAL CORE
scene=display()
scene.title='Simulation of optical paths.'
scene.width=500
scene.height=500
scene.autoscale=False
scene.range=(15,15,15)  #
scene.center=(0, 0, 0)  #
scene.x=100             #
scene.y=30              #
scene.fullscreen=False
scene.exit=False
srr=frame()
scene.show_rendertime=True


## PARAMETERS
r=vector(-9, 0, 0)
rp=vector(0,-1,0)

dt=0.001
it=0

maxit=18000
resolution=40
fps=100

## INICIALICITING
photon=sphere(frame=srr,pos=r,radius=0.5,color=color.yellow, vel=rp)
tray=curve(frame=srr,color=color.yellow, pos=r, radius=0.1)
center=sphere(frame=srr, color=color.magenta, pos=(0,0,0), radius=0.1)

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
    
    rate(fps)

print "Done"
