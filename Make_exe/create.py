## Creates an image of m x n pixels white, black, or of a plain color.

from numpy import array, reshape, zeros, ones

def black(m, n): return zeros(n*m*3).reshape(m, n, 3)
def white(m, n): return ones(n*m*3).reshape(m, n, 3)
def color(m, n, col):
    if (type(col)!=list and type(col)!=tuple and type(col)!=numpy.ndarray):
        raise 'TypeError. Atribute color must be a list, a tuple or an array.'
    if (len(col)!=3 and len(col)!=4):
        raise 'RGBError. Atribute color must have three or four elements.'
    for i in col:
        if i<0 or i> 1:
            raise 'RGBError. Not a color.'
        
    img=ones(n*m*3).reshape(m, n, 3)
    for i in xrange(n):
        for j in xrange(m):
            img[j][i]*=col
    return img
