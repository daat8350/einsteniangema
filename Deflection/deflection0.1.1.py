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

def read(x0, pic):                   #Eats an array and returns the correspondient pixel
    x=round(x0[0])
    y=round(x0[1])
    if x<0: return (0,0,1)
    elif y<0: return (1,0,0)
    elif x>=m: return (0,1,0)
    elif y>=n: return (1,0,1)
    else: return pic[x][y]

def dist(a,b):
#    if len(a)!=len(b): raise 'TypeError: should be list of the same length'     #We can assume that, for the shake of perfomance.
    d=0
    for i in xrange(len(a)):
       d+=(a[i]-b[i])**2
    return sqrt(d)

def raytrace(obj0):
        obj=obj0
        readable=True
        for lens in lenses:
            b=dist(obj,lens[1])
            if b<=lens[0]:
                return obj0, False  # Ray eaten.
                readable=False
                break
            else:
                sa=lens[0]/b
                a=tan(asin(sa))
                #a=sa/sqrt(1-sa**2)
                vdir=norm(array(lens[1])-array([i, j]))                      #Director vector.
                obj+=a*distance*vdir
        if readable==True: return obj, True

# Setup:
psyco.full()
t0=time()
img=mpimg.imread('galaxy.png')

m=len(img)
n=len(img[0])

imgf=create.white(m, n)



# Parameters:

lenses=[[2,[301,314]]]   # [Schwarchild radius, (vector position, R^2)]
#lenses=[[2,[100,100]]]   # [Schwarchild radius, (vector position, R^2)]
#lenses=[[1, [272.63826437460227, 258.79159753184547]], [1, [276.95728331738718, 208.9239361514922]], [1, [261.65412099275017, 206.30696874469248]], [1, [231.99043936911897, 238.33683656721212]], [1, [251.5012749156291, 266.11741633248465]], [1, [226.73724535502544, 229.77943637968474]], [1, [266.4110827780583, 209.46044604432589]], [1, [225.64594147229775, 291.02562377782181]], [1, [235.53337397403948, 227.5711808611083]], [1, [220.45044318506228, 257.23548166177187]], [1, [223.65973580111097, 274.10923973302852]], [1, [278.46526064687652, 261.2376955226178]], [1, [286.77774817562732, 265.81459607558418]], [1, [276.16096242873186, 218.43141057381138]], [1, [246.0090783627569, 204.94758833327739]], [1, [250.32496241579508, 285.21523856695075]], [1, [262.97917135198412, 278.74036133420003]], [1, [236.85772292205294, 263.23797660843536]], [1, [246.44430302664978, 259.50877373310016]], [1, [220.11718516828202, 281.76794288432893]], [1, [296.00967181855236, 238.19969729290253]], [1, [270.55899362161301, 259.9108930556273]], [1, [229.99110815941424, 237.98875005803851]], [1, [210.42842666990563, 297.67653759366846]], [1, [234.13845345422504, 241.52707941842783]], [1, [299.62403311742662, 245.58292701843891]], [1, [287.80443275590869, 291.69144406152526]], [1, [220.7481985055708, 265.15627784841854]], [1, [245.57828335572816, 250.97131739091577]], [1, [273.56231582674138, 299.6608679729502]], [1, [216.69935649482886, 242.27405628755338]], [1, [281.88365901504517, 251.69167086710976]], [1, [250.38361141408387, 237.43751790907729]], [1, [292.26742864742107, 217.04246728140492]], [1, [289.19636886465867, 261.78472808359595]], [1, [274.86004666400333, 252.68507576164006]], [1, [247.8050351550705, 275.25927319513227]], [1, [283.00469909623439, 268.74555762563614]], [1, [260.6162491801428, 214.70157480655496]], [1, [209.13041383902333, 242.38263392545883]], [1, [222.21071306040139, 227.11391244594668]], [1, [247.38217392982645, 280.07777635044505]], [1, [293.21050981113143, 229.00001264354978]], [1, [259.22259716630776, 258.57115569683833]], [1, [281.80570195532903, 277.37816137842862]], [1, [211.24369914775457, 203.60529310682642]], [1, [290.23296425448297, 252.01919562149419]], [1, [271.08469428809656, 229.92390911764588]], [1, [276.22307747601144, 209.62901839959972]], [1, [296.43927051774642, 236.55981722566364]], [1, [273.7248702273248, 244.43096350683749]], [1, [228.71819495877088, 244.609440886725]], [1, [257.18190931955871, 245.81516499151587]], [1, [287.02370923399729, 238.72863288037286]], [1, [292.00556173765096, 237.48878166653364]], [1, [293.39151438050635, 268.4213983432071]], [1, [214.28086229487167, 213.73836834986074]], [1, [258.30574820539766, 209.32960638236241]], [1, [247.93982666188859, 213.89101357261035]], [1, [228.98499882425133, 269.37434939304978]], [1, [299.66700457690007, 269.29625732399131]], [1, [231.68668412636137, 254.21744949974419]], [1, [205.74562442673493, 288.61240146519981]], [1, [207.54180741224923, 297.71987799320891]], [1, [220.25558395502864, 271.92226539115825]], [1, [200.36333540179578, 220.1699911731624]], [1, [207.94005065782017, 231.52988379579045]], [1, [228.95234031382171, 211.97773922513844]], [1, [276.69155835312694, 261.26191626997985]], [1, [202.9283652977127, 264.4905266281728]], [1, [233.78584910701721, 240.60097097940294]], [1, [262.59972482619662, 248.57647929416908]], [1, [264.60481205229161, 291.23525609711839]], [1, [215.26486461520091, 257.94090481249469]], [1, [259.43983520281751, 297.8734007303363]], [1, [295.36331642906271, 294.60514908492945]], [1, [260.6378325906328, 247.28471676395293]], [1, [256.35638876515713, 236.75639736426967]], [1, [216.19851637252577, 236.09531751027407]], [1, [292.60372835863438, 270.63821819817582]], [1, [219.96840343361231, 208.23995616975245]], [1, [268.55115225579357, 299.62467119969665]], [1, [217.12794935878392, 204.6261886245012]], [1, [205.31062993459528, 221.98717216146531]], [1, [228.13487143266252, 218.42846780367552]], [1, [258.20337594219632, 227.19942786678698]], [1, [279.98216072293002, 252.25611587850901]], [1, [258.56438754069541, 236.20840260683411]], [1, [284.3522127575286, 213.07927930595127]], [1, [253.37308505227651, 204.037724786121]], [1, [287.37329410948576, 236.44485401030184]], [1, [252.01998825031325, 259.6850137343128]], [1, [245.54076492296426, 242.94525551475323]], [1, [228.86810033112661, 251.78837169304518]], [1, [208.10593945572103, 217.70589855194601]], [1, [275.05612710150052, 266.9738606685919]], [1, [296.42593340538286, 252.77607071785215]], [1, [200.2138554414847, 224.68117461219904]], [1, [237.66394921107405, 292.27873030219922]], [1, [255.97061874353895, 241.29300461127764]]]

distance=3000                 # Distance from 
v=[]
w=[]
#Iterating:
for i in xrange(m):
    for j in xrange (n):
        ob=array([i,j])
        pos, readable=raytrace(ob)
        if readable==True:
             imgf[i][j]=read(pos, img)
        else:  imgf[i][j]=(1,1,0)



# Results

plt.imshow(imgf).set_interpolation('nearest')
print time()-t0

#show()