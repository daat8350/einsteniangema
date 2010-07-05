## Creates an image of m x n pixels white, black, or of a plain color.
# Version 1.0

from numpy import array, reshape, zeros, ones

def black(m, n):
    if type(m) in [int, float] and type(n) in [int, float]:
        if int(m)==m and m>0 and int(n)==n and n>0: return zeros(n*m*3).reshape(m, n, 3)
        else: raise 'TypeError. Dimensions should be positive integers.'
    else: raise 'TypeError. Dimensions should be valid numbers.'
    
   

def white(m, n):
    if type(m) in [int, float] and type(n) in [int, float]:
        if int(m)==m and m>0 and int(n)==n and n>0: return ones(n*m*3).reshape(m, n, 3)
        else: raise 'TypeError. Dimensions should be positive integers.'
    else: raise 'TypeError. Dimensions should be valid numbers.'
    

def color(m, n, col):
    if type(m) in [int, float] and type(n) in [int, float]:
        if int(m)==m and m>0 and int(n)==n and n>0:
            pass                                            # Trivial
        else: raise 'TypeError. Dimensions should be positive integers.'
    else: raise 'TypeError. Dimensions should be valid numbers.'
    
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
