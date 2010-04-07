import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from pylab import show, savefig

img=mpimg.imread('stinkbug.png')

plt.imshow(img)
show()
##print img[0]
##print
##print img[0][0]


#[[ 0.35294119  0.51764709  0.4627451 ]
# [ 0.35294119  0.51764709  0.4627451 ]
# [ 0.35294119  0.51764709  0.4627451 ]
# ..., 
# [ 0.3764706   0.5411765   0.48235294]
# [ 0.3764706   0.5411765   0.48235294]
# [ 0.3764706   0.5411765   0.48235294]]


#[ 0.35294119  0.51764709  0.4627451 ]
