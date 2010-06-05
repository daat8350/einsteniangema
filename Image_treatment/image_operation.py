import create

def check(im0, im1):
    m0=len(im0)
    n0=len(im0[0])
    m1=len(im1)
    n1=len(im1[0])

    if m0==m1 and n0==n1: return m0, n0
    else: raise 'Confusion error. Both images should have the same dimensions.'

def check_list(series):
    for im in xrange(1, len(series)-1):
        if check(im[i], series[0])==False:
            return False
    return True
        
def add(im0, im1):
    m, n=check(im0, im1)

    img=create.black(m,n)
    
    for i in xrange(m):
        for j in xrange(n):
            a=im0[m][n]+im1[m][n]             # Could fall outside RGB domain. To fix.
            for k in xrange(0, len(a)-1):
                if a[k]>1: a[k]=1
                elif if a[k]<0: a[k]=0
            img[m][n]=a

    return img


def substract(im0, im1):                        # Reveals differences between pictures.
    m, n=check(im0, im1)

    img=create.color(m,n, (0.5,0.5,0.5))
    
    for i in xrange(m):
        for j in xrange(n):
            a=im0[m][n]-im1[m][n]            # Could fall outside RGB domain. To fix.
            for k in xrange(0, len(a)-1):
                if a[k]>1: a[k]=1
                elif if a[k]<0: a[k]=0
            img[m][n]=a

    return img

        
