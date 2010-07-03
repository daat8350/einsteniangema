from random import random

lenses=[]
radius=1

m=100
n=100
top=100

for i in xrange(top):
    lenses.append([radius, [random()*m+200, random()*n+200]])
print lenses
