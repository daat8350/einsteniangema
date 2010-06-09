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

def n(pos):                             #Estratified refractive index: mirage
    x=pos[1]
    n0=1                                # 1
    n1=0.4                              # 0.209764
    b=0.9                               # 2.3
    return n0+n1*(1-exp(-b*x))
    
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
    if pos[1]<0:
        return True
    else: False

def show():
    scene.visible=True
    
print "Simulation of optical paths: a mirage"

print
print

psyco.full()

## GRAPHICAL CORE
scene=display()
scene.title='Simulation of optical paths.'
scene.width=700
scene.height=500
scene.autoscale=False
scene.range=(15,15,15)  #
scene.center=(0, 9, 0)  #
scene.x=100             #
scene.y=30              #
scene.fullscreen=False
scene.exit=False
srr=frame()
scene.show_rendertime=True


## PARAMETERS
r=vector(-14, 9, 0)
rp=vector(1,-0.7,0)

dt=0.01
it=0

maxit=2800
resolution=10
fps=100

## INICIALICITING
photon=sphere(frame=srr,pos=r,radius=0.5,color=color.yellow, vel=rp)
tray=curve(frame=srr,color=color.yellow, pos=r, radius=0.1)
floor=curve(frame=srr, color=color.magenta, pos=[(-20, 0, 0), (20, 0, 0)], radius=0.05)

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
