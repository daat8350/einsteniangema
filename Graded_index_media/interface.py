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

def n(pos):                             #Estratified refractive index: interface
    n0=1.0                                # 1
    n1=2.0                              # 2
    if pos[1]<4:
        return n1
    else: return n0
    
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
    return False

def show():
    scene.visible=True
    
print "Simulation of optical paths: an optical interface."

print
print

psyco.full()

## GRAPHICAL CORE
scene=display()
scene.title='Simulation of optical paths.'
scene.width=500
scene.height=500
scene.autoscale=False
scene.range=(10,15,15)  #
scene.center=(0, 4, 0)  #
scene.x=100             #
scene.y=30              #
scene.fullscreen=False
scene.exit=False
srr=frame()
scene.show_rendertime=True


## PARAMETERS
r=vector(-7, 9, 0)
rp=vector(1,-0.7,0)

dt=0.005
it=0

maxit=2000
resolution=20
fps=30

## INICIALICITING
photon=sphere(frame=srr,pos=r,radius=0.5,color=color.yellow, vel=rp)
tray=curve(frame=srr,color=color.yellow, pos=r, radius=0.1)
floor=curve(frame=srr, color=(0.3,0.4,1), pos=[(-20, 4, 0), (20, 4, 0)], radius=0.05)

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
